#!/bin/bash
$(rm ~/excel.xls) #удаляем файл для записи результата работы скрипта
title="abs path + name\ttype\tsize(bytes)\tchanged date\tvideo or audio length (h.m.s.ms)\n"
printf "$title" >> ~/excel.xls #добавляем заголовок для таблицы
find  "$1" -type f -print0 | while IFS= read -r -d '' file; do  #находим рекурсивно все файлы, используя в качестве разделителя нулевой байт
	name=$(echo "$file" | sed 's/\.[^.]*$//') #достаем абсолютное имя
	ext=$(echo "$file" | sed 's/^.*\.//') #достаем расширение 
	size=$(stat -c '%s' "$file") #достаем размер
	date=$(stat -c '%z' "$file") #достаем дату изменения файла
	videol=$(ffprobe -i "$file" -sexagesimal -show_entries format=duration -v quiet -of csv="p=0"); #достаем видео или аудио длину файла
	if [[ $videol == "" ]]; then
		videol="0" #обнуляем длительность не видео и аудио файлов
	fi
	if [[ "$ext" == "avi" || "$ext" == "mp4" || "$ext" == "mp3" ]]; then 
		thing=$name"\t"$ext"\t"$size"\t"$date"\t"$videol"\t\n"
		printf "$thing" >> ~/excel.xls #добавляем в таблицу информацию о видео и аудио файлах
	else 
		thing=$name"\t"$ext"\t"$size"\t"$date"\t\n"
		printf "$thing" >> ~/excel.xls #добавляем в таблицу информацию об остальных файлах
	fi
done
