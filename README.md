# makeAnswerSheet
組み合わせたい解答フォームの画像を含めたフォルダを作る。
(可能なフォーマットは、'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff' である。)
次に、このフォルダを「images」フォルダに入れる。
'python makeAnswerSheet.py', 'フォルダ名' の順にコマンドを実行する。
その後、解答用紙中の解答フォームにタイトルをつけるかを選び、その解答フォームの高さを100以上の整数で設定する。
すると、「as_pdf」フォルダに目的の解答用紙が作成される。
この解答用紙で良いなら'save'で終了し、フォームのレイアウトを変えたいなら'new'で上の処理に戻る。

make a folder which includes images of your answer forms.
('png', 'jpg', 'jpeg', 'gif', 'bmp', and 'tiff' are available) 
then, set the folder in the 'images' folder.
input commands, 'python makeAnswerSheet.py', 'YOUR FOLDER NAME' in this order.
afterwards, choose whether to put titles on each answer form, and set height of the forms in integer of 100 or higher.
finally, you can find a sheet of paper in the 'as_pdf' folder.
if you are satisfied with this sheet, input 'save' to terminate this program. 
if not, enter 'new', and go back to the executions upper.