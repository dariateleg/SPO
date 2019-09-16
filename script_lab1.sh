#!/bin/bash
files=$(find "$1" -type f)
vals=""
dates=""
#создаем переменные для хранения длительности видео- аудиофайлов
for file in $files; do
	videol=$(ffprobe -i "$file" -sexagesimal -show_entries format=duration -v quiet -of csv="p=0"); 
	if [[ $videol == "" ]]; then
		videol="0"
	fi
	vals=$vals" "$videol;
	dates=$dates""$(stat -c %z "$file")"|";
done
#в цикле проходимся по каждому файлу из заданной директории и записываем длительность в переменную vals
find $1 -type f -exec stat -c '%n|%s' {} + |
sed 's/\./|/g' |
sed 's/,/\./g' |
awk -F "|" -v a="$vals" -v b="$dates" '
BEGIN {
split(a,list," ");
split(b,dates,"|");
print "abs path + name\ttype\tsize (bytes)\tchanged date\tvideo or audio length (h.m.s.ms)";
}
{
if ($2=="avi" || $2=="mp4" || $2=="mp3")
	print $1"\t"$2"\t"$3"\t"dates[NR]"\t"list[NR];
else
	print $1"\t"$2"\t"$3"\t"dates[NR]"\t";
}' > ~/excel.xls
#с помощью ls получаем информацию о файлах из директории, форматируем, заменяя точки на пробел 
#(для отделения нового столбца с расширениями файлов), заменяем запятые на точки, в переменную а передаем строку с длительностью, 
#форматируем строку в лист. После печатаем в конечный xls-файл заголовки для параметров и в зависимости от типа файла выводим все параметры с длительностью или без нее.

