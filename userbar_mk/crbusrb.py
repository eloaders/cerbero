#!/usr/bin/python
#python run.py "A10-4600M APU with Radeon(tm) HD Graphics 1400 MHz" "Gallium 0.4 on AMD ARUBA" "LENOVO ThinkPad Edge E535" "Ubuntu 14.04 Unity 7.1.2" /home/michal/Pulpit/simple.png
import argparse
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
parser = argparse.ArgumentParser(description='Cerbero Userbar Creator',epilog="Cerbero component for creating userbars for forums and blogs.")
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-c','--cpu', help='CPU Name',required=True)
parser.add_argument('-g','--opengl', help='OpenGL',required=True)
parser.add_argument('-m','--mobo', help='Motherboard',required=True)
parser.add_argument('-d','--dist', help='Distribution',required=True)
parser.add_argument('-k','--kernel', help='Kernel',required=True)
parser.add_argument('-o','--output', help='Output file name',required=True)
args = parser.parse_args()

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",9)

cputext = "CPU: %s" % args.cpu
gputext = "OpenGL: %s" % args.opengl
mobo_text = "Mobo: %s" % args.mobo
distro_text = "Dist: %s" % args.dist
kerneltext = "Kernel: %s" % args.kernel
cpu_pos = (5,5)
gpu_pos = (5,14)
mobo_pos = (5,24)
distro_pos = (5,33)
kernel_pos = (5,42)
tcolor = (255,255,0,255)

img = Image.open(args.input)
draw = ImageDraw.Draw(img)

draw.text(cpu_pos, cputext, fill=tcolor, font=font)
draw.text(gpu_pos, gputext, fill=tcolor, font=font)
draw.text(mobo_pos, mobo_text, fill=tcolor, font=font)
draw.text(distro_pos, distro_text, fill=tcolor, font=font)
draw.text(kernel_pos, kerneltext, fill=tcolor, font=font)
del draw

img.save(args.output)
