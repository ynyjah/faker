from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = ("{{last_name}}{{first_name}}", )
    formats_male = ["{{last_name_male}}{{first_name_male}}"]
    formats_female = ["{{last_name_female}}{{first_name_female}}"]

    first_names_female = (
        '雅萍', '惠雯', '嘉玲', '雅文', '詩婷', '欣怡', '怡萱', '美玲', '淑玲', '怡伶',
        '淑芬', '惠如', '思穎', '怡如', '筱涵', '雅琪', '怡安', '佳玲', '心怡', '宜君',
        '淑娟', '淑貞', '郁雯', '佩珊', '靜怡', '雅涵', '怡君', '靜宜', '雅玲', '依婷',
        '詩涵', '佩君', '婷婷', '淑惠', '佳蓉', '瑋婷', '佳穎', '怡婷', '鈺婷', '雅筑',
        '淑華', '雅雯', '佳慧', '雅慧', '慧君', '雅惠', '婉婷', '琬婷', '雅芳', '郁婷',
        '淑慧', '雅婷', '宜庭', '家瑜', '惠婷', '美琪',
    )

    first_names_male = (
        '宇軒', '庭瑋', '志偉', '冠廷', '彥廷', '哲瑋', '佳樺', '志豪', '威廷', '俊賢',
        '志宏', '家豪', '俊傑', '承翰', '俊宏', '馨儀', '柏翰', '信宏', '建宏', '冠宇',
        '家瑋', '家銘', '冠霖', '宗翰', '沖', '懿', '羽', '龍', '中山', '飛', '傑克',
    )

    first_names = first_names_male + first_names_female

    # From https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E5%A7%93%E6%B0%8F%E6%8E%92%E5%90%8D
    last_names = OrderedDict((
        ('王', 7.170),
        ('李', 7.000),
        ('張', 6.740),
        ('劉', 5.100),
        ('陳', 4.610),
        ('楊', 3.220),
        ('黃', 2.450),
        ('吳', 2.000),
        ('趙', 2.000),
        ('周', 1.900),
        ('徐', 1.450),
        ('孫', 1.380),
        ('馬', 1.290),
        ('朱', 1.280),
        ('胡', 1.160),
        ('林', 1.130),
        ('郭', 1.130),
        ('何', 1.060),
        ('高', 1.000),
        ('羅', 0.950),
        ('鄭', 0.930),
        ('梁', 0.850),
        ('謝', 0.760),
        ('宋', 0.700),
        ('唐', 0.690),
        ('許', 0.660),
        ('鄧', 0.620),
        ('馮', 0.620),
        ('韓', 0.610),
        ('曹', 0.600),
        ('曾', 0.580),
        ('彭', 0.580),
        ('蕭', 0.560),
        ('蔡', 0.530),
        ('潘', 0.520),
        ('田', 0.520),
        ('董', 0.510),
        ('袁', 0.500),
        ('於', 0.480),
        ('余', 0.480),
        ('葉', 0.480),
        ('蔣', 0.480),
        ('杜', 0.470),
        ('蘇', 0.460),
        ('魏', 0.450),
        ('程', 0.450),
        ('呂', 0.450),
        ('丁', 0.430),
        ('沈', 0.410),
        ('任', 0.410),
        ('姚', 0.400),
        ('盧', 0.400),
        ('傅', 0.400),
        ('鐘', 0.400),
        ('姜', 0.390),
        ('崔', 0.380),
        ('譚', 0.380),
        ('廖', 0.370),
        ('範', 0.360),
        ('汪', 0.360),
        ('陸', 0.360),
        ('金', 0.350),
        ('石', 0.340),
        ('戴', 0.340),
        ('賈', 0.330),
        ('韋', 0.320),
        ('夏', 0.320),
        ('邱', 0.320),
        ('方', 0.310),
        ('侯', 0.300),
        ('鄒', 0.300),
        ('熊', 0.290),
        ('孟', 0.290),
        ('秦', 0.290),
        ('白', 0.280),
        ('江', 0.280),
        ('閻', 0.270),
        ('薛', 0.260),
        ('尹', 0.260),
        ('段', 0.240),
        ('雷', 0.240),
        ('黎', 0.220),
        ('史', 0.210),
        ('龍', 0.210),
        ('陶', 0.210),
        ('賀', 0.210),
        ('顧', 0.200),
        ('毛', 0.200),
        ('郝', 0.200),
        ('龔', 0.200),
        ('邵', 0.200),
        ('萬', 0.190),
        ('錢', 0.190),
        ('嚴', 0.190),
        ('賴', 0.180),
        ('覃', 0.180),
        ('洪', 0.180),
        ('武', 0.180),
        ('莫', 0.180),
        ('孔', 0.170),
        ('湯', 0.170),
        ('向', 0.170),
        ('常', 0.160),
        ('溫', 0.160),
        ('康', 0.160),
        ('施', 0.150),
        ('文', 0.150),
        ('牛', 0.150),
        ('樊', 0.150),
        ('葛', 0.150),
        ('邢', 0.140),
        ('安', 0.130),
        ('齊', 0.130),
        ('易', 0.130),
        ('喬', 0.130),
        ('伍', 0.130),
        ('龐', 0.130),
        ('顏', 0.120),
        ('倪', 0.120),
        ('莊', 0.120),
        ('聶', 0.120),
        ('章', 0.120),
        ('魯', 0.110),
        ('嶽', 0.110),
        ('翟', 0.110),
        ('殷', 0.110),
        ('詹', 0.110),
        ('申', 0.110),
        ('歐', 0.110),
        ('耿', 0.110),
        ('關', 0.100),
        ('蘭', 0.100),
        ('焦', 0.100),
        ('俞', 0.100),
        ('左', 0.100),
        ('柳', 0.100),
        ('甘', 0.095),
        ('祝', 0.090),
        ('包', 0.087),
        ('寧', 0.083),
        ('尚', 0.082),
        ('符', 0.082),
        ('舒', 0.082),
        ('阮', 0.082),
        ('柯', 0.080),
        ('紀', 0.080),
        ('梅', 0.079),
        ('童', 0.079),
        ('淩', 0.078),
        ('畢', 0.078),
        ('單', 0.076),
        ('季', 0.076),
        ('裴', 0.076),
        ('霍', 0.075),
        ('塗', 0.075),
        ('成', 0.075),
        ('苗', 0.075),
        ('谷', 0.075),
        ('盛', 0.074),
        ('曲', 0.074),
        ('翁', 0.073),
        ('冉', 0.073),
        ('駱', 0.073),
        ('藍', 0.072),
        ('路', 0.072),
        ('遊', 0.071),
        ('辛', 0.070),
        ('靳', 0.069),
        ('歐陽', 0.068),
        ('管', 0.065),
        ('柴', 0.065),
        ('蒙', 0.062),
        ('鮑', 0.062),
        ('華', 0.061),
        ('喻', 0.061),
        ('祁', 0.061),
        ('蒲', 0.056),
        ('房', 0.056),
        ('滕', 0.055),
        ('屈', 0.055),
        ('饒', 0.055),
        ('解', 0.053),
        ('牟', 0.053),
        ('艾', 0.052),
        ('尤', 0.052),
        ('陽', 0.050),
        ('時', 0.050),
        ('穆', 0.048),
        ('農', 0.047),
        ('司', 0.044),
        ('卓', 0.043),
        ('古', 0.043),
        ('吉', 0.043),
        ('繆', 0.043),
        ('簡', 0.043),
        ('車', 0.043),
        ('項', 0.043),
        ('連', 0.043),
        ('蘆', 0.042),
        ('麥', 0.041),
        ('褚', 0.041),
        ('婁', 0.040),
        ('竇', 0.040),
        ('戚', 0.040),
        ('岑', 0.039),
        ('景', 0.039),
        ('黨', 0.039),
        ('宮', 0.039),
        ('費', 0.039),
        ('蔔', 0.038),
        ('冷', 0.038),
        ('晏', 0.038),
        ('席', 0.036),
        ('衛', 0.036),
        ('米', 0.035),
        ('柏', 0.035),
        ('宗', 0.034),
        ('瞿', 0.033),
        ('桂', 0.033),
        ('全', 0.033),
        ('佟', 0.033),
        ('應', 0.033),
        ('臧', 0.032),
        ('閔', 0.032),
        ('茍', 0.032),
        ('鄔', 0.032),
        ('邊', 0.032),
        ('卞', 0.032),
        ('姬', 0.032),
        ('師', 0.031),
        ('和', 0.031),
        ('仇', 0.030),
        ('欒', 0.030),
        ('隋', 0.030),
        ('商', 0.030),
        ('刁', 0.030),
        ('沙', 0.030),
        ('榮', 0.029),
        ('巫', 0.029),
        ('寇', 0.029),
        ('桑', 0.028),
        ('郎', 0.028),
        ('甄', 0.027),
        ('叢', 0.027),
        ('仲', 0.027),
        ('虞', 0.026),
        ('敖', 0.026),
        ('鞏', 0.026),
        ('明', 0.026),
        ('佘', 0.025),
        ('池', 0.025),
        ('查', 0.025),
        ('麻', 0.025),
        ('苑', 0.025),
        ('遲', 0.024),
        ('鄺', 0.024),
        ('官', 0.023),
        ('封', 0.023),
        ('談', 0.023),
        ('匡', 0.023),
        ('鞠', 0.230),
        ('惠', 0.022),
        ('荊', 0.022),
        ('樂', 0.022),
        ('冀', 0.021),
        ('郁', 0.021),
        ('胥', 0.021),
        ('南', 0.021),
        ('班', 0.021),
        ('儲', 0.021),
        ('原', 0.020),
        ('栗', 0.020),
        ('燕', 0.020),
        ('楚', 0.020),
        ('鄢', 0.020),
        ('勞', 0.019),
        ('諶', 0.019),
        ('奚', 0.017),
        ('皮', 0.017),
        ('粟', 0.017),
        ('冼', 0.017),
        ('藺', 0.017),
        ('樓', 0.017),
        ('盤', 0.017),
        ('滿', 0.016),
        ('聞', 0.016),
        ('位', 0.016),
        ('厲', 0.016),
        ('伊', 0.016),
        ('仝', 0.015),
        ('區', 0.015),
        ('郜', 0.015),
        ('海', 0.015),
        ('闞', 0.015),
        ('花', 0.015),
        ('權', 0.014),
        ('強', 0.014),
        ('帥', 0.014),
        ('屠', 0.014),
        ('豆', 0.014),
        ('樸', 0.014),
        ('蓋', 0.014),
        ('練', 0.014),
        ('廉', 0.014),
        ('禹', 0.014),
        ('井', 0.013),
        ('祖', 0.013),
        ('漆', 0.013),
        ('巴', 0.013),
        ('豐', 0.013),
        ('支', 0.013),
        ('卿', 0.013),
        ('國', 0.013),
        ('狄', 0.013),
        ('平', 0.013),
        ('計', 0.012),
        ('索', 0.012),
        ('宣', 0.012),
        ('晉', 0.012),
        ('相', 0.012),
        ('初', 0.012),
        ('門', 0.012),
        ('雲', 0.012),
        ('容', 0.012),
        ('敬', 0.011),
        ('來', 0.011),
        ('扈', 0.011),
        ('晁', 0.011),
        ('芮', 0.011),
        ('都', 0.011),
        ('普', 0.011),
        ('闕', 0.011),
        ('浦', 0.011),
        ('戈', 0.011),
        ('伏', 0.011),
        ('鹿', 0.011),
        ('薄', 0.011),
        ('邸', 0.011),
        ('雍', 0.010),
        ('辜', 0.010),
        ('羊', 0.010),
        ('阿', 0.010),
        ('烏', 0.010),
        ('母', 0.010),
        ('裘', 0.010),
        ('亓', 0.010),
        ('修', 0.010),
        ('邰', 0.010),
        ('赫', 0.010),
        ('杭', 0.010),
        ('況', 0.0094),
        ('那', 0.0093),
        ('宿', 0.0093),
        ('鮮', 0.0092),
        ('印', 0.0091),
        ('逯', 0.0091),
        ('隆', 0.0090),
        ('茹', 0.0090),
        ('諸', 0.0089),
        ('戰', 0.0088),
        ('慕', 0.0086),
        ('危', 0.0084),
        ('玉', 0.0084),
        ('銀', 0.0084),
        ('亢', 0.0083),
        ('嵇', 0.0082),
        ('公', 0.0082),
        ('哈', 0.0081),
        ('湛', 0.0079),
        ('賓', 0.0077),
        ('戎', 0.0076),
        ('勾', 0.0076),
        ('茅', 0.0076),
        ('利', 0.0076),
        ('於', 0.0074),
        ('呼', 0.0074),
        ('居', 0.0074),
        ('揭', 0.0073),
        ('幹', 0.0072),
        ('但', 0.0072),
        ('尉', 0.0071),
        ('冶', 0.0071),
        ('斯', 0.0070),
        ('元', 0.0069),
        ('束', 0.0068),
        ('檀', 0.0068),
        ('衣', 0.0067),
        ('信', 0.0067),
        ('展', 0.0067),
        ('陰', 0.0067),
        ('昝', 0.0066),
        ('智', 0.0065),
        ('幸', 0.0065),
        ('奉', 0.0064),
        ('植', 0.0064),
        ('衡', 0.0063),
        ('富', 0.0063),
        ('堯', 0.0060),
        ('閉', 0.0060),
        ('由', 0.0060),
    ))

    romanized_formats = (
        '{{first_romanized_name}} {{last_romanized_name}}',
    )

    # From https://en.wikipedia.org/wiki/Chinese_given_name#Common_Chinese_names,
    # with accents stripped
    first_romanized_names = (
        'Chao',
        'Fang',
        'Gang',
        'Guiying',
        'Jie',
        'Jing',
        'Juan',
        'Jun',
        'Lei',
        'Li',
        'Min',
        'Ming',
        'Na',
        'Ping',
        'Qiang',
        'Tao',
        'Wei',
        'Xia',
        'Xiulan',
        'Xiuying',
        'Yang',
        'Yong',
        'Yan',
    )

    # From https://en.wikipedia.org/wiki/List_of_common_Chinese_surnames
    # with accents stripped
    last_romanized_names = (
        'Bai', 'Cai', 'Cao', 'Chang', 'Chen', 'Cheng', 'Cui', 'Dai', 'Deng',
        'Ding', 'Dong', 'Du', 'Duan', 'Fan', 'Fang', 'Feng', 'Fu', 'Gao', 'Gong',
        'Gu', 'Guo', 'Han', 'Hao', 'He', 'Hou', 'Hu', 'Huang', 'Jia', 'Jiang',
        'Jin', 'Kang', 'Kong', 'Lai', 'Lei', 'Li', 'Liang', 'Liao', 'Lin', 'Liu',
        'Long', 'Lu', 'Luo', 'Ma', 'Mao', 'Meng', 'Mo', 'Pan', 'Peng', 'Qian',
        'Qiao', 'Qin', 'Qiu', 'Ren', 'Shao', 'Shen', 'Shi', 'Song', 'Su', 'Sun',
        'Tan', 'Tang', 'Tao', 'Tian', 'Wan', 'Wang', 'Wei', 'Wen', 'Wu', 'Xia',
        'Xiang', 'Xiao', 'Xie', 'Xiong', 'Xu', 'Xue', 'Yan', 'Yang', 'Yao', 'Ye',
        'Yi', 'Yin', 'Yu', 'Yuan', 'Zeng', 'Zhang', 'Zhao', 'Zheng', 'Zhong',
        'Zhou', 'Zhu', 'Zou',
    )

    def romanized_name(self):
        '''
        @example 'Chao Bai'
        '''
        pattern = self.random_element(self.romanized_formats)
        return self.generator.parse(pattern)

    def first_romanized_name(self):
        '''
        @example 'Chao'
        '''
        return self.random_element(self.first_romanized_names)

    def last_romanized_name(self):
        '''
        @example 'Chao'
        '''
        return self.random_element(self.last_romanized_names)
