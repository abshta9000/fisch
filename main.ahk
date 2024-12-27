#Requires AutoHotkey v1.1
#Include TextSearch.ahk
#SingleInstance, force


; Text:="|<>AFAFAE-0.59$83.7z0k0s0s0k1lzyTz3k1k1s1k73zxwD7U3U7k3US703U4D070DU71sC0700S0C0vUC7UQ0C00w0Q1r0QS0s0S01s0s3i0ts1k0y03k1kCC1rU3U0z07U3UQQ3j0700zkDzz0ss7z0DzUTkTzy3UsDy0Tz07ss0Q71kTC0s003ls0sDzUwS1k003nk1kzzVkQ3U003bU3Vk73UQ70007D0730670sC040CQ0CC0CC0sQ0S0ww0QQ0QQ1ss0z3ls0tk0Qs1lk0zz3U1nU0tk1nzwTs303b01n03bzw"

; if (ok:=FindText(X, Y, 1322-150000, 558-150000, 1322+150000, 558+150000, .5, .5, Text))
; {
;     MouseMove, X, Y 
;     Click
;     MsgBox, %X% %Y%
; }

CoordMode, Mouse, Screen
SysGet, Mon2, Monitor
; MsgBox, Left: %Mon2Left% -- Top: %Mon2Top% -- Right: %Mon2Right% -- Bottom %Mon2Bottom%.
MsgBox, searching
ImageSearch, OutputVarX, OutputVarY, %Mon2Left%, %Mon2Top%, %Mon2Right%, %Mon2Bottom%, C:\Users\Abishta\Documents\AutoHotkey\fisch\shake2.png
MsgBox, %OutputVarX% %OutputVarY%
if (%OutputVarX% > -1){
    MsgBox, fortni8t6yu
    MouseMove, %OutputVarX%, %OutputVarY%
}
MsgBox, dsoifhdsiofdhfoi
Exit
