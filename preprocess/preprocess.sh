# modify directory below according to your repo
GRAVEL_TEMP=/home/stuartsul/J6-Sampyo_SediNet/temp_images/gravel
SAND_TEMP=/home/stuartsul/J6-Sampyo_SediNet/temp_images/sand
IMAGES=/home/stuartsul/J6-Sampyo_SediNet/images
DATA=/home/stuartsul/J6-Sampyo_SediNet/data

[ ! -d $GRAVEL_TEMP ] && mkdir -p $GRAVEL_TEMP
[ ! -d $SAND_TEMP ] && mkdir -p $SAND_TEMP

LOCATIONS="1_풍납 2_송도 3_성수 4_서부 5_광주 6_동서울 7_화성 8_김포 9_안성 10_용인 11_인천
 12_안양 13_아산 14_청원 15_여주 16_대전 17_남부 18_오산 19_골재사업소"

for i in $LOCATIONS; do
    if [ ! -d $i ]; then
        continue
    fi

    printf "________GETTING IMAGES FROM %s________\n" $i
    case $i in
        1_강남) LOC=GN ;;
        1_풍납) LOC=PN ;;
        2_송도) LOC=SD ;;
        3_성수) LOC=SS ;;
        4_서부) LOC=SB ;;
        5_광주) LOC=GJ ;;
        6_동서울) LOC=DS ;;
        7_화성)LOC=HS ;;
        8_김포) LOC=GP ;;
        9_안성) LOC=AG ;;
        10_용인) LOC=YI ;;
        11_인천) LOC=IC ;;
        12_안양) LOC=AY ;;
        13_아산) LOC=AN ;;
        14_청원) LOC=CW ;;
        15_여주) LOC=YJ ;;
        16_대전) LOC=DJ ;;
        17_남부) LOC=NB ;;
        18_오산) LOC=OS ;;
        19_골재사업소) LOC=GJ ;;
        *) echo Wrong Location ;;
    esac

    for month in `ls ./$i/`; do
        printf "IN %s\n" $month
        `rename 's/ //g' ./$i/$month/*`;
        if [ "$1" == "gravel" ] || [ "$1" == "both" ]; then
            for folder in `find ./$i/$month/ -name '*G*' -type d`; do
                MODEL=$(echo $folder | cut -f4 -d '/');
                NAME=$(echo $MODEL | cut -f2 -d '-');
                SAMPLE=$(echo $MODEL | cut -f3 -d '-');
                printf "$folder\n"

                # SAMPLE FILE
                if [ ! -z $NAME ] && [ ! -z $SAMPLE ] && [[ $SAMPLE == "샘플"* ]]; then
                    for image in `ls $folder`; do
                        `cp $folder/$image $GRAVEL_TEMP/"RAW-$LOC-$NAME-SAMPLE.jpg"`;
                    done
                fi

                # NORMAL FILE
                if [ ! -z $NAME ] && [ -z $SAMPLE ]; then
                imageNum=1;
                for image in `ls $folder`; do
                    `cp $folder/$image $GRAVEL_TEMP/"RAW-$LOC-$NAME-$imageNum.jpg"`;
                    imageNum=$((imageNum+1));
                done
                fi
            done
        fi

        if [ "$1" == "sand" ] || [ "$1" == "both" ]; then
            for folder in `find ./$i/$month/ -name '*S*' -type d`; do
                MODEL=$(echo $folder | cut -f4 -d '/');
                NAME=$(echo $MODEL | cut -f2 -d '-');
                SAMPLE=$(echo $MODEL | cut -f3 -d '-');

                # SAMPLE FILE
                if [ ! -z $NAME ] && [ ! -z $SAMPLE ] && [ $SAMPLE == "샘플"* ]; then
                    for image in `ls $folder`; do
                        `cp $folder/$image $SAND_TEMP/"RAW-$LOC-$NAME-SAMPLE.jpg"`;
                    done
                fi

                # NORMAL FILE
                if [ ! -z $NAME ] && [ -z $SAMPLE ]; then
                imageNum=1;
                for image in `ls $folder`; do
                    `cp $folder/$image $SAND_TEMP/"RAW-$LOC-$NAME-$imageNum.jpg"`;
                    imageNum=$((imageNum+1));
                done
                fi
            done
        fi
    done
    python3 ./labeling.py $1
done

