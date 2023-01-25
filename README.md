# 目录

[项目说明](#项目说明)

[i3wm的评价](#i3wm的评价)

[i3wm官网](#i3wm官网)

[壁纸](#arch壁纸里有4张1920x1080分辨率的壁纸。)

[电脑硬件情况](#电脑硬件情况)

[免驱动的硬件](#免驱动的硬件)

[ArchLinux安装](#ArchLinux安装)

# 项目说明

我的 i3wm 配置

# i3wm的评价

## 优点

i3wm 的多工作区模式, 对用户来说, 非常方便. 通过快捷键切换工作区。

平铺所有应用程序窗口，这样就不会浪费空间并且用完整个屏幕空间。

i3wm 速度很快。它既不冗杂、也不花哨。它的设计简单而高效。

## 缺点

配置麻烦。

# i3wm官网

https://i3wm.org/

## i3wm官网文档

https://i3wm.org/docs/

## i3wm简体中文使用说明书

https://github.com/zjuyk/i3wm-userguide-zh

https://zjuyk.site/i3wm-userguide-zh/

# arch壁纸里有4张1920x1080分辨率的壁纸

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

## Linux查看网卡型号、驱动版本

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

# ArchLinux安装

教程参考 https://arch.icekylin.online/rookie/pre-install.html 和 https://archlinuxstudio.github.io/ArchLinuxTutorial/#/rookie/basic_install 和 https://wiki.archlinux.org/title/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87) 和 https://www.php.cn/blog/detail/35327.html

# tty 字体变大

`setfont /usr/share/kbd/consolefonts/LatGrkCyr-12x22.psfu.gz`

或

`setfont ter-132n`

# 打开 Arch ISO 的 SSH

`passwd`

`systemctl start sshd`

`ip addr`

`ssh root@刚刚的 IP 地址`

# 设置 LANG 变量

`vim /etc/locale.gen`

    en_US.UTF-8 UTF-8
    zh_CN.UTF-8 UTF-8

`locale-gen`

`export LANG=zh_CN.UTF-8`

# 禁用 reflector 服务

`systemctl stop reflector.service`

# 更换国内软件仓库镜像源

`vim /etc/pacman.d/mirrorlist`

`Server = https://mirrors.bfsu.edu.cn/archlinux/$repo/os/$arch`

`pacman -Syy`

`pacman -S archlinux-keyring`

# 检查现在的分区

`lsblk`

或

`fdisk -l`

# 选择一个需要分区的磁盘

`cfdisk /dev/nvme0n1`

# 类型更改

`[Type] > 然后按下回车 Enter > 通过方向键 ↑ 和 ↓ 选中 > 最后按下回车 Enter`

# 格式化分区

引导分区

`mkfs.fat -F 32 /dev/nvme0n1p1`

Swap分区

`mkswap /dev/nvme0n1p2`

root分区

`mkfs.ext4 /dev/nvme0n1p3`

home分区

`mkfs.ext4 /dev/nvme0n1p4`

# 启用 swap

`swapon /dev/nvme0n1p2`

# 挂载分区

挂载root

`mount /dev/nvme0n1p3 /mnt`

`mkdir /mnt/boot`

`mkdir /mnt/home`

挂载引导分区

`mount /dev/nvme0n1p1 /mnt/boot`

挂载home

`mount /dev/nvme0n1p4 /mnt/home`

# 使用pacstrap安装系统

`pacstrap /mnt base linux linux-firmware`

# 生成 fstab 文件

`genfstab -U /mnt > /mnt/etc/fstab`

# chroot 进入新系统

`arch-chroot /mnt`

# 设置主机名

`echo 'myarch' > /etc/hostname`

`vim /etc/hosts`

    127.0.0.1   localhost
    ::1         localhost
    127.0.1.1   myarch.localdomain	myarch

可以使用 Tab 对齐。

# 设置时区

`ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`

# 将系统时间同步到硬件时间

`hwclock --systohc`

# 设置 Locale

编辑 /etc/locale.gen，去掉 `en_US.UTF-8 UTF-8` 以及 `zh_CN.UTF-8 UTF-8` 行前的注释符号（#）

`vim /etc/locale.gen`

# 生成 locale

`locale-gen`

`vim /etc/locale.conf`

    LANG=en_US.UTF-8
    LANG=zh_CN.UTF-8

# 为 root 用户设置密码

`passwd root`

# 配置 pacman

`vim /etc/pacman.conf`

取消掉 Color 和 ParallelDownloads = 5 的注释

`去掉 [multilib] 一节中两行的注释，来开启 32 位库支持`

取消"VerbosePkgLists"的注释。

```
[archlinuxcn]
Server = https://mirrors.bfsu.edu.cn/archlinuxcn/$arch
```

`pacman -Syu archlinuxcn-keyring`

# 安装软件

`pacman -S --needed xorg-server sudo vim xorg-xinit git i3-wm alacritty linux-headers yay networkmanager amd-ucode mesa lib32-mesa xf86-video-amdgpu vulkan-radeon lib32-vulkan-radeon fcitx5-im fcitx5-chinese-addons libva-mesa-driver lib32-libva-mesa-driver mesa-vdpau lib32-mesa-vdpau i3status-rust adobe-source-han-serif-cn-fonts wqy-zenhei noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra npm zsh neovim xclip neofetch ttf-dejavu ttf-fira-code ttf-jetbrains-mono pulseaudio ttf-font-awesome upower alsa-utils alsa-plugins sof-firmware alsa-ucm-conf v2ray v2raya-git chromium rofi xfce4-screenshooter dunst curl ttf-hack-nerd feh lsd ranger lxappearance pulseaudio-alsa pasystray fcitx5-nord icalingua++ python-bidi ffmpeg highlight atool lynx calibre jq mpv ffmpegthumbnailer pygmentize bat unrar w3m elinks xdg-utils p7zip ueberzug i3lock screenkey slop obs-studio jre-openjdk jdk-openjdk openjdk-doc openjdk-src java-openjfx java-openjfx-doc java-openjfx-src python-pip cmake dunst copyq arc-icon-theme ttf-nerd-fonts-symbols-2048-em ttf-iosevka-nerd`

`yay -S google-chrome visual-studio-code-bin visual-studio-code-insiders-bin clash-for-windows-bin whitesur-icon-theme whitesur-gtk-theme whitesur-cursor-theme-git picom-jonaburg-git rofi-power-menu`

# 无线网络

`systemctl enable NetworkManager`

# 准备非 root 用户

`useradd -m -G wheel -s /bin/bash qq`

`passwd qq`

# 给用户 sudo 权限

`EDITOR=vim visudo`

取消注释

```
%wheel ALL=(ALL:ALL) ALL
%wheel ALL=(ALL:ALL) NOPASSWD: ALL
%sudo ALL=(ALL:ALL) ALL
```

# 使用 systemd-boot

`bootctl --path=/boot install`

`bootctl update`

# 编辑EFI引导内容

`vim /boot/loader/loader.conf `

```
default  arch.conf
timeout  4
console-mode max
editor   no
```

# archlinux启动项配置

`vim /boot/loader/entries/arch.conf`

```
title          Arch Linux
linux          /vmlinuz-linux
initrd         /initramfs-linux.img
options        root=PARTUUID=nvme0n1p3的 rw loglevel=3 quiet systemd.show_status=1
```

# vim中查看硬盘并复制

`:r!blkid`

按y键完成拷贝
按p执行粘贴
按两次d就可以删除一行

# 添加pacman的hook文件，方便更新内核时更新efi分区

`mkdir /etc/pacman.d/hooks`

`vim /etc/pacman.d/hooks/100-systemd-boot.hook`

```
[Trigger]
Type = Package
Operation = Upgrade
Target = systemd

[Action]
Description = Updating systemd-boot
When = PostTransaction
Exec = /usr/bin/bootctl update
```

# 免 Display Manager 登录桌面

`vim ~/.bash_profile`

```
if [ "$(tty)" = "/dev/tty1" ]
then
    exec startx /usr/bin/i3
    exit
fi
```

# vim 配置

`vim ~/.vimrc`

```
set nocompatible " 不与 Vi 兼容
syntax on " 打开语法高亮
set encoding=utf-8 " 使用 utf-8 编码
set t_Co=256 " 启用256色
set laststatus=0 " 不显示状态栏
set showmatch " 光标遇到圆括号、方括号、大括号时，自动高亮对应的另一个圆括号、方括号和大括号
set hlsearch " 搜索时，高亮显示匹配结果
set incsearch " 输入搜索模式时，每输入一个字符，就自动跳到第一个匹配的结果
set clipboard=unnamedplus " 剪贴板

" Vim plugin
call plug#begin()

call plug#end()
```

# i3wm 配置

`vim ~/.config/i3/config`

```
# 这个文件是由i3-config-wizard(1)自动生成的。                                                                              
# 它不会被覆盖，所以你可以随意编辑。
#
# 如果你在某个时候改变了你的键盘布局，请删除
# 这个文件并重新运行i3-config-wizard(1)。
#

# i3 config file (v4)
#
# 请参阅https://i3wm.org/docs/userguide.html，以获得完整的参考资料! 

set $mod Mod4

# 窗口标题的字体。除非有不同的字体，否则也会被栏杆所使用。
# 在下面的bar {}块中使用。
font pango:monospace 8

# 这种字体被广泛安装，提供大量的unicode字形，从右到左
# 在视网膜/HIDPI显示器上的文本渲染和可扩展性（感谢pango）。
#font pango:DejaVu Sans Mono 8

# 使用dex启动XDG自动启动.desktop文件。另见
# https://wiki.archlinux.org/index.php/XDG_Autostart
exec --no-startup-id dex --autostart --environment i3

# xss-lock、nm-applet和pactl的组合是一个受欢迎的选择，所以
# 这里包括它们作为一个例子。按你认为合适的方式进行修改。

# xss-lock会抓取一个logind挂起的抑制锁，并使用i3lock来锁定该锁。
# 暂停前的屏幕。使用loginctl lock-session来锁定你的屏幕。
#exec --no-startup-id xss-lock --transfer-sleep-lock -- i3lock --nofork

# NetworkManager是在Linux上管理无线网络的最流行方式。
# 而nm-applet是一个独立于桌面环境的系统托盘GUI。
#exec --no-startup-id nm-applet

# 使用pactl来调整PulseAudio的音量。
set $refresh_i3status killall -SIGUSR1 i3status
bindsym XF86AudioRaiseVolume exec --no-startup-id pactl set-sink-volume @DEFAULT_SINK@ +10% && $refresh_i3status
bindsym XF86AudioLowerVolume exec --no-startup-id pactl set-sink-volume @DEFAULT_SINK@ -10% && $refresh_i3status
bindsym XF86AudioMute exec --no-startup-id pactl set-sink-mute @DEFAULT_SINK@ toggle && $refresh_i3status
bindsym XF86AudioMicMute exec --no-startup-id pactl set-source-mute @DEFAULT_SOURCE@ toggle && $refresh_i3status

# 使用鼠标+$mod将浮动窗口拖到他们想要的位置
floating_modifier $mod

# 通过左键点击标题栏来拖放移动平铺窗口。
# 或在持有浮动修改器的情况下左键点击窗口中的任何地方。
tiling_drag modifier titlebar

# 启动终端
#bindsym $mod+Return exec i3-sensible-terminal
bindsym $mod+Return exec --no-startup-id alacritty &
bindsym $mod+Shift+Return exec --no-startup-id code &

# 杀死焦点窗口
bindsym $mod+Shift+q kill
bindsym $mod+q kill

# 启动dmenu（一个程序启动器）。
#bindsym $mod+d exec --no-startup-id dmenu_run
bindsym $mod+d exec --no-startup-id rofi -show drun &
bindsym $mod+Shift+d exec --no-startup-id rofi -show window &
bindsym $mod+Shift+z exec --no-startup-id rofi -show power-menu -modi "power-menu:rofi-power-menu --choices=shutdown/reboot" & # 电源管理
# 一个更现代的dmenu替代品是rofi。
# bindcode $mod+40 exec "rofi -modi drun,run -show drun"
# 还有一个i3-dmenu-desktop，它只显示应用程序。
# .desktop文件。它是一个围绕dmenu的包装，所以你需要安装它。
# bindcode $mod+40 exec --no-startup-id i3-dmenu-desktop

# 改变焦点
bindsym $mod+h focus left
bindsym $mod+j focus down
bindsym $mod+k focus up
bindsym $mod+l focus right

# 或者，你可以使用光标键。
bindsym $mod+Left focus left
bindsym $mod+Down focus down
bindsym $mod+Up focus up
bindsym $mod+Right focus right

# 在水平方向上分裂
#bindsym $mod+h split h
bindsym $mod+g split h

# 垂直方向上的分裂
bindsym $mod+v split v

# 为被关注的容器进入全屏模式
bindsym $mod+f fullscreen toggle

# 改变容器的布局（堆叠式、标签式、切换式分割）。
#bindsym $mod+s layout stacking
#bindsym $mod+w layout tabbed
bindsym $mod+e layout toggle split
bindsym $mod+s exec --no-startup-id google-chrome-stable &
bindsym $mod+w exec --no-startup-id chromium &

# 拨动平铺/浮动
bindsym $mod+Shift+space floating toggle

# 在平铺/浮动窗口之间改变焦点
bindsym $mod+space focus mode_toggle

# 关注父容器
#bindsym $mod+a focus parent
bindsym $mod+a exec --no-startup-id cfw &
bindsym $mod+c exec --no-startup-id icalingua &
bindsym $mod+x exec --no-startup-id i3lock &
bindsym $mod+z exec --no-startup-id screenkey &

# 关注孩子的容器
#bindsym $mod+d focus child

# 定义默认工作空间的名称，我们以后为其配置键绑定。
# 我们使用变量来避免在多个地方重复名称。
set $ws1 "1"
set $ws2 "2"
set $ws3 "3"
set $ws4 "4"
set $ws5 "5"
set $ws6 "6"
set $ws7 "7"
set $ws8 "8"
set $ws9 "9"
set $ws10 "10"

# 切换到工作区
bindsym $mod+1 workspace number $ws1
bindsym $mod+2 workspace number $ws2
bindsym $mod+3 workspace number $ws3
bindsym $mod+4 workspace number $ws4
bindsym $mod+5 workspace number $ws5
bindsym $mod+6 workspace number $ws6
bindsym $mod+7 workspace number $ws7
bindsym $mod+8 workspace number $ws8
bindsym $mod+9 workspace number $ws9
bindsym $mod+0 workspace number $ws10

# 将焦点容器移至工作区
bindsym $mod+Shift+1 move container to workspace number $ws1
bindsym $mod+Shift+2 move container to workspace number $ws2
bindsym $mod+Shift+3 move container to workspace number $ws3
bindsym $mod+Shift+4 move container to workspace number $ws4
bindsym $mod+Shift+5 move container to workspace number $ws5
bindsym $mod+Shift+6 move container to workspace number $ws6
bindsym $mod+Shift+7 move container to workspace number $ws7
bindsym $mod+Shift+8 move container to workspace number $ws8
bindsym $mod+Shift+9 move container to workspace number $ws9
bindsym $mod+Shift+0 move container to workspace number $ws10

# 重新加载配置文件
bindsym $mod+Shift+c reload
# 原地重启i3（保留你的布局/会话，可用于升级i3）。
bindsym $mod+Shift+r restart
# exit i3 (将你从你的X会话中注销)
bindsym $mod+Shift+e exec "i3-nagbar -t warning -m 'You pressed the exit shortcut. Do you really want to exit i3? This will end your X session.' -B 'Yes, exit i3' 'i3-msg exit'"

# 调整窗口大小（你也可以用鼠标来调整）。  
mode "resize" {
    # 一旦你进入调整大小模式，这些绑定就会触发

    # 按左键将缩小窗口的宽度。
    # 按右键将增长窗口的宽度。
       # 向上按会缩小窗口的高度。
    # 按下去会增长窗口的高度。
    bindsym j resize shrink width 10 px or 10 ppt
    bindsym k resize grow height 10 px or 10 ppt
    bindsym l resize shrink height 10 px or 10 ppt
    bindsym semicolon resize grow width 10 px or 10 ppt

    # 同样的绑定，但是对于方向键来说
    bindsym Left resize shrink width 10 px or 10 ppt
    bindsym Down resize grow height 10 px or 10 ppt
    bindsym Up resize shrink height 10 px or 10 ppt
    bindsym Right resize grow width 10 px or 10 ppt

    # 恢复到正常状态。输入或Escape或$mod+r
    bindsym Return mode "default"
    bindsym Escape mode "default"
    bindsym $mod+r mode "default"
}

bindsym $mod+r mode "resize"

# 壁纸
exec --no-startup-id feh --bg-scale /home/qq/1.jpg &
# 截屏
bindsym $mod+Shift+s exec --no-startup-id xfce4-screenshooter &
bindsym $mod+Shift+a exec --no-startup-id obs &
# Fcitx5
exec --no-startup-id fcitx5 -d
# 设置窗口参数
for_window [class="^.*"] border pixel 2 # 把所有的窗口边框设为 2 像素
new_window 1pixel # 去掉标题栏
gaps inner 6
gaps outer 4
# 关闭X的屏幕保护
exec --no-startup-id xset s off & # 取消屏保
exec --no-startup-id xset dpms 0 0 0 & # 关闭DPMS 
exec --no-startup-id pasystray & # 声卡管理
exec --no-startup-id picom --experimental-backends -b # 启动 picom
exec --no-startup-id dunst & # 桌面通知
exec --no-startup-id copyq & # 剪切板管理器

# 启动i3bar以显示工作区栏（加上系统信息i3status
# 发现，如果有的话)
#bar {
#    status_command i3status
#}

bar {
    font pango:DejaVu Sans Mono, FontAwesome 12
    position top
    status_command /usr/bin/i3status-rs ~/.config/i3status-rust/config.toml
    colors {
        separator #666666
        background #222222
        statusline #dddddd
        focused_workspace #0088CC #0088CC #ffffff
        active_workspace #333333 #333333 #ffffff
        inactive_workspace #333333 #333333 #888888
        urgent_workspace #2f343a #900000 #ffffff
    }
}
```

# i3status-rust 配置

`mkdir ~/.config/i3status-rust`

`vim ~/.config/i3status-rust/config.toml`

```
theme = "solarized-dark"

icons = "awesome"

# 聚焦窗口
[[block]]
block = "focused_window"
max_width = 50
show_marks = "visible"

# 网络管理器
[[block]]
block = "networkmanager"
on_click = "alacritty -e sudo nmtui"
interface_name_exclude = ['br\-[0-9a-f]{12}', 'docker\d+']
interface_name_include = []
ap_format = "{ssid} {strength}"
device_format = "{icon} {ap}" 
      
# 背光
[[block]]
block = "backlight"
minimum = 15
maximum = 100
step_width = 1
invert_icons = true
format = "{brightness:6#100} {brightness}"

# 声音
[[block]]
block = "sound"
step_width = 1
format = "{volume:5#110} {volume:01}"

# 电池
[[block]]
block = "battery"
interval = 1
driver = "upower"
format = "{percentage:6#100} {percentage} {time}"

# 时间
[[block]]
block = "time"
format = "%F %A %R"
interval = 1
```

# 启动 v2rayA 和 设置 v2rayA 自动启动

`sudo systemctl start v2raya.service`

`sudo systemctl enable v2raya.service`

`yay -S ttf-font-awesome-4 ttf-font-awesome-5`

# 配置 neovim 使用系统剪贴板

`mkdir ~/.config/nvim`

`vim ~/.config/nvim/init.lua`

添加一行

`set clipboard+=unnamedplus`

## 有时执行wget或curl来下载国外的东西，需要临时在终端启用代理时，可以使用如下命令

```
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

# 配置 alacritty 主题和字体

`mkdir ~/.config/alacritty`

`cp /usr/share/doc/alacritty/example/alacritty.yml ~/.config/alacritty/alacritty.yml`

`sudo npm i -g alacritty-themes`

`alacritty-themes`

`vim ~/.bashrc`

```
alias at='alacritty-themes' # 终端主题
```

`vim /home/qq/.config/alacritty/alacritty.yml`

```
# 设置字体
font:
    normal:
        family: "Hack Nerd Font"
        style: Regular
    bold:
        family: "Hack Nerd Font"
        style: Bold
    italic:
        family: "Hack Nerd Font"
        style: Italic
    bold_italic:
        family: "Hack Nerd Font"
        style: Bold Italic

    # 字大小
    size: 9.0
    
    offset:
    x: 0
    y: 0
  glyph_offset:
    x: 0
    y: 0

window:
  padding:
    x: 2
    y: 2
```

删除备份文件

`rm ~/.config/alacritty/alacritty.yml.*`

# Oh My Zsh

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

南京大学源

安装

```
git clone https://mirror.nju.edu.cn/git/ohmyzsh.git
cd ohmyzsh/tools
REMOTE=https://mirror.nju.edu.cn/git/ohmyzsh.git sh install.sh
```

切换已有 ohmyzsh 至镜像源

```
git -C $ZSH remote set-url origin https://mirror.nju.edu.cn/git/ohmyzsh.git
git -C $ZSH pull
```

# Powerlevel10k

```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

中国用户可以使用 gitee.com 上的官方镜像加速下载

```
git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

# zsh-autosuggestions

ohmyzsh插件，提供了命令提示功能，能够基于已经输入的命令历史进行智能补全。

```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

# zsh-syntaxhighlighting

提供了zsh当中命令的语法高亮

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

# zshrc

`vim ~/.zshrc`

```
plugins=( 
    sudo
    zsh-autosuggestions
    zsh-syntax-highlighting
)
```

```
ZSH_THEME="powerlevel10k/powerlevel10k"
```

```
if [ "$(tty)" = "/dev/tty1" ]
then
    exec startx /usr/bin/i3
    exit
fi
```

```
alias at='alacritty-themes' # 终端主题
# 临时在终端启用代理
alias clash1='export http_proxy=http://127.0.0.1:7890'
alias clash2='export https_proxy=http://127.0.0.1:7890'
alias gj='poweroff' # 立刻关机
alias cq='reboot' # 重启
```

# Fcitx5

`mkdir ~/.config/autostart`

`cp /usr/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart/`

`sudo vim /etc/environment`

```
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
```

# rofi-theme

`icon主题可以从系统的主题目录（/usr/share/icons）里拷贝一份到~/.icons/或者~/.local/share/icons/里。`

`git clone https://github.com/lr-tech/rofi-themes-collection.git`

`mkdir -p ~/.local/share/rofi/themes/`

`cp ~/rofi-themes-collection/themes/nord.rasi ~/.local/share/rofi/themes/`

`rofi-theme-selector`

`Alt+a`

`vim ~/.config/rofi/config.rasi`

```
configuration {
	/* 配置显示类型 */
	modi: "window,run,ssh,drun";
    /* 配置是否支持icon以及icon主题 */
	show-icons: true;
    icon-theme: "WhiteSur-dark";
	drun-icon-theme: "WhiteSur-dark";
}
```

# ranger

`ranger --copy-config=all`

```
rc.conf - 选项设置和快捷键
commands.py - 能通过 : 执行的命令
rifle.conf - 指定不同类型的文件的默认打开程序。
scope.sh - 文件预览相关配置
```

## scope.sh

```
#!/usr/bin/env bash

set -o noclobber -o noglob -o nounset -o pipefail
IFS=$'\n'

## 如果选项`use_preview_script`被设置为`true`。
## 那么这个脚本就会被调用，它的输出就会显示在ranger中。
## 支持ANSI颜色代码。
## STDIN被禁用，所以交互式脚本不能正常工作

## 这个脚本被认为是一个配置文件，必须手动更新。
## 如果你升级游侠，它将不被触动。

## 因为我们对脚本#的评论做了一些自动测试，需要
## 要翻倍的。被注释掉的代码，因为它是一个替代的
## 例如，只得到一个#。

## 退出代码的含义。
## code | meaning    | action of ranger
## -----+------------+-------------------------------------------
## 0    | success    | Display stdout as preview
## 1    | no preview | Display no preview at all
## 2    | plain text | Display the plain content of the file
## 3    | fix width  | Don't reload when width changes
## 4    | fix height | Don't reload when height changes
## 5    | fix both   | Don't ever reload
## 6    | image      | Display the image `$IMAGE_CACHE_PATH` points to as an image preview
## 7    | image      | Display the file directly as an image

## 脚本参数
FILE_PATH="${1}"         # 突出显示文件的完整路径
PV_WIDTH="${2}"          # 预览窗格的宽度（适合的字符数）。
## shellcheck disable=SC2034 # PV_HEIGHT是为了方便而提供的，未被使用。
PV_HEIGHT="${3}"         # 预览窗格的高度（适合的字符数）。
IMAGE_CACHE_PATH="${4}"  # 应该用于缓存图像预览的完整路径
PV_IMAGE_ENABLED="${5}"  # 如果启用了图像预览，则为'真'，否则为'假'。

FILE_EXTENSION="${FILE_PATH##*.}"
FILE_EXTENSION_LOWER="$(printf "%s" "${FILE_EXTENSION}" | tr '[:upper:]' '[:lower:]')"

## 设置
HIGHLIGHT_SIZE_MAX=262143  # 256KiB
HIGHLIGHT_TABWIDTH=${HIGHLIGHT_TABWIDTH:-8}
HIGHLIGHT_STYLE=${HIGHLIGHT_STYLE:-pablo}
HIGHLIGHT_OPTIONS="--replace-tabs=${HIGHLIGHT_TABWIDTH} --style=${HIGHLIGHT_STYLE} ${HIGHLIGHT_OPTIONS:-}"
PYGMENTIZE_STYLE=${PYGMENTIZE_STYLE:-autumn}
OPENSCAD_IMGSIZE=${RNGR_OPENSCAD_IMGSIZE:-1000,1000}
OPENSCAD_COLORSCHEME=${RNGR_OPENSCAD_COLORSCHEME:-Tomorrow Night}

handle_extension() {
    case "${FILE_EXTENSION_LOWER}" in
        ## 档案
        a|ace|alz|arc|arj|bz|bz2|cab|cpio|deb|gz|jar|lha|lz|lzh|lzma|lzo|\
        rpm|rz|t7z|tar|tbz|tbz2|tgz|tlz|txz|tZ|tzo|war|xpi|xz|Z|zip)
            atool --list -- "${FILE_PATH}" && exit 5
            bsdtar --list --file "${FILE_PATH}" && exit 5
            exit 1;;
        rar)
            ## 通过提供空密码避免密码提示
            unrar lt -p- -- "${FILE_PATH}" && exit 5
            exit 1;;
        7z)
            ## 通过提供空密码避免密码提示
            7z l -p -- "${FILE_PATH}" && exit 5
            exit 1;;

        ## PDF
        pdf)
            ## 预览为文本转换
            pdftotext -l 10 -nopgbrk -q -- "${FILE_PATH}" - | \
              fmt -w "${PV_WIDTH}" && exit 5
            mutool draw -F txt -i -- "${FILE_PATH}" 1-10 | \
              fmt -w "${PV_WIDTH}" && exit 5
            exiftool "${FILE_PATH}" && exit 5
            exit 1;;

        ## BitTorrent
        torrent)
            transmission-show -- "${FILE_PATH}" && exit 5
            exit 1;;

        ## 开放文档
        odt|ods|odp|sxw)
            ## 预览为文本转换
            odt2txt "${FILE_PATH}" && exit 5
            ## 预览为markdown转换
            pandoc -s -t markdown -- "${FILE_PATH}" && exit 5
            exit 1;;

        ## XLSX
        xlsx)
            ## 预览为csv转换
            ## Uses: https://github.com/dilshod/xlsx2csv
            xlsx2csv -- "${FILE_PATH}" && exit 5
            exit 1;;

        ## HTML
        htm|html|xhtml)
            ## 预览为文本转换
            w3m -dump "${FILE_PATH}" && exit 5
            lynx -dump -- "${FILE_PATH}" && exit 5
            elinks -dump "${FILE_PATH}" && exit 5
            pandoc -s -t markdown -- "${FILE_PATH}" && exit 5
            ;;

        ## JSON
        json)
            jq --color-output . "${FILE_PATH}" && exit 5
            python -m json.tool -- "${FILE_PATH}" && exit 5
            ;;

        ## 没有检测到直接流数字/传输（DSDIFF）和wavpack
        ## 由文件(1)。
        dff|dsf|wv|wvc)
            mediainfo "${FILE_PATH}" && exit 5
            exiftool "${FILE_PATH}" && exit 5
            ;; # Continue with next handler on failure
    esac
}

handle_image() {
    ## 如果有多个选项，预览的尺寸或必须是
    ## 从矢量图形渲染出来的。如果转换程序允许
    ## 在保持长宽比的情况下，只指定一个尺寸，宽度
    ## 将被使用。
    local DEFAULT_SIZE="1920x1080"

    local mimetype="${1}"
    case "${mimetype}" in
        ## SVG
         image/svg+xml|image/svg)
             convert -- "${FILE_PATH}" "${IMAGE_CACHE_PATH}" && exit 6
             exit 1;;

        ## DjVu
         image/vnd.djvu)
             ddjvu -format=tiff -quality=90 -page=1 -size="${DEFAULT_SIZE}" \
                   - "${IMAGE_CACHE_PATH}" < "${FILE_PATH}" \
                   && exit 6 || exit 1;;

        ## 图片
        image/*)
            local orientation
            orientation="$( identify -format '%[EXIF:Orientation]\n' -- "${FILE_PATH}" )"
            ## 如果方向数据是存在的，并且图像实际
            ## 需要旋转（"1 "表示不旋转）...
            if [[ -n "$orientation" && "$orientation" != 1 ]]; then
                ## ...根据EXIF数据自动旋转图像。
                convert -- "${FILE_PATH}" -auto-orient "${IMAGE_CACHE_PATH}" && exit 6
            fi

            ## `w3mimgdisplay'将被调用，用于所有的图像（除非被覆盖）。
            ## 同上），但对于不支持的类型可能会失败。
            exit 7;;

        ## 视频
         video/*)
             # Thumbnail
             ffmpegthumbnailer -i "${FILE_PATH}" -o "${IMAGE_CACHE_PATH}" -s 0 && exit 6
             exit 1;;

        ## PDF
         application/pdf)
             pdftoppm -f 1 -l 1 \
                      -scale-to-x "${DEFAULT_SIZE%x*}" \
                      -scale-to-y -1 \
                      -singlefile \
                      -jpeg -tiffcompression jpeg \
                      -- "${FILE_PATH}" "${IMAGE_CACHE_PATH%.*}" \
                 && exit 6 || exit 1;;


        ## ePub, MOBI, FB2 (using Calibre)
         application/epub+zip|application/x-mobipocket-ebook|\
         application/x-fictionbook+xml)
             # ePub (using https://github.com/marianosimone/epub-thumbnailer)
             epub-thumbnailer "${FILE_PATH}" "${IMAGE_CACHE_PATH}" \
                 "${DEFAULT_SIZE%x*}" && exit 6
             ebook-meta --get-cover="${IMAGE_CACHE_PATH}" -- "${FILE_PATH}" \
                 >/dev/null && exit 6
             exit 1;;

        ## 字体
        application/font*|application/*opentype)
            preview_png="/tmp/$(basename "${IMAGE_CACHE_PATH%.*}").png"
            if fontimage -o "${preview_png}" \
                         --pixelsize "120" \
                         --fontname \
                         --pixelsize "80" \
                         --text "  ABCDEFGHIJKLMNOPQRSTUVWXYZ  " \
                         --text "  abcdefghijklmnopqrstuvwxyz  " \
                         --text "  0123456789.:,;(*!?') ff fl fi ffi ffl  " \
                         --text "  The quick brown fox jumps over the lazy dog.  " \
                         "${FILE_PATH}";
            then
                convert -- "${preview_png}" "${IMAGE_CACHE_PATH}" \
                    && rm "${preview_png}" \
                    && exit 6
            else
                exit 1
            fi
            ;;

        ## 使用里面的第一张图片预览档案。
        ## (例如，对漫画书的收藏非常有用）。
        # application/zip|application/x-rar|application/x-7z-compressed|\
        #     application/x-xz|application/x-bzip2|application/x-gzip|application/x-tar)
        #     local fn=""; local fe=""
        #     local zip=""; local rar=""; local tar=""; local bsd=""
        #     case "${mimetype}" in
        #         application/zip) zip=1 ;;
        #         application/x-rar) rar=1 ;;
        #         application/x-7z-compressed) ;;
        #         *) tar=1 ;;
        #     esac
        #     { [ "$tar" ] && fn=$(tar --list --file "${FILE_PATH}"); } || \
        #     { fn=$(bsdtar --list --file "${FILE_PATH}") && bsd=1 && tar=""; } || \
        #     { [ "$rar" ] && fn=$(unrar lb -p- -- "${FILE_PATH}"); } || \
        #     { [ "$zip" ] && fn=$(zipinfo -1 -- "${FILE_PATH}"); } || return
        #
        #     fn=$(echo "$fn" | python -c "import sys; import mimetypes as m; \
        #             [ print(l, end='') for l in sys.stdin if \
        #               (m.guess_type(l[:-1])[0] or '').startswith('image/') ]" |\
        #         sort -V | head -n 1)
        #     [ "$fn" = "" ] && return
        #     [ "$bsd" ] && fn=$(printf '%b' "$fn")
        #
        #     [ "$tar" ] && tar --extract --to-stdout \
        #         --file "${FILE_PATH}" -- "$fn" > "${IMAGE_CACHE_PATH}" && exit 6
        #     fe=$(echo -n "$fn" | sed 's/[][*?\]/\\\0/g')
        #     [ "$bsd" ] && bsdtar --extract --to-stdout \
        #         --file "${FILE_PATH}" -- "$fe" > "${IMAGE_CACHE_PATH}" && exit 6
        #     [ "$bsd" ] || [ "$tar" ] && rm -- "${IMAGE_CACHE_PATH}"
        #     [ "$rar" ] && unrar p -p- -inul -- "${FILE_PATH}" "$fn" > \
        #         "${IMAGE_CACHE_PATH}" && exit 6
        #     [ "$zip" ] && unzip -pP "" -- "${FILE_PATH}" "$fe" > \
        #         "${IMAGE_CACHE_PATH}" && exit 6
        #     [ "$rar" ] || [ "$zip" ] && rm -- "${IMAGE_CACHE_PATH}"
        #     ;;
    esac

    # openscad_image() {
    #     TMPPNG="$(mktemp -t XXXXXX.png)"
    #     openscad --colorscheme="${OPENSCAD_COLORSCHEME}" \
    #         --imgsize="${OPENSCAD_IMGSIZE/x/,}" \
    #         -o "${TMPPNG}" "${1}"
    #     mv "${TMPPNG}" "${IMAGE_CACHE_PATH}"
    # }

    # case "${FILE_EXTENSION_LOWER}" in
    #     ## 3D models
    #     ## OpenSCAD only supports png image output, and ${IMAGE_CACHE_PATH}
    #     ## is hardcoded as jpeg. So we make a tempfile.png and just
    #     ## move/rename it to jpg. This works because image libraries are
    #     ## smart enough to handle it.
    #     csg|scad)
    #         openscad_image "${FILE_PATH}" && exit 6
    #         ;;
    #     3mf|amf|dxf|off|stl)
    #         openscad_image <(echo "import(\"${FILE_PATH}\");") && exit 6
    #         ;;
    # esac
}

handle_mime() {
    local mimetype="${1}"
    case "${mimetype}" in
        ## RTF and DOC
        text/rtf|*msword)
            ## 预览为文本转换
            ## note: catdoc does not always work for .doc files
            ## catdoc: http://www.wagner.pp.ru/~vitus/software/catdoc/
            catdoc -- "${FILE_PATH}" && exit 5
            exit 1;;

        ## DOCX, ePub, FB2 (using markdown)
        ## You might want to remove "|epub" and/or "|fb2" below if you have
        ## 取消了其他预览这些格式的方法
        *wordprocessingml.document|*/epub+zip|*/x-fictionbook+xml)
            ## 预览为markdown转换
            pandoc -s -t markdown -- "${FILE_PATH}" && exit 5
            exit 1;;

        ## XLS
        *ms-excel)
            ## 预览为csv转换
            ## xls2csv带有catdoc。
            ##   http://www.wagner.pp.ru/~vitus/software/catdoc/
            xls2csv -- "${FILE_PATH}" && exit 5
            exit 1;;

        ## Text
        text/* | */xml)
            ## 语法高亮
            if [[ "$( stat --printf='%s' -- "${FILE_PATH}" )" -gt "${HIGHLIGHT_SIZE_MAX}" ]]; then
                exit 2
            fi
            if [[ "$( tput colors )" -ge 256 ]]; then
                local pygmentize_format='terminal256'
                local highlight_format='xterm256'
            else
                local pygmentize_format='terminal'
                local highlight_format='ansi'
            fi
            env HIGHLIGHT_OPTIONS="${HIGHLIGHT_OPTIONS}" highlight \
                --out-format="${highlight_format}" \
                --force -- "${FILE_PATH}" && exit 5
            env COLORTERM=8bit bat --color=always --style="plain" \
                -- "${FILE_PATH}" && exit 5
            pygmentize -f "${pygmentize_format}" -O "style=${PYGMENTIZE_STYLE}"\
                -- "${FILE_PATH}" && exit 5
            exit 2;;

        ## DjVu
        image/vnd.djvu)
            ## 预览为文本转换（需要djvulibre）。
            djvutxt "${FILE_PATH}" | fmt -w "${PV_WIDTH}" && exit 5
            exiftool "${FILE_PATH}" && exit 5
            exit 1;;

        ## 图片
        image/*)
            ## 预览为文本转换
            # img2txt --gamma=0.6 --width="${PV_WIDTH}" -- "${FILE_PATH}" && exit 4
            exiftool "${FILE_PATH}" && exit 5
            exit 1;;

        ## 视频和音频
        video/* | audio/*)
            mediainfo "${FILE_PATH}" && exit 5
            exiftool "${FILE_PATH}" && exit 5
            exit 1;;
    esac
}

handle_fallback() {
    echo '----- File Type Classification -----' && file --dereference --brief -- "${FILE_PATH}" && exit 5
    exit 1
}


MIMETYPE="$( file --dereference --brief --mime-type -- "${FILE_PATH}" )"
if [[ "${PV_IMAGE_ENABLED}" == 'True' ]]; then
    handle_image "${MIMETYPE}"
fi
handle_extension
handle_mime "${MIMETYPE}"
handle_fallback

exit 1
```

## rc.conf

```
# ===================================================================
# 这个文件包含ranger的默认启动命令。
# 要改变它们，建议创建/etc/ranger/rc.conf
# (全系统)或~/.config/ranger/rc.conf (每个用户)，并添加你的自定义
# 那里的命令。
#
# 如果你把这整个文件复制到那里，你可能想设置环境
# 变量RANGER_LOAD_DEFAULT_RC为FALSE，以避免加载两次。
#
# 这个文件的目的主要是为了定义键盘绑定和设置。
# 对于运行更复杂的Python代码，请在 "plugins/"或""创建一个插件。
# commands.py "中的一个命令。
#
# 每一行都是一个命令，将在用户界面前运行
# 被初始化。 因此，你不能使用那些依赖
# 在用户界面上，如:删除或:标记。
# ===================================================================

# ===================================================================
# == 选择
# ===================================================================

# 应该使用哪种视图模式？ 可能的值是。
#     米勒。使用显示多层次结构的米勒列
#     multipane。像Midnight-commander一样的多窗格视图，显示所有标签的下一个。
#                相互之间
set viewmode miller
#set viewmode multipane

# 有多少列，它们的相对宽度是多少？
set column_ratios 1,3,4

# 哪些文件应该被隐藏？(正则表达式)
set hidden_filter ^\.|\.(?:pyc|pyo|bak|swp)$|^lost\+found$|^__(py)?cache__$

# 显示隐藏的文件？你可以通过输入'zh'来切换这个功能。
set show_hidden true

# 文件图标
default_linemode devicons

# 无边框列可能会导致图像预览中出现条纹。
set draw_borders true

# 运行 "delete" 命令时要求确认？
# 有效值是 "always", "never", "multiple" (default)
# 如果是 "多个"，ranger只会询问你是否一次删除多个文件。
set confirm_on_delete multiple

# 为文件预览脚本使用非默认的路径？
# 在ranger中配备了scope.sh，这个脚本可以调用外部程序（见
# README.md的依赖性）来预览图像、档案等。
set preview_script ~/.config/ranger/scope.sh

# 使用外部预览脚本或显示简单的纯文本或图像预览？
set use_preview_script true

# 自动计算目录中的文件，甚至在进入这些文件之前？
set automatically_count_files true

# 运行某些图像查看器时，打开此目录中的所有图像
# 像feh或sxiv？ 你仍然可以通过标记来打开选定的文件。
set open_all_images true

# 要了解版本控制系统和显示信息。
set vcs_aware true

# git、hg、bzr、svn四个后台的状态。可能的状态是
# disabled, local (only show local info), enabled (show local and remote
# information).
# 禁用，本地（只显示本地信息），启用（显示本地和远程信息）。
set vcs_backend_git enabled
set vcs_backend_hg disabled
set vcs_backend_bzr disabled
set vcs_backend_svn disabled

# 在状态栏中显示长的提交信息时，将其截断为这个长度。
set vcs_msg_length 50

# 使用支持的图像预览协议之一
set preview_images false

# 设置预览图像的方法。支持的方法。
#
# * w3m (default):
#   用外部命令 "w3mimgpreview "预览全彩图像？
#   这需要控制台网络浏览器 "w3m "和一个支持的终端。
#   它已经成功地用 "xterm "和 "urxvt "进行了测试，没有tmux。
#
# * iterm2:
#   使用iTerm2图像预览器全彩预览图像
#   (http://iterm2.com/images.html). 这需要使用iTerm2编译的
#   支持图像预览。
#
#   This feature relies on the dimensions of the terminal's font.  By default, a
#   width of 8 and height of 11 are used.  To use other values, set the options
#   iterm2_font_width and iterm2_font_height to the desired values.
#   这一功能依赖于终端的字体尺寸。在默认情况下，使用 宽度为8，高度为11。
#   要使用其他值，请将选项 iterm2_font_width和iterm2_font_height设置为需要的值。
#
# * terminology:
#   Previews images in full color in the terminology terminal emulator.
#   Supports a wide variety of formats, even vector graphics like svg.
#
# * urxvt:
#   Preview images in full color using urxvt image backgrounds. This
#   requires using urxvt compiled with pixbuf support.
#
# * urxvt-full:
#   The same as urxvt but utilizing not only the preview pane but the
#   whole terminal window.
#
# * kitty:
#   Preview images in full color using kitty image protocol.
#   Requires python PIL or pillow library.
#   If ranger does not share the local filesystem with kitty
#   the transfer method is changed to encode the whole image;
#   while slower, this allows remote previews,
#   for example during an ssh session.
#   Tmux is unsupported.
#
# * ueberzug:
#   用外部命令 "ueberzug "预览全彩图像。
#   图像是通过使用子窗口显示的。
#   只针对在GNU/Linux中运行X11的用户。
set preview_images_method ueberzug

# 用w3m方法显示图像前的延迟，单位是秒。
# 在遇到显示器损坏的情况下，增加它。
set w3m_delay 0.02

# 当使用一个需要这样的终端时，手动调整w3mimg的偏移量
set w3m_offset 0

# 默认的iTerm2字体大小（见： preview_images_method: iterm2）。
set iterm2_font_width 8
set iterm2_font_height 11

# 使用unicode"... "字符来标记截止的文件名？
set unicode_ellipsis false

# 支持BIDI - 尝试正确显示RTL语言（希伯来语、阿拉伯语）的文件名。
# 需要 python-bidi pip 包。
set bidi_support false

# 在书签预览框中显示dotfiles？
set show_hidden_bookmarks true

# 使用哪种颜色方案？ 这些色系默认是可用的。
# default, jungle, snow, solarized
set colorscheme default

# 预览文件在最右边一栏？
# 如果没有什么要预览的，就把最后一列折叠（缩小）？
set preview_files true
set preview_directories true
set collapse_preview true

# 在纯文本预览中包裹长行？
set wrap_plaintext_previews false

# 退出时保存控制台历史记录？
set save_console_history true

# Draw the status bar on top of the browser window (default: bottom)
# 将状态栏画在浏览器窗口的顶部（默认：底部）。
set status_bar_on_top true

# 在状态栏中画出一个进度条，显示所有的平均状态。
# 目前正在运行的支持进度条的任务？
set draw_progress_bar_in_status_bar true

# Draw borders around columns? (separators, outline, both, or none)
# 在列周围绘制边框？(分隔符、轮廓、两者都有或没有)
# 分隔符是列之间的垂直线。
# 大纲在所有列的周围画出一个方框。
# 两者结合起来。
set draw_borders none

# 在标签中显示目录名称？
set dirname_in_tabs true

# 启用鼠标支持？
set mouse_enabled true

# 在主栏或状态栏中显示文件大小？
set display_size_in_main_column true
set display_size_in_status_bar true

# 在状态栏中显示可用磁盘空间？
set display_free_space_in_status_bar true

# 在所有列中显示文件标签还是只在主列中显示？
set display_tags_in_all_columns true

# 为窗口设置一个标题？同时更新`WM_NAME`和`WM_ICON_NAME`。
set update_title true

# 将tmux/screen的窗口名称设为 "ranger"？
set update_tmux_title true

# 如果标题变长就缩短？ 这个数字定义了多少个
# 列表中的所有目录都是一次性显示的，0将关闭这一功能。
set shorten_title 3

# 在标题栏中显示主机名？
set hostname_in_titlebar true

# 在ranger的标题栏（第一行）中用~来缩写$HOME？
set tilde_in_titlebar true

# 历史上应该保留多少次目录变化或控制台命令？
set max_history_size 20
set max_console_history_size 50

# 滚动时尽量在上/下边框之间保持这么大的空间。
set scroll_offset 8

# 每次按键后都要刷新输入吗？ (当游侠滞后时可以注意到)。
set flushinput true

# 在没有预览的情况下，右边有填充物？
# 这允许你点击进入空间来运行该文件。
set padding_right true

# 即时保存书签（与mX和`X一起使用）？
# 这有助于在多个游侠之间同步书签。
# 实例，但会导致*轻微的性能损失。
# 如果是假的，书签会在退出ranger时被保存。
set autosave_bookmarks true

# 将"`"书签保存到磁盘。 这可以用来切换到最后一个
# 通过键入"``"，就可以看到目录。
set save_backtick_bookmark true

# 你可以通过使用以下方法来显示目录的 "真实 "累积大小
# 命令:get_cumulative_size或键入 "dc"。 该大小是昂贵的，以
# 计算，不会自动更新。 你可以选择
# 通过打开这个选项，可以自动更新它。
set autoupdate_cumulative_size true

# 开启这个功能对屏幕阅读器来说是有意义的。
set show_cursor false

# 其中之一：size、natural、basename、atime、ctime、mtime、type、random
set sort natural

# 额外的排序选项
set sort_reverse false
set sort_case_insensitive true
set sort_directories_first true
set sort_unicode false

# 如果使用Alt键的组合键对你不起作用，就启用这个功能。
# (特别是在xterm上)
set xterm_alt_key false

# 是否在cd命令中包括书签
set cd_bookmarks true

# 改变cd命令标签完成时的大小写敏感性
set cd_tab_case sensitive

# U在 "cd "命令中使用模糊的制表符完成。比如说。
# ":cd /u/lo/b<tab>" 扩大到 ":cd /usr/local/bin".
set cd_tab_fuzzy true

# 避免预览大于此大小的文件，单位为字节。 使用0的值来
# 禁用此功能。
set preview_max_size 0

# 达到这个大小的关键提示列表有其子列表的扩展。
# 否则，子图将被替换成"..."。
set hint_collapse_threshold 10

# 将突出显示的文件添加到标题栏的路径中
set show_selection_in_titlebar true

# ranger空闲时等待用户输入的延迟时间，以毫秒为单位。
# 的分辨率为100ms。 较低的延迟减少了目录更新之间的滞后，但
# 增加CPU负载。
set idle_delay 2000

# 当元数据管理器模块寻找元数据时，它应该只寻找
# 在当前目录下的".metadata.json "文件，或者做一个深入的搜索并
# 也要检查当前目录以上的所有目录吗？
set metadata_deep_search false

# 离开一个目录时清除所有现有的过滤器
set clear_filters_on_dir_change false

# 禁用在主栏中显示行号。
# Possible values: false, absolute, relative.
set line_numbers relative

# 当line_numbers=relative时，显示绝对行数在
# 当前行。
set relative_current_zero false

# 行数从1开始，而不是从0开始
set one_indexed true

# 退出时保存标签
set save_tabs_on_exit false

# 启用滚动包装--在最后一个项目上向下移动时，将环绕至
# 顶端，反之亦然。
set wrap_scroll false

# 将global_inode_type_filter设为空。 可能的选项：d、f和l，用于
# 分别是目录、文件和符号链接。
set global_inode_type_filter

# 这个设置允许冻结文件列表以节省I/O带宽。 它
# 在启动过程中应该是 "false"，但你可以按F键来切换它。
set freeze_files false

# 以字节为单位打印文件大小，而不是默认的人类可读格式。
set size_in_bytes false

# 如果RANGER_LEVEL环境变量大于0，在启动时发出警告，换句话说就是
# 当你在ranger启动的子壳中嵌套ranger时，会给出警告。
# 特殊值 "错误 "使警告更加明显。
set nested_ranger_warning true

# ===================================================================
# == 本地选择
# ===================================================================
# 你可以设置只影响一个目录的本地选项。

# Examples:
# setlocal path=~/downloads sort mtime

# ===================================================================
# == 控制台中的命令别名
# ===================================================================

alias e     edit
alias q     quit
alias q!    quit!
alias qa    quitall
alias qa!   quitall!
alias qall  quitall
alias qall! quitall!
alias setl  setlocal

alias filter     scout -prts
alias find       scout -aets
alias mark       scout -mr
alias unmark     scout -Mr
alias search     scout -rs
alias search_inc scout -rts
alias travel     scout -aefklst

# ===================================================================
# == 为浏览器定义按键
# ===================================================================

# 基本
map     Q quitall
map     q quit
copymap q ZZ ZQ

map R     reload_cwd
map F     set freeze_files!
map <C-r> reset
map <C-l> redraw_window
map <C-c> abort
map <esc> change_mode normal
map ~ set viewmode!

map i display_file
map <A-j> scroll_preview 1
map <A-k> scroll_preview -1
map ? help
map W display_log
map w taskview_open
map S shell $SHELL

map :  console
map ;  console
map !  console shell%space
map @  console -p6 shell  %%s
map #  console shell -p%space
map s  console shell%space
map r  chain draw_possible_programs; console open_with%space
map f  console find%space
map cd console cd%space

map <C-p> chain console; eval fm.ui.console.history_move(-1)

# 改变线路模式
map Mf linemode filename
map Mi linemode fileinfo
map Mm linemode mtime
map Mh linemode humanreadablemtime
map Mp linemode permissions
map Ms linemode sizemtime
map MH linemode sizehumanreadablemtime
map Mt linemode metatitle

# 标签/标记
map t       tag_toggle
map ut      tag_remove
map "<any>  tag_toggle tag=%any
map <Space> mark_files toggle=True
map v       mark_files all=True toggle=True
map uv      mark_files all=True val=False
map V       toggle_visual_mode
map uV      toggle_visual_mode reverse=True

# 对于怀旧的人来说："午夜指挥官 "捆绑装置
map <F1> help
map <F2> rename_append
map <F3> display_file
map <F4> edit
map <F5> copy
map <F6> cut
map <F7> console mkdir%space
map <F8> console delete
#map <F8> console trash
map <F10> exit

# 如果你使用的是Dvorak布局的键盘
map <UP>       move up=1
map <DOWN>     move down=1
map <LEFT>     move left=1
map <RIGHT>    move right=1
map <HOME>     move to=0
map <END>      move to=-1
map <PAGEDOWN> move down=1   pages=True
map <PAGEUP>   move up=1     pages=True
map <CR>       move right=1
#map <DELETE>   console delete
map <INSERT>   console touch%space

# 类似VIM
copymap <UP>       k
copymap <DOWN>     j
copymap <LEFT>     h
copymap <RIGHT>    l
copymap <HOME>     gg
copymap <END>      G
copymap <PAGEDOWN> <C-F>
copymap <PAGEUP>   <C-B>

map J  move down=0.5  pages=True
map K  move up=0.5    pages=True
copymap J <C-D>
copymap K <C-U>

# 跳来跳去
map H     history_go -1
map L     history_go 1
map ]     move_parent 1
map [     move_parent -1
map }     traverse
map {     traverse_backwards
map )     jump_non

map gh cd ~
map ge cd /etc
map gu cd /usr
map gd cd /dev
map gl cd -r .
map gL cd -r %f
map go cd /opt
map gv cd /var
map gm cd /media
map gi eval fm.cd('/run/media/' + os.getenv('USER'))
map gM cd /mnt
map gs cd /srv
map gp cd /tmp
map gr cd /
map gR eval fm.cd(ranger.RANGERDIR)
map g/ cd /
map g? cd /usr/share/doc/ranger

# 外部项目
map E  edit
map du shell -p du --max-depth=1 -h --apparent-size
map dU shell -p du --max-depth=1 -h --apparent-size | sort -rh
map yp yank path
map yd yank dir
map yn yank name
map y. yank name_without_extension

# 文件系统操作
map =  chmod

map cw console rename%space
map a  rename_append
map A  eval fm.open_console('rename ' + fm.thisfile.relative_path.replace("%", "%%"))
map I  eval fm.open_console('rename ' + fm.thisfile.relative_path.replace("%", "%%"), position=7)

map pp paste
map po paste overwrite=True
map pP paste append=True
map pO paste overwrite=True append=True
map pl paste_symlink relative=False
map pL paste_symlink relative=True
map phl paste_hardlink
map pht paste_hardlinked_subtree
map pd console paste dest=
map p`<any> paste dest=%any_path
map p'<any> paste dest=%any_path

map dD console delete
map dT console trash

map dd cut
map ud uncut
map da cut mode=add
map dr cut mode=remove
map dt cut mode=toggle

map yy copy
map uy uncut
map ya copy mode=add
map yr copy mode=remove
map yt copy mode=toggle

# 临时性的变通办法
map dgg eval fm.cut(dirarg=dict(to=0), narg=quantifier)
map dG  eval fm.cut(dirarg=dict(to=-1), narg=quantifier)
map dj  eval fm.cut(dirarg=dict(down=1), narg=quantifier)
map dk  eval fm.cut(dirarg=dict(up=1), narg=quantifier)
map ygg eval fm.copy(dirarg=dict(to=0), narg=quantifier)
map yG  eval fm.copy(dirarg=dict(to=-1), narg=quantifier)
map yj  eval fm.copy(dirarg=dict(down=1), narg=quantifier)
map yk  eval fm.copy(dirarg=dict(up=1), narg=quantifier)

# 搜索
map /  console search%space
map n  search_next
map N  search_next forward=False
map ct search_next order=tag
map cs search_next order=size
map ci search_next order=mimetype
map cc search_next order=ctime
map cm search_next order=mtime
map ca search_next order=atime

# 标签
map <C-n>     tab_new
map <C-w>     tab_close
map <TAB>     tab_move 1
map <S-TAB>   tab_move -1
map <A-Right> tab_move 1
map <A-Left>  tab_move -1
map gt        tab_move 1
map gT        tab_move -1
map gn        tab_new
map gc        tab_close
map uq        tab_restore
map <a-1>     tab_open 1
map <a-2>     tab_open 2
map <a-3>     tab_open 3
map <a-4>     tab_open 4
map <a-5>     tab_open 5
map <a-6>     tab_open 6
map <a-7>     tab_open 7
map <a-8>     tab_open 8
map <a-9>     tab_open 9
map <a-r>     tab_shift 1
map <a-l>     tab_shift -1

# 分拣
map or set sort_reverse!
map oz set sort=random
map os chain set sort=size;      set sort_reverse=False
map ob chain set sort=basename;  set sort_reverse=False
map on chain set sort=natural;   set sort_reverse=False
map om chain set sort=mtime;     set sort_reverse=False
map oc chain set sort=ctime;     set sort_reverse=False
map oa chain set sort=atime;     set sort_reverse=False
map ot chain set sort=type;      set sort_reverse=False
map oe chain set sort=extension; set sort_reverse=False

map oS chain set sort=size;      set sort_reverse=True
map oB chain set sort=basename;  set sort_reverse=True
map oN chain set sort=natural;   set sort_reverse=True
map oM chain set sort=mtime;     set sort_reverse=True
map oC chain set sort=ctime;     set sort_reverse=True
map oA chain set sort=atime;     set sort_reverse=True
map oT chain set sort=type;      set sort_reverse=True
map oE chain set sort=extension; set sort_reverse=True

map dc get_cumulative_size

# 设置
map zc    set collapse_preview!
map zd    set sort_directories_first!
map zh    set show_hidden!
map <C-h> set show_hidden!
copymap <C-h> <backspace>
copymap <backspace> <backspace2>
map zI    set flushinput!
map zi    set preview_images!
map zm    set mouse_enabled!
map zp    set preview_files!
map zP    set preview_directories!
map zs    set sort_case_insensitive!
map zu    set autoupdate_cumulative_size!
map zv    set use_preview_script!
map zf    console filter%space
copymap zf zz

# 滤波器组
map .d filter_stack add type d
map .f filter_stack add type f
map .l filter_stack add type l
map .m console filter_stack add mime%space
map .n console filter_stack add name%space
map .# console filter_stack add hash%space
map ." filter_stack add duplicate
map .' filter_stack add unique
map .| filter_stack add or
map .& filter_stack add and
map .! filter_stack add not
map .r filter_stack rotate
map .c filter_stack clear
map .* filter_stack decompose
map .p filter_stack pop
map .. filter_stack show

# 书签
map `<any>  enter_bookmark %any
map '<any>  enter_bookmark %any
map m<any>  set_bookmark %any
map um<any> unset_bookmark %any

map m<bg>   draw_bookmarks
copymap m<bg>  um<bg> `<bg> '<bg>

# 在一些python的帮助下，生成所有的chmod绑定。
eval for arg in "rwxXst": cmd("map +u{0} shell -f chmod u+{0} %s".format(arg))
eval for arg in "rwxXst": cmd("map +g{0} shell -f chmod g+{0} %s".format(arg))
eval for arg in "rwxXst": cmd("map +o{0} shell -f chmod o+{0} %s".format(arg))
eval for arg in "rwxXst": cmd("map +a{0} shell -f chmod a+{0} %s".format(arg))
eval for arg in "rwxXst": cmd("map +{0}  shell -f chmod u+{0} %s".format(arg))

eval for arg in "rwxXst": cmd("map -u{0} shell -f chmod u-{0} %s".format(arg))
eval for arg in "rwxXst": cmd("map -g{0} shell -f chmod g-{0} %s".format(arg))
eval for arg in "rwxXst": cmd("map -o{0} shell -f chmod o-{0} %s".format(arg))
eval for arg in "rwxXst": cmd("map -a{0} shell -f chmod a-{0} %s".format(arg))
eval for arg in "rwxXst": cmd("map -{0}  shell -f chmod u-{0} %s".format(arg))

# ===================================================================
# == 定义控制台的按键
# ===================================================================
# 注意：未映射的键会直接传递给控制台。

# 基本
cmap <tab>   eval fm.ui.console.tab()
cmap <s-tab> eval fm.ui.console.tab(-1)
cmap <ESC>   eval fm.ui.console.close()
cmap <CR>    eval fm.ui.console.execute()
cmap <C-l>   redraw_window

copycmap <ESC> <C-c>
copycmap <CR>  <C-j>

# 左右移动
cmap <up>    eval fm.ui.console.history_move(-1)
cmap <down>  eval fm.ui.console.history_move(1)
cmap <left>  eval fm.ui.console.move(left=1)
cmap <right> eval fm.ui.console.move(right=1)
cmap <home>  eval fm.ui.console.move(right=0, absolute=True)
cmap <end>   eval fm.ui.console.move(right=-1, absolute=True)
cmap <a-b> eval fm.ui.console.move_word(left=1)
cmap <a-f> eval fm.ui.console.move_word(right=1)

copycmap <a-b> <a-left>
copycmap <a-f> <a-right>

# 线路编辑
cmap <backspace>  eval fm.ui.console.delete(-1)
cmap <delete>     eval fm.ui.console.delete(0)
cmap <C-w>        eval fm.ui.console.delete_word()
cmap <A-d>        eval fm.ui.console.delete_word(backward=False)
cmap <C-k>        eval fm.ui.console.delete_rest(1)
cmap <C-u>        eval fm.ui.console.delete_rest(-1)
cmap <C-y>        eval fm.ui.console.paste()

# 当然还有emacs的方式
copycmap <ESC>       <C-g>
copycmap <up>        <C-p>
copycmap <down>      <C-n>
copycmap <left>      <C-b>
copycmap <right>     <C-f>
copycmap <home>      <C-a>
copycmap <end>       <C-e>
copycmap <delete>    <C-d>
copycmap <backspace> <C-h>

# 注意：有多种方法来表达退格。 <退格> (代码 263)
# 和<backspace2>（代码127）。 为确定起见，请同时使用。
copycmap <backspace> <backspace2>

# 这种特殊的表达方式允许输入数字。
cmap <allow_quantifiers> false

# ===================================================================
# == 呼叫器按键绑定
# ===================================================================

# 运动
pmap  <down>      pager_move  down=1
pmap  <up>        pager_move  up=1
pmap  <left>      pager_move  left=4
pmap  <right>     pager_move  right=4
pmap  <home>      pager_move  to=0
pmap  <end>       pager_move  to=-1
pmap  <pagedown>  pager_move  down=1.0  pages=True
pmap  <pageup>    pager_move  up=1.0    pages=True
pmap  <C-d>       pager_move  down=0.5  pages=True
pmap  <C-u>       pager_move  up=0.5    pages=True

copypmap <UP>       k  <C-p>
copypmap <DOWN>     j  <C-n> <CR>
copypmap <LEFT>     h
copypmap <RIGHT>    l
copypmap <HOME>     g
copypmap <END>      G
copypmap <C-d>      d
copypmap <C-u>      u
copypmap <PAGEDOWN> n  f  <C-F>  <Space>
copypmap <PAGEUP>   p  b  <C-B>

# 基本
pmap     <C-l> redraw_window
pmap     <ESC> pager_close
copypmap <ESC> q Q i <F3>
pmap E      edit_file

# ===================================================================
# == 任务视图绑定键
# ===================================================================

# 运动
tmap <up>        taskview_move up=1
tmap <down>      taskview_move down=1
tmap <home>      taskview_move to=0
tmap <end>       taskview_move to=-1
tmap <pagedown>  taskview_move down=1.0  pages=True
tmap <pageup>    taskview_move up=1.0    pages=True
tmap <C-d>       taskview_move down=0.5  pages=True
tmap <C-u>       taskview_move up=0.5    pages=True

copytmap <UP>       k  <C-p>
copytmap <DOWN>     j  <C-n> <CR>
copytmap <HOME>     g
copytmap <END>      G
copytmap <C-u>      u
copytmap <PAGEDOWN> n  f  <C-F>  <Space>
copytmap <PAGEUP>   p  b  <C-B>

# 改变优先级和删除任务
tmap J          eval -q fm.ui.taskview.task_move(-1)
tmap K          eval -q fm.ui.taskview.task_move(0)
tmap dd         eval -q fm.ui.taskview.task_remove()
tmap <pagedown> eval -q fm.ui.taskview.task_move(-1)
tmap <pageup>   eval -q fm.ui.taskview.task_move(0)
tmap <delete>   eval -q fm.ui.taskview.task_remove()

# 基本
tmap <C-l> redraw_window
tmap <ESC> taskview_close
copytmap <ESC> q Q w <C-c>

# 移至废纸篓
#map DD shell mv %s /home/qq/.local/share/Trash/files/
map DD shell gio trash %s

# 解压缩快捷方式
map ex extract
map ec compress
```

## command.py

```
# 这是一个commands.py的例子。 你可以在这里添加你自己的命令。
#
# 请参考 commands_full.py 以了解所有的默认命令和一个完整的
#  文件。 不要把它们都加在这里，否则你可能会得到一个失效的
# 升级游侠时的命令。

# 下面是一个用于演示的简单命令。
# -----------------------------------------------------------------------------

from __future__ import (absolute_import, division, print_function)

# 你可以根据需要导入任何python模块。
import os

# 你总是需要在这里导入ranger.api.commands来获得Command类。
from ranger.api.commands import Command


# 任何属于 "指挥 "的子类都将被整合到游侠中，成为一个
# 命令。 尝试在ranger中输入":my_edit<ENTER>"!
class my_edit(Command):
    # 类的所谓doc-string将在内置的
    # 帮助，可以通过在ranger里面输入"?c "获得。
    """:my_edit <filename>

    A sample command for demonstration purposes that opens a file in an editor.
    """

    # 当你在ranger中运行这个命令时，执行方法会被调用。
    def execute(self):
        # self.arg(1)是函数的第一个（用空格分隔的）参数。
        # 这样，你可以写":my_edit somefilename<ENTER>"。
        if self.arg(1):
            # self.rest(1)包含self.arg(1)和后面的所有内容。
            target_filename = self.rest(1)
        else:
            # self.fm是一个ranger.core.filemanager.FileManager对象，并给出了
            # 你可以接触到游侠的内部结构。
            # self.fm.thisfile是一个ranger.container.file.File对象，是一个
            # 对当前选定文件的引用。
            target_filename = self.fm.thisfile.path

        # 这是一个通用函数，用于在ranger中打印文本。
        self.fm.notify("Let's edit the file " + target_filename + "!")

        # 在fm.notify中使用bad=True允许你打印错误信息。
        if not os.path.exists(target_filename):
            self.fm.notify("The given file does not exist!", bad=True)
            return

        # 这将执行ranger.core.acitons中的一个函数，这个模块有一个
        # 各种子程序可以帮助你构建命令。
        # 请查看源代码，或者运行 "pydoc ranger.core.actions "获取列表。
        self.fm.edit_file(target_filename)

    # 当你按下tab键时，tab方法被调用，并应返回一个
    # 用户将浏览的建议。
    # tabnum对于<TAB>来说是1，对于<S-TAB>来说默认是-1
    def tab(self, tabnum):
        # 这是一个通用的标签完成函数，它通过遍历
        # 当前目录的内容。
        return self._tab_directory_content()

# 添加以下条目以清空垃圾目录  :empty
class empty(Command):
    """:empty

    Empties the trash directory ~/.Trash
    """

    def execute(self):
        self.fm.run("rm -rf /home/myname/.Trash/")
```

# ranger_devicons

`git clone https://github.com/alexanderjeurissen/ranger_devicons ~/.config/ranger/plugins/ranger_devicons`

# ranger-archives

`cd ~/.config/ranger/plugins`

`git clone https://github.com/maximtrp/ranger-archives.git`

# 触摸板

`sudo vim /etc/X11/xorg.conf.d/30-touchpad.conf`

`echo "default_linemode devicons" >> $HOME/.config/ranger/rc.conf`

```
Section "InputClass"
     Identifier "touchpad"
     Driver "libinput"
     MatchIsTouchpad "on"
     Option "Tapping" "on"
     # Option "TappingButtonMap" "lmr"

     Option "TabButton1" "1"
     Option "TabButton2" "3"
     Option "TabButton3" "2"
EndSection
```

# Vim plugin

```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

# npm 配置

`npm config set registry https://registry.npmmirror.com/`

`mkdir ~/npm`

`vim ~/.npmrc`

`prefix = ~/npm`

`vim ~/.bashrc`

`vim ~/.zshrc`

`export PATH=~/npm/bin:$PATH`

# pip 配置

`pip config set global.index-url https://mirrors.bfsu.edu.cn/pypi/web/simple`

# dunst

`mkdir ~/.config/dunst`

`vim ~/.config/dunst/dunstrc`

```
[global]
	monitor = 0
	follow = mouse
	geometry = "320x6-30+60"
	indicate_hidden = yes
	shrink = no
	notification_height = 15
	separator_height = 1
	padding = 10
	horizontal_padding = 10
	frame_width = 2
	frame_color = "#aaaaaa"
	separator_color = frame
	sort = yes
	idle_threshold = 120
	font = Noto Sans Mono SC 14
	line_height = 0
	markup = full
	format = "<span><b>%s %p</b></span>\n%b"
	alignment = left
	show_age_threshold = 60
	word_wrap = yes
	ellipsize = middle
	ignore_newline = no
	stack_duplicates = true
	hide_duplicate_count = false
	show_indicators = yes
	icon_position = left
	max_icon_size = 48
	icon_path = /usr/share/icons/Arc/status/48/:/usr/share/icons/Arc/devices/48/:/usr/share/icons/Papirus/48x48/apps/
	sticky_history = yes
	history_length = 20
	always_run_script = true
	startup_notification = false
	verbosity = mesg
	corner_radius = 5
	force_xinerama = false
	mouse_left_click = do_action
	mouse_middle_click = close_all
	mouse_right_click = close_current


[shortcuts]
	#close = ctrl+space
	#history = ctrl+shift+space
	#context = ctrl+shift+period


[urgency_low]
	# IMPORTANT: colors have to be defined in quotation marks.
	# Otherwise the '#' and following  would be interpreted as a comment.
	background="#2B2F36"
	foreground="#b6a49b"
	timeout = 5


[urgency_normal]
	background="#2B2F36"
	foreground="#b6a49b"
	timeout = 10


[urgency_critical]
	background="#2B2F36"
	foreground="#b6a49b"
	timeout = 0
```

# 最后的vim配置

```
set nocompatible " 不与 Vi 兼容
syntax on " 打开语法高亮
set encoding=utf-8 " 使用 utf-8 编码
set t_Co=256 " 启用256色
set laststatus=0 " 不显示状态栏
set showmatch " 光标遇到圆括号、方括号、大括号时，自动高亮对应的另一个圆括号、方括号和大括号
set hlsearch " 搜索时，高亮显示匹配结果
set incsearch " 输入搜索模式时，每输入一个字符，就自动跳到第一个匹配的结果
set clipboard=unnamedplus " 剪贴板
set mouse=a " 支持使用鼠标
set relativenumber " 相对行号
set cursorline " 光标所在的当前行高亮

call plug#begin()
Plug 'mhinz/vim-startify' " 启动屏幕
Plug 'vim-airline/vim-airline' " 状态行
Plug 'vim-airline/vim-airline-themes' " 状态行主题
Plug 'LunarWatcher/auto-pairs' " 自动配对
Plug 'luochen1990/rainbow' " 彩虹括号增强版
Plug 'preservim/nerdtree' " 文件系统浏览器
Plug 'tiagofumo/vim-nerdtree-syntax-highlight' " nerdtree-语法高亮
Plug 'ryanoasis/vim-devicons' " 添加图标到你的插件
Plug 'ap/vim-css-color' " 颜色名称荧光笔
call plug#end()

let g:airline#extensions#tabline#enabled = 1 " 启用状态行
let g:airline_statusline_ontop=1 " 顶部的状态行
let g:airline_powerline_fonts = 1 " 与电力线字体集成
let g:airline_theme='violet' " 状态行主题

let g:rainbow_active = 1 " 启用彩虹括号增强版

" 树的显示图标
let g:NERDTreeDirArrowExpandable = '+'
let g:NERDTreeDirArrowCollapsible = '-'

" 显示隐藏文件
let NERDTreeShowHidden=1

" 显示行号
let NERDTreeShowLineNumbers=1

" 窗口位置
let g:NERDTreeWinPos='left'

" 将F2设置为开关NERDTree的快捷键
map <F2> :NERDTreeToggle<CR>

" 窗口尺寸
let g:NERDTreeSize=30


" 使用完全匹配突出显示文件夹
let g:NERDTreeHighlightFolders = 1
let g:NERDTreeHighlightFoldersFullName = 1
```

