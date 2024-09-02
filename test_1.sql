https://github.com/netology-code/py-homeworks-db/blob/SQLPY-76/04-dml/README.md

--исполнители
INSERT INTO artist(artist_name) VALUES ('Пикник');
INSERT INTO artist(artist_name) VALUES ('Секрет');
INSERT INTO artist(artist_name) VALUES ('Максим Леонидов');
INSERT INTO artist(artist_name) VALUES ('Scorpions');

--жанры
INSERT INTO genre(genre_name) VALUES ('рок');
INSERT INTO genre(genre_name) VALUES ('хеви-метал');
INSERT INTO genre(genre_name) VALUES ('рок-н-ролл');
INSERT INTO genre(genre_name) VALUES ('бит');

--связка жанры-исполнители
INSERT INTO artist_genre VALUES (1, 1);
INSERT INTO artist_genre VALUES (1, 3);
INSERT INTO artist_genre VALUES (2, 1);
INSERT INTO artist_genre VALUES (2, 3);
INSERT INTO artist_genre VALUES (2, 4);
INSERT INTO artist_genre VALUES (3, 1);
INSERT INTO artist_genre VALUES (3, 3);
INSERT INTO artist_genre VALUES (3, 4);
INSERT INTO artist_genre VALUES (4, 2);

--альбомы
INSERT INTO album(album_name, reelease_year) VALUES ('В руках великана', 2019);
INSERT INTO album(album_name, reelease_year) VALUES ('Всё это и есть любовь', 2014);
INSERT INTO album(album_name, reelease_year) VALUES ('Седьмое небо', 2021);
INSERT INTO album(album_name, reelease_year) VALUES ('Humanity: Hour I', 2007);
INSERT INTO album(album_name, reelease_year) VALUES ('Совместный альбом', 2020);

--связка альбом-исполнитель
INSERT INTO album_artist VALUES (1,1);
INSERT INTO album_artist VALUES (2,2);
INSERT INTO album_artist VALUES (3,3);
INSERT INTO album_artist VALUES (4,4);
INSERT INTO album_artist VALUES (1,5);
INSERT INTO album_artist VALUES (3,5);

--треки
--треки альбома 'В руках великана'
INSERT INTO track(track_name, track_time, albumid) VALUES ('Счастливчик', 256, 1);
INSERT INTO track(track_name, track_time, albumid) VALUES ('В руках великана', 269, 1);
INSERT INTO track(track_name, track_time, albumid) VALUES ('Grand finale', 71, 1);
--треки альбома 'Всё это и есть любовь'
INSERT INTO track(track_name, track_time, albumid) VALUES ('Всё это и есть любовь', 217, 2);
INSERT INTO track(track_name, track_time, albumid) VALUES ('Серенада', 239, 2);
INSERT INTO track(track_name, track_time, albumid) VALUES ('Лети', 205, 2);
--треки альбома 'Седьмое небо'
INSERT INTO track(track_name, track_time, albumid) VALUES ('В твоём городе осень', 266, 3);
INSERT INTO track(track_name, track_time, albumid) VALUES ('Mon Amour', 174, 3);
--треки альбома 'Humanity: Hour I'
INSERT INTO track(track_name, track_time, albumid) VALUES ('The Game of Life', 244, 4);
INSERT INTO track(track_name, track_time, albumid) VALUES ('We Were Born to Fly', 239, 4);
INSERT INTO track(track_name, track_time, albumid) VALUES ('Humanity', 326, 4);
INSERT INTO track(track_name, track_time, albumid) VALUES ('When You Came into My Life', 284, 4);
--треки альбома 'Совместный альбом'
INSERT INTO track(track_name, track_time, albumid) VALUES ('Иероглиф (кавер)', 287, 5);
INSERT INTO track(track_name, track_time, albumid) VALUES ('Вниз по течению (кавер)', 315, 5);


--сборники
INSERT INTO mixtape(mixtape_name, release_year) VALUES ('Легенды русского рока', 2020);
INSERT INTO mixtape(mixtape_name, release_year) VALUES ('Rock Legends', 2019);
INSERT INTO mixtape(mixtape_name, release_year) VALUES ('Сборник лучших песен', 2023);
INSERT INTO mixtape(mixtape_name, release_year) VALUES ('The best of rock music', 2017);

--связка треки-сборники
INSERT INTO mixtape_track VALUES (1,2);
INSERT INTO mixtape_track vaLUES (1,4);
INSERT INTO mixtape_track VALUES (1,7);
INSERT INTO mixtape_track VALUES (2,9);
INSERT INTO mixtape_track VALUES (2,11);
INSERT INTO mixtape_track VALUES (3,2);
INSERT INTO mixtape_track VALUES (3,4);
INSERT INTO mixtape_track VALUES (3,8);
INSERT INTO mixtape_track VALUES (3,12);
INSERT INTO mixtape_track VALUES (4,11);
INSERT INTO mixtape_track VALUES (4,12);

Добрый день!
Меня очень заинтересовала Ваша вакансия инженера технической поддержки, и в качестве сопроводительного письма, хотел бы немного рассказать о себе и своих навыках.
В текущем году я окончил институт по специальности "Информатика и вычислительная техника", на данный момент работаю на оборонном предприятии на должности более близкой к "эникею", где к большому сожалению, перспективы роста отсутствуют, а также приходится иметь дело с весьма устаревшими технологиями, что сильно затрудняет собственное развитие как перспективного специалиста.
В процессе работы я взаимодействовал с NGFW, ALT Linux, Bash, VM VirtualBox, Proxmox,  настройка Mikrotik, Eltex, Zabbix.
Я постоянно стараюсь учиться и осваивать новые и новые навыки, так, в 2023 году я окончил курсы Системного администратора, приобретя крайне важный опыт использования таких технологий как Terraform, Ansible, работа с облачными серверами Яндекс.Облако, выполнив дипломный проект по развертыванию отказоустойчивой инфраструктуры сайта:
https://github.com/Adrenokrome72/alifanov-sys-diplom
Не все эти навыки в деле удалось применить, поскольку пока на моем опыте не было организаций использующих данные технологии, поэтому я очень надеюсь, что смогу использовать эти навыки у Вас!
Также в данный момент я обучаюсь на курсах fullstack разработчика на python, поскольку считаю, что уверенные знания и навыки в python крайне необходимы в том числе и devops специалисту.

Дополнительно, хотел бы рассказать о своих soft-навыках. Несколькими годами ранее я окончил также институт по специальности Юриспруденция, после чего несколько лет весьма успешно проработал по данной специальности. Я успел приобрести навыки делового общения, работы с документами, консультирования сотрудников и многое другое. Но поскольку в долгосрочной перспективе я не видел себя успешным юристом, я решил сменить деятельность и начать развиваться в IT сфере и я считаю, что наиболее полноценное развитие может быть только в крупной и разносторонней организации.
Надеюсь мое резюме сможет Вас заинтересовать.
Для дополнительной связи ТГ: @Adreno72

С уважением, Алифанов Сергей.
