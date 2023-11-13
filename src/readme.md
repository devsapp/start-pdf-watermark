
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# start-pdf-watermark-v3 帮助文档
<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-pdf-watermark-v3&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-pdf-watermark-v3" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-pdf-watermark-v3&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-pdf-watermark-v3" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-pdf-watermark-v3&type=packageDownload">
  </a>
</p>

<description>

快速部署一个pdf加水印的应用到阿里云函数计算

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/start-pdf-watermark/tree/V3/src)

</codeUrl>
<preview>



</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  |
| --- |  --- |
| 函数计算 |  AliyunFCFullAccess |

</service>

<remark>



</remark>

<disclaimers>



</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-pdf-watermark-v3) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-pdf-watermark-v3) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init start-pdf-watermark-v3 -d start-pdf-watermark-v3`
  - 进入项目，并进行项目部署：`cd start-pdf-watermark-v3 && s deploy -y`
   
</deploy>

## 应用详情

<appdetail id="flushContent">

项目部署完成，可以通过`invoke`命令进行触发/测试, 有如下相关的参数：

```
{
    "pdf_file": "example.pdf",
    "mark_text": "AliyunFC",  // 水印文字， 如果给 PDF 加水印，该参数必填
    "pagesize": [595.275590551181, 841.8897637795275], // 可选参数，默认是 A4 大小， (21*cm, 29.7*cm), 其中 1cm=28.346456692913385
    "font": "Helvetica", // 字体，可选参数， 默认为 Helvetica,  中文字体可选择为 zenhei 或 microhei
    "font_size": 30, // 字体d大小，可选参数， 默认为 30
    "font_color": [0, 0, 0], // 字体颜色，格式为 RGB， 默认为黑色
    "rotate": 30, // 旋转角度, 可选参数， 默认为 0
    "opacity": 0.1, // 透明度, 可选参数， 默认为 0.1， 1 表示不透明
    "density": [198.4251968503937, 283.46456692913387] // 水印密度，水印文字间隔，默认是 [141.73228346456693, 141.73228346456693]，即（7*cm, 10*cm),  表示每个水印文字在横坐标和纵坐标的间隔分别是 7cm 和 10
}
```

函数调用成功后，生成的 pdf 文件在和输入的 pdf 文件在相同的 OSS 目录中，比如这个例子是在 example_out.pdf。

比如:

```bash
$ s invoke -e '{"pdf_file":"example.pdf", "mark_text": "AliyunFC", "rotate":30}'

# 如果是中文水印, font 为 zenhei 或者 microhei
$ s invoke -e '{"pdf_file":"example.pdf", "mark_text": "函数计算", "rotate":30, "font": "zenhei"}'
```

生成带有水印的 example_out.pdf 示例:

![](https://img.alicdn.com/imgextra/i1/O1CN01Tu6Ovz1gT5GcXhfm0_!!6000000004142-2-tps-647-842.png)

</appdetail>

## 使用文档

<usedetail id="flushContent">
</usedetail>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
