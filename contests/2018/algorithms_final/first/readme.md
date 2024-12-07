<h1 text-align="center">Это первая задача Алгоритмов 2018 Финал</h1>

<details>
    <summary>Условия задачи (<a href="https://contest.yandex.ru/algorithm2018/contest/8254/problems/?success=129248266#23/2018_05_20/Z7QiHJ33Bv">ссылка на ресурс</a>)</summary>
<div>В этот жаркий Санкт-Петербургский полдень стажёр Яндекса Аркадий сидел в офисе и вносил последние правки в свою дипломную работу. После нескольких часов тяжких трудов он решил развеяться и прогуляться до торгового автомата на первом этаже, чтобы купить бутылку своего любимого напитка Квас-Класс.

Стоит отметить, что в офисе установлен довольно необычный торговый автомат. Он принимает только монеты достоинством один рубль и купюры достоинством один миллион рублей, и при этом продаёт только бутылки напитка Квас-Класс ценой r рублей за штуку. Изначально у Аркадия есть b банкнот достоинством миллион рублей и c монет по одному рублю. В автомате изначально находятся d рублёвых монет, которыми он может давать сдачу. Процесс покупки одной бутылки напитка устроен следующим образом.
    
 Аркадий вставляет в автомат x банкнот и y монет, то есть общая загруженная сумма составляет z = 106 ⋅ x + y.
    Затем он нажимает на кнопку совершения покупки. Если z оказывается меньше r, то автомат просит внести ещё денег.
    Если z больше либо равно r, то автомат пытается выдать Аркадию сдачу. Поскольку автомат может выдавать сдачу только монетами, то количество находящихся в нём монет в один рубль (при этом не учитываются монеты, вставленные для совершения именно этой покупки) должно быть не менее z - r. Если монет для выдачи сдачи недостаточно, то покупка не состоится.
    Если z ≥ r и в автомате достаточно монет для того, чтобы выдать Аркадию сдачу (или сдача вообще не требуется, то есть z = r), происходит покупка. Автомат забирает себе x банкнот и y монет (которые могут быть использованы для выдачи сдачи при следующих покупках), после чего возвращает Аркадию z - r монет и выдаёт бутылку желанного напитка.

Хотя Аркадий пришёл купить только одну бутылку, он всё же программист, так что ему интересно, какое максимально количество бутылок он смог бы приобрести, если бы действовал оптимально? Можете считать, что в автомат загружено заведомо достаточное количество бутылок напитка Квас-Класс (что, к сожалению, далеко не всегда выполнено в реальной жизни).
Формат ввода

В первой строке входных данных записаны два целых числа b и c (0 ≤ b, c ≤ 10^9) — количество банкнот достоинством в один миллион рублей и количество монет в один рубль в распоряжении Аркадия.

Во второй строке записаны два целых числа r и d (1 ≤ r ≤ 10^9, 0 ≤ d ≤ 10^9) — цена одной бутылки напитка Квас-Класс и количество монет в торговом автомате до покупок Аркадия. Обратите внимание, что количество купюр внутри автомата значения не имеет.
Формат вывода

Выведите одно целое число равное максимальному количеству бутылок напитка Квас-Класс, которые Аркадий сможет купить если будет действовать оптимально.
</div>

</details>

<details>
    <summary>Решение (<a href="https://codeforces.com/blog/entry/59730">ссылка на решение</a>)</summary>
    <div>Автор идеи и разработчик: GlebsHP.

Заметим, что в любом случае Аркадий не может потратить больше денег, чем у него есть, поэтому количество купленных бутылок не превзойдёт . Однако, может так получится, что Аркадию придётся купить меньше бутылок, если в какой-то момент у Аркадия не будет хватать мелочи на покупку без сдачи, а нужно количество сдачи в автомате не будет.

Заметим, что суммарное количество мелочи в обороте не меняется и составляет c + d. При этом, если c + d ≥ 999 999, то либо у Аркадия всегда найдётся мелочь, чтобы купить очередную бутылку, либо автомат сможет дать сдачу, если платить только с помощью банкнот. В этом случае ответ равен z.

Если же c + d < 999 999, то может быть, что у Аркадия хватает мелочи для совершения покупки без сдачи, может быть, что в автомате достаточно сдачи для покупки банкнотами, но не может быть одновременно выполнено и то и другое, а значит, действия Аркадия определяются однозначно. В этом случае можно было бы промоделировать его действия, однако, их может оказаться слишком много.

Обозначим через ai количество монет у Аркадия после первых i действий (то есть a0 = c). Заметим, что если ai = aj, то ai + 1 = aj + 1 (действительно, следующее действие однозначно определяется величиной ai), а значит последовательность зацикливается и повторяется. Будем моделировать действия Аркадия по покупке бутылок напитка Квас-Класс, до тех пор пока какое-то из значений ai не повторится, либо не возникнет ситуация, когда Аркадий не может совершить следующую покупку. В случае повторения значения ai в качестве ответа выведем величину z, в противном случае номер итерации, на котором не получилось совершить очередную покупку.
</div>    
</details>


<details>
    <summary>Комментарии к коду</summary>
    <div>Решение не проходит 10 тест</div>
</details>