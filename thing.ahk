#Requires AutoHotkey v1.1
#Include TextSearch.ahk
#SingleInstance, force

t1:=A_TickCount, Text:=X:=Y:=""

Text:="|<>0B0D1C-323232$103.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz0Ts7zzzzzzzzzzzzwTzzwTzzzzzzzzzzzlzzzznzzzzzzzzzzzbzzzzzDzzzzzzzzzzDzzzzztzzzzzzzzzzTzzzzzzDzzzzzzzzwTzzzzzzlzzzzzzzzwzzzzzzzyTzzzzzzzwzzzzzzzzbzzzzzzzxzzzzzzzzxzzzzzzzxzzzzzzzzzDzzzzzzxzzzzzzzzznzzzzzzxzzzzzzzzzwzzzzzzxzzzzzzzzzzTzzzzzxzzzzzzzzzzrzzzzzxzzzzzzzzzzxzzzzzxzzzzzzzzzzzTzzzzwzzzzzzzzzzzbzzzzyzzzzzzzzzzztzzzzyzzzzzzzzzzzyzzzzyTzzzzzzzzzzzDzzzzTzzzzzzzzzzzrzzzzTzzzzzzzzzzzxzzzzjzzzzzzzzzzzyzzzzjzzzzzzzzzzzzjzzzrzzzzzzzzzzzzrzzzrzzzzzzzzzzzzzzzzvzzzzzzzzzzzzyzzzxzzzzzzzzzzzzzTzzxzzzzzzzzzzzzzrzzyzzzzzzzzzzzzzvzzzTzzzzzzzzzzzzxzzzTzzzzzzzzzzzzzTzzjzzzzzzzzzzzzzjzzrzs7nzTnzDnU3zrzzvzlltzjszbnnzzvzzxztywzrwTnttzzxzzyzxzyTvwjttwzzyzzzzyzzDxynwtyTzzzzzTzDzbyzNyNzDzzzzzjzlznzTCz8zbzzvzzzzwDs0DbDVDk3zxzzzzzVwzrbblbtzzyzzzzzySTvnvstwzzzTzzzzzbDxs0wwyTzzjzzzzznbytySTDDzzzzzzzztnzQzjDbbzzzzzvzbxtziznbtnzzvzzxzsswzqTtnyNzzxzzyzy1yTvDyNzA0TyzzzTzzzzzzzzzzzzzTzzjzzzzzzzzzzzzzjzzrzzzzzzzzzzzzzrzzxzzzzzzzzzzzzzrzzyzzzzzzzzzzzzzvzzzTzzzzzzzzzzzzxzzzrzzzzzzzzzzzzxzzzvzzzzzzzzzzzzyzzzxzzzzzzzzzzzzzTzzzTzzzzzzzzzzzzTzzzjzzzzzzzzzzzzjzzzvzzzzzzzzzzzzbzzzxzzzzzzzzzzzzrzzzzTzzzzzzzzzzzrzzzzbzzzzzzzzzzzvzzzzvzzzzzzzzzzzvzzzzwzzzzzzzzzzztzzzzzTzzzzzzzzzzxzzzzzrzzzzzzzzzzxzzzzzxzzzzzzzzzzxzzzzzzTzzzzzzzzzwzzzzzzbzzzzzzzzzwzzzzzztzzzzzzzzzwzzzzzzyTzzzzzzzzwzzzzzzzbzzzzzzzzwzzzzzzzxzzzzzzzzwzzzzzzzzTzzzzzzzxzzzzzzzznzzzzzzztzzzzzzzzwzzzzzzztzzzzzzzzzbzzzzzznzzzzzzzzzwzzzzzzbzzzzzzzzzzbzzzzzDzzzzzzzzzzwTzzzwTzzzzzzzzzzzlzzzlzzzzzzzzzzzzz1zs7zzzzzzzzzzzzzz03zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

MsgBox, starting
If (ok:=FindText(X, Y, 513-150000, 507-150000, 513+150000, 507+150000, 0, 0,  Text, 1, 1, 0, 0, 0, 7, 1, 1)){
	Msgbox Found at original zoom
}

scale = 70
range = 200
MsgBox, staring loop
Loop, %range%
{
	; Searches for the image at incremetnal width %scale% with preserved aspect ration "h-1"
	If (ok:=FindText(X, Y, 513-150000, 507-150000, 513+150000, 507+150000, 0, 0, *w%scale% *h-1 Text, 1, 1, 0, 0, 0, 7, 1, 1))
	{
		MsgBox Found at scale level %scale%
		Break
	}  
	scale += 1
	; MsgBox, %scale%
	; OPTIONAL: Shows the image at the current zoom level in the loop, just to illustrate how the loop works.
	; SplashImage, %A_ScriptDir%/needle.png, Zw%scale% Zh-1  
	; SplashImage, off
}
MsgBox, %scale%
; ok:=FindText(X:="wait", Y:=3, 0,0,0,0,0,0,Text)    ; Wait 3 seconds for appear
; ok:=FindText(X:="wait0", Y:=-1, 0,0,0,0,0,0,Text)  ; Wait indefinitely for disappear

; MsgBox, 4096, Tip, % "Found:`t" (IsObject(ok)?ok.Length():ok)
;   . "`n`nTime:`t" (A_TickCount-t1) " ms"
;   . "`n`nPos:`t" X ", " Y
;   . "`n`nResult:`t<" (IsObject(ok)?ok[1].id:"") ">"

; Try For i,v in ok  ; ok value can be get from ok:=FindText().ok
;   if (i<=2)
;     FindText().MouseTip(ok[i].x, ok[i].y)


;==========
Exit