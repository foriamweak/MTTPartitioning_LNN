@echo off
set seqroot=C:\Sequence\
if %4 == 24 (	
	set frate=24
) else if %4 == 30 (
	set frate=32
) else if %4 == 50 (
	set frate=48
) else if %4 == 60 (
	set frate=64
)
set /a frameskip=%4 * 2
if %5 == 1 (
	if %4 == 60 (
		set /a frm=%4 * 5 - %frameskip%
	) else if %4 == 30 (
		set /a frm=%4 * 10 - %frameskip%
	) else if %4 == 50 (
		set /a frm=%4 * 6 - %frameskip%
	) 
) else (
	set /a frm=%4 * 10 - %frameskip%
)
@echo on
EncoderApp4.0_org.exe -c .\cfg\encoder_intra_vtm.cfg -c .\cfg\%1.cfg -q %3 -fs %frameskip% -f %frm% -b .\bin\%1_%3.bin -i %seqroot%%1_%2_%4.yuv >> .\dat\%1_%3.txt
del rec.yuv