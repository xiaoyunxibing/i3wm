# 目录

[项目说明](#项目说明)

[i3wm 的评价](#i3wm的评价)

[壁纸](#arch壁纸里有4张1920x1080分辨率的壁纸。)

[电脑硬件情况](#电脑硬件情况)

[免驱动的硬件](#免驱动的硬件)

[Arch Linux 安装](#ArchLinux安装)

# 项目说明

我的 i3wm 配置

# i3wm 的评价

## 优点

i3wm 的多工作区模式, 对用户来说, 非常方便. 通过快捷键切换工作区。

平铺所有应用程序窗口，这样就不会浪费空间并且用完整个屏幕空间。

i3wm 速度很快。它既不冗杂、也不花哨。它的设计简单而高效。

## 缺点

配置麻烦。

# i3wm 官网

https://i3wm.org/

## i3wm 官网文档

https://i3wm.org/docs/

## i3wm 简体中文使用说明书

https://github.com/zjuyk/i3wm-userguide-zh

https://zjuyk.site/i3wm-userguide-zh/

# arch 壁纸里有 4 张 1920x1080 分辨率的壁纸

## 1.png

![1.png](https://github.com/xiaoyunxibing/i3wm/blob/main/arch%E5%A3%81%E7%BA%B8/1.png)

## 2.jpg

![2.jpg](https://github.com/xiaoyunxibing/i3wm/blob/main/arch%E5%A3%81%E7%BA%B8/2.jpg)

## 3.jpg

![3.jpg](https://github.com/xiaoyunxibing/i3wm/blob/main/arch%E5%A3%81%E7%BA%B8/3.jpg)

## 4.png

![4.png](https://github.com/xiaoyunxibing/i3wm/blob/main/arch%E5%A3%81%E7%BA%B8/4.png)

# 电脑硬件情况

名称：联想 小新Air 14 2020款(R5-4600U/16GB/512GB)

## 处理器

处理器：AMD锐龙5 4600U

核心/线程：六核心/十二线程

处理器系列：AMD Ryzen5

处理器主频：2.1GHz

最高频率：4GHz

三级缓存：L3 8M

## 运行内存
内存容量：16GB

内存类型：DDR4

## 存储设备

硬盘类型：SSD固态硬盘

硬盘容量：512GB SSD

## 显示屏

屏幕尺寸：14英寸

分辨率：1920×1080

显示比例：16:9

显示屏描述：16:9比例,宽屏,IPS屏,DC调光无屏闪，100%sRGB，300nits

## 显示卡

显卡类型：集成显卡

显存容量：共享系统内存

# 免驱动的硬件

## Linux 查看网卡型号、驱动版本

用于打印（“列表”）有关系统中所有PCI总线和设备的详细信息。

`lspci`

## 网络控制器：高通创锐讯QCA6174 802.11ac无线网络适配器

`Network controller: Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter`

属于开箱即用的网卡。

**QCA6174 802.11ac Wireless Network Adapter** <https://linux-hardware.org/index.php?id=pci:168c-003e-1a56-143a>

## 声卡

05:00.1 音频设备。Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon高清晰度音频控制器

`05:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller`

05:00.5 多媒体控制器。Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x音频协处理器(rev 01)

`05:00.5 Multimedia controller: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor (rev 01)`

05:00.6 音频设备。Advanced Micro Devices, Inc. [AMD] 家族17h/19h高清音频控制器

`05:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller`

**Advanced Micro Devices** https://en.wikipedia.org/wiki/Advanced_Micro_Devices

属于开箱即用的声卡。

**ACP/ACP3X/ACP6x Audio Coprocessor** https://linux-hardware.org/?id=pci:1022-15e2-1028-09e3

# Arch Linux 安装

教程参考 https://arch.icekylin.online/rookie/pre-install.html 和 https://archlinuxstudio.github.io/ArchLinuxTutorial/#/rookie/basic_install 和 https://wiki.archlinux.org/title/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87) 和 https://www.php.cn/blog/detail/35327.html

### 1. 禁用 reflector 服务

`systemctl stop reflector.service`

手机共享 usb 网络给电脑。

### 2. 更新系统时钟

`timedatectl set-ntp true`

### 3. 查看磁盘

`fdisk -l`

### 4. 使用 cfdisk 进行分区

`cfdisk /dev/你的磁盘`

### 5. 分区方案

EFI 分区 : 800M

根目录 : 剩下的空间

### 6. 查看磁盘并进行格式化操作

`lsblk`

`mkfs.fat -F32 /dev/你的 efi 分区`

`mkfs.ext4 /dev/你的根目录`

### 7. 挂载分区

`mount /dev/你的根目录 /mnt`

`mkdir /mnt/boot`

`mount /dev/你的efi分区 /mnt/boot`

### 8. 选择镜像源

`vim /etc/pacman.d/mirrorlist`

`Server = https://mirrors.ustc.edu.cn/archlinux/$repo/os/$arch # 中国科学技术大学开源镜像站` 放到首行

`pacman -Syu`

`pacman -S archlinux-keyring`

`ParallelDownloads = 5` 在 /etc/pacman.d/mirrorlist 里把注释去掉。开启多线程下载

### 9. 如果本地主密钥无法签署其他密钥

说明 https://archlinux.org/news/gnupg-21-and-the-pacman-keyring/

`pacman -Syu haveged`

`systemctl start haveged`

`rm -fr /etc/pacman.d/gnupg`

`pacman-key --init`

`pacman-key --populate archlinux`

