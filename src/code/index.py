# coding=utf-8
import sys
sys.path.insert(0, "/code/python")

from reportlab.pdfbase import pdfmetrics, ttfonts
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import subprocess
import oss2
import os
import json


# support chinese
pdfmetrics.registerFont(ttfonts.TTFont('zenhei', os.path.join(
    "/usr/share/fonts/truetype/wqy", 'wqy-zenhei.ttc')))
pdfmetrics.registerFont(ttfonts.TTFont('microhei', os.path.join(
    "/usr/share/fonts/truetype/wqy", 'wqy-microhei.ttc')))


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    print(pdf_file_in, pdf_file_mark, pdf_file_out)
    pdf_output = PdfFileWriter()
    with open(pdf_file_in, 'rb') as input_stream:
        pdf_input = PdfFileReader(input_stream, strict=False)

        pageNum = pdf_input.getNumPages()
        pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)

        for i in range(pageNum):
            page = pdf_input.getPage(i)
            page.mergePage(pdf_watermark.getPage(0))
            page.compressContentStreams()
            pdf_output.addPage(page)

        with open(pdf_file_out, 'wb') as f:
            pdf_output.write(f)


def _create_watermark(mark_text, pagesize=(21*cm, 29.7*cm), font="Helvetica", font_size=30, font_color=(0, 0, 0), rotate=0, opacity=1, density=(5*cm, 5*cm)):
    file_name = "/tmp/mark.pdf"
    c = canvas.Canvas(file_name, pagesize=pagesize)
    c.setFont(font, font_size)
    c.rotate(rotate)
    c.setStrokeColorRGB(0, 0, 0)
    r, g, b = font_color
    c.setFillColorRGB(r, g, b)
    c.setFillAlpha(opacity)

    row_gap, col_gap = density
    colN = int(pagesize[0]/col_gap)
    rowN = int(pagesize[1]/row_gap)
    x = colN * 4
    y = rowN * 4

    for i in range(y):
        for j in range(x):
            a = col_gap*(j - 2*colN)
            b = row_gap*(i - 2*rowN)
            c.drawString(a, b, mark_text)

    c.save()


def create_watermark(evt):
    mark_text = evt['mark_text']
    # 1cm = 28.346456692913385， defalut is A4, (21*cm, 29.7*cm)
    pagesize = evt.get(
        'pagesize', [595.275590551181, 841.8897637795275])
    font = evt.get('font', 'Helvetica')
    font_size = evt.get('font_size', 30)
    font_color = evt.get('font_color', (0, 0, 0))
    rotate = evt.get('rotate', 0)
    opacity = evt.get('opacity', 0.1)
    # default is (7*cm, 10*cm)
    density = evt.get('density', [198.4251968503937, 283.46456692913387])
    _create_watermark(mark_text, pagesize, font, font_size,
                      font_color, rotate, opacity, density)
    print('create_watermark success!')


def handler(event, context):
    region = context.region
    oss_endpoint = "http://oss-{}-internal.aliyuncs.com".format(region)
    print(event)
    evt = json.loads(event)
    word_file = evt["pdf_file"]
    fileDir, tempfilename = os.path.split(word_file)
    shortname, _ = os.path.splitext(tempfilename)
    creds = context.credentials
    auth = oss2.StsAuth(creds.access_key_id,
                        creds.access_key_secret, creds.security_token)
    bucket = oss2.Bucket(auth, oss_endpoint, os.environ['OSS_BUCKET'])
    bucket.get_object_to_file(word_file, '/tmp/' + tempfilename)
    pdf_file = os.path.join(fileDir, shortname + ".pdf")
    create_watermark(evt)
    local_pdf_out_file = '/tmp/' + shortname + "_out.pdf"
    add_watermark('/tmp/' + shortname + ".pdf",
                  '/tmp/mark.pdf', local_pdf_out_file)
    print('pdf add_watermark success!')

    result = bucket.put_object_from_file(
        pdf_file, local_pdf_out_file)

    subprocess.check_call(["ls", "-ll", "/tmp"])
    subprocess.check_call("rm -rf /tmp/*", shell=True)
    if result.status == 200:
        return "upload to oss success!"
    else:
        return "upload fail, error code %s " % result.status
