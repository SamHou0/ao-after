﻿# 游戏的脚本可置于此文件中。
style red_highlight:
    color "ff8081"
    size 45
# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

layeredimage bs:
    offset (0,-300)
    always:
        "images/in chr/bs1_in010101.jpg"

    group face:
        offset(33.5,91)
        attribute happy:
            "images/in chr/bs1_in_f01_02.jpg"
layeredimage ao:
    offset(90,150)
    group outfit:
        attribute stu_stand:
            offset(-226,-122)
            "images/ao chr/bs2_ao011101.jpg"
        attribute com_stand:
            offset(-222,-126)
            "images/ao chr/bs2_ao021101.jpg"
        attribute jap_stand:
            offset(-250,-121)
            "images/ao chr/bs2_ao031101.jpg"
    group face:
        attribute eye_closed_smile:
            "images/ao chr/bs2_ao_f11_08.jpg"
        attribute com:
            "images/ao chr/bs2_ao_f11_12.jpg"
        attribute eye_closed:
            "images/ao chr/bs2_ao_f11_15.jpg"
        attribute eye_closed_feeling:
            "images/ao chr/bs2_ao_f11_11.jpg"
        attribute what_can_i_say:
            "images/ao chr/bs2_ao_f11_18.jpg"
        attribute eye_closed_feel_bad:
            "images/ao chr/bs2_ao_f11_15.jpg"
        attribute smile:
            "images/ao chr/bs2_ao_f11_19.jpg"
        attribute earnest:
            "images/ao chr/bs2_ao_f11_05.jpg"
# 游戏在此开始。

label start:
    $ ending=0
    play music "bgm/bgm01.ogg"
    scene bg001a1 with fade
    "鸟白岛上，有一种独特的祭祀，山之祭祀。"
    scene bg011n with fade 
    "祭祀的主持者需要手持灯笼，在山中漫步。"
    "当然，那些东西只是一种习惯罢了，是古代科学尚未发展时人们的幻想。"
    "毕竟在这个科学主导的世界上，怎么可能存在什么超自然现象呢？"
    "……开玩笑的。"
    "这个夏天，我和一个名叫苍的少女相识，相爱，共同度过了一段无可替代的时光。"
    "我也明白了，风俗什么的，只是一个用以转移注意力的借口罢了。"
    "山之祭祀绝不仅仅是那种老祖宗留下来的传说而已。"
    "那些发光的神秘蝴蝶，叫七影蝶，是这个小岛上人们魂魄的化身，拥有能够通过接触传递记忆的强大力量。"
    "而山之祭祀，则是将迷失的愿望引导回它们所应该回到的地方去。"
    stop music fadeout 2.0
    show bs happy with dissolve
    "稻荷" "嘣！"
    "蓝色小狐狸的叫声将我拉回了现实。"
    "这个名叫稻荷的生物，似乎能够听懂人们的对话。"
    show bs happy with ease:
        xoffset -300
    show ao com_stand eye_closed with dissolve:
        xalign 0.8
    "我背上的这个叫苍的少女，正安心地睡着。"
    "然而，我却不仅要忍受背上的重量，还要和困意做斗争。"
    "由于刚刚摸过苍的七影蝶，大脑需要休息来整理刚刚传来的信息。"
    scene bg_kuro with fade
    "双脚似乎自动往前走着。"
    "脑中浮现出一幕幕……"
    scene bg001a1 with fade
    play music "bgm/bgm04.ogg" fadein 1.2
    "是这个夏天发生的事情。"
    "我为了整理祖母的遗物，来到了这座叫做鸟白岛的岛上，和苍在树下相遇了。"
    scene bg019n1 with fade
    "在某次睡觉前，山上的一点亮光吸引了我的注意力。"
    scene bg011n with fade
    show ao jap_stand eye_closed with dissolve
    "怀着好奇心来到山上，发现穿着巫女服的苍正在触碰发光蝴蝶。"
    scene cg_ao03_0203 with fade
    "通过仓库里的古书，我明白了这些蝴蝶叫七影碟，是人死后魂魄化身的蝴蝶，向活着的人传递着思念之情。"
    "由于想要见苍，意外之下，我自己也在夜晚的山中触摸了这种蝴蝶。"
    scene bg011n1 with fade
    "……却被其中传来的记忆所控制，在不自知的情况下缓缓移动到了悬崖边。"
    "危急时刻，苍把我从悬崖边救了下来。"
    show ao jap_stand earnest with dissolve
    "而苍也没有隐瞒，告诉了我山之祭祀和七影蝶的真相。"
    "这个小岛，是记忆回归的地方。"
    "具有强烈迷恋和后悔的人类的记忆，回到了岛上。"
    "山之祭，就是将不能留在世上的七影碟引导回应该归去的地方的一种祭祀。"
    "而之所以她打破禁忌，不断触摸蝴蝶，是为了找到一个重要的记忆。"
    scene cg_ao04_0101 with fade
    "那是她的姐姐，蓝的记忆。"
    "为了拯救摔下悬崖而沉睡的姐姐，她必须检查所有七影蝶的记忆，试图找回蓝的记忆，并送回蓝的体内。"
    "而我祖母的遗物中，就有一本书，记载着将七影蝶中蕴含的记忆送回体内的方法。"
    scene cg_ao09_0102 with fade
    "在我的陪伴和苍的努力下，蓝找回了记忆，但触摸太多七影蝶的苍却随之陷入沉睡……"
    scene cg_ao11_0101 with fade
    "最后，包含着记忆的七影蝶从她体内涌出，而她自己的那只七影蝶也飞向天空，近在咫尺，却又遥不可及。"
    "因此，我下定决心，要找回苍的记忆，正如苍找回蓝的记忆一样。"
    stop music fadeout 2.0
    scene bg_kuro with fade
    "……一阵疼痛传来。"
    scene bg011n
    "稻荷" "嘣！！！嘣！！！"
    "狐狸牙齿带来的疼痛和焦急的叫声，让我的意识回到了现实。"
    "原来，不知不觉地，我已经睡着了啊。"
    "羽依里" "谢谢你，稻荷。"
    "下山的路，只剩一点点了。"
    "再坚持一下吧。"
    "……"
    scene bg_kuro with fade
    "我缓缓拉开了病房的房门。"
    scene cg_ao09_0201 with fade
    "背上的苍仍然在熟睡着。我把她放到床上，盖好被子。"
    "羽依里" "……"
    "蓝" "……"
    "一阵沉默。"
    play music "bgm/bgm20.ogg" fadein 2.0
    "不知为何，我又把苍带到了迷途橘上。"
    "或许是内心还抱着一些希望吧。"
    "一旁熟睡的苍正发出着均匀的呼吸声。"
    "苍" "唔唔，羽依里，不要走……想……在一起……嗯嗯……"
    "羽依里" "知道了啦……"
    "羽依里" "果然，只能用那个方法了。"
    "蓝" "该不会是那个方法吧。"
    "羽依里" "没错，就是那个。"
    "我要追随苍的脚步，去完成属于我的使命。"
    "蓝" "……明年？"
    "羽依里" "无论多少年，我也要找到。苍找到你的七影蝶花了10年……即使需要花20年，甚至一辈子，我会永远找下去。"
    "唤醒苍，可是我的职责啊。"
    "在苍的七影蝶飞走之后，我已经下定了决心。"
    "蓝" "虽然我也想看到苍露出笑容的样子，但这可是10年啊……为了一个不是自己亲人的人，值得吗？"
    "羽依里" "苍是我最重要的人。况且，苍已经算是我的亲人了。"
    "蓝" "那我也去。不管10年，还是20年……"
    "面前的蓝脸上充满了坚定。"
    "是想要报答苍吗？还是空门家的职责所在？又或者……是想要陪在我的身边？"
    "……对于一个妹控，和夺走自己妹妹的人整天呆在一起这种可能性根本不存在吧。"
    "羽依里" "你不是看不见七影蝶吗？"
    "蓝" "不，我想陪你找……直到苍醒来的那一天。"
    "陪着我？"
    "蓝" "空门家的职责，还记得吗？既然苍不在，那么我来替代她吧。"
    stop music fadeout 0.5
    play music "bgm/bgm12.ogg" fadein 2.0
    "蓝" "不过，有一件事情，我想问一下。"
    "羽依里" "什么事情？"
    "蓝" "你和苍，那个……是不是已经做过那种事情了？"
    "蓝" "她最近的梦话，越来越……怎么说呢？"
    "蓝的脸已经通红了。"
    "羽依里" "等等……那个真的只是……梦话……而已。"
    "看来，可能要瞒不住了。那天晚上，在亲吻之后，在山上的树林里……"
    "苍" "羽依里……请……温柔一点……嗯嗯……"
    "这个梦话可真是不妙啊。现在轮到我解释，不，“掩饰”了吗？"
    menu:
        "转移话题":
            jump ch0_1_c1
        "老实承认":
            jump ch0_1_c2
label ch0_1_c1:
    "暂且找个其他话题吧？"
    "羽依里" "话说，如果我和苍结婚的话，就要叫空门羽依里了吧？还是叫鹰原苍好呢？果然还是把空门的姓氏传递下去好……"
    "蓝" "……果然做过了呢。都想着结婚以后的事情了。"
    "这根本不能叫转移话题吧！？"
    "羽依里！该好好锻炼一下转移话题的技术了！"
    stop music fadeout 1.0
    jump ch0_2
label ch0_1_c2:
    play music "bgm/bgm36.ogg" fadein 2.0
    "羽依里" "嗯……好吧，虽然有点说不出口，不过确……确实……做过了。"
    "说这话时整个人都在颤抖。"
    "蓝" "你还挺诚实啊。是不是想很快生出小宝宝啊？"
    "羽依里" "……"
    "现在已经不止是我和苍间的秘密了。"
    stop music fadeout 1.0
    jump ch0_2
label ch0_2:
    
    "蓝露出了可怕的脸色。"
    "羽依里" "那个，不是，嗯，啊……对不起！今天已经很晚了我明天再来吧啊啊啊"
    scene bg009n with fade
    play music "bgm/bgm11.ogg" fadein 1.0
    "我一溜烟跑出了蓝和苍的病房。"
    "鸟白岛熟悉的乡间小路。"
    "是什么时候变得如此熟悉的呢？"
    "回望这个夏天，和苍一起度过的时光。"
    "树下沉睡的少女，粗点心店的打工，海边的相遇……"
    "不知是不是触碰苍的七影蝶的效果，我的记忆格外清晰。"
    "羽依里" "苍，这个夏天我过得，真的很开心。"
    "今天就是8月28日了啊。"
    "后天早上，我就必须离开鸟白岛了。"
    "在接近假期尾声的这个深夜里，要做点什么呢？"
    menu:
        "什么都不做":
            jump ch0_2_c1
        "去迷途橘看看":
            jump ch0_2_c2
label ch0_2_c1:
    "还是睡觉吧。"
    scene bg019n1 with fade
    "回到家里的时候，海己和镜子阿姨看起来都已经睡了。"
    scene bg019n3 with dissolve
    "那么我也去睡觉吧。"
    $ ending=1
    jump ch0_3

label ch0_2_c2:
    scene bg011n with fade
    "夜晚的山路还是那么熟悉。"
    "在稻荷的带领下，一路上没有遇到七影蝶。"
    scene bg202n1 with fade
    "迷途橘上盘旋的七影蝶早已不见，花自然也是凋谢的。"
    "挂在树边的灯笼，静静地等待着山之祭祀的到来。"
    "树下的人却只有一个。"
    "脑海中浮现出苍的笑容。"
    "我拿出包里的蝴蝶标本和古书的译本，埋在了树下。"
    "羽依里" "苍，等你醒来，我们再一起把它们挖出来，一起读完剩下的一半……"
    "羽依里" "到时候，我还要请教你里面的故事真不真实呢……"
    "羽依里" "苍……我们不是还有一个约定吗……"
    "泪水不知不觉滑下了脸颊。"
    "我仰望着天空，祈求奇迹的出现。"
    "那种事情当然不可能在现实中存在。"
    "……真的没办法吗？"
    show bs with dissolve
    "稻荷的叫声突然传来。"
    "我心里一紧，望向它所在的方向，盼望着能看到那只七影蝶。"
    "……它对着天空中的月亮叫起来。原来是提醒我快后半夜了啊。"
    "还是放弃那些不切实际的幻想吧。"
    "这个世界上的任何事情，都是脚踏实地地做事带来的结果。"
    "赶紧回去睡觉吧。明天还要继续陪苍呢。"
    jump ch0_3
label ch0_3:
    scene bg019n3 with fade
    "躺在床上，脑中的回忆不断显现。"
    "羽依里" "根本睡不着啊。"
    "不过，注意力很快就被分散了。"
    "讨厌的蚊子突然出现，在我耳边嗡嗡叫着。"
    "羽依里" "可恶……还是打不到。"
    "我放弃了挣扎。"
    "不知是太累的缘故，还是蚊子分散了注意力，这次我很快入睡了。"
    stop music fadeout 2.0
    scene bg002a with fade
    "这是在哪里呢……？"
    "面前的商店如此熟悉。"
    "是粗点心店啊。"
    show ao com_stand smile with dissolve
    "苍" "欢迎光临……是你啊。"
    "羽依里" "苍？你不是……？"
    "苍" "别管那么多了，跟我来吧。"
    "羽依里" "嗯？去哪里？"
    "苍自顾自地走了出去。"
    "我只好跟上。"
    scene bg010a with fade
    "她带我来到了那棵她经常睡觉的树下。"
    show ao com_stand smile with dissolve
    "苍" "准备好了吗？"
    "羽依里" "什么准备好了？"
    "苍" "当然是……这个啊～"
    play music "bgm/bgm34.ogg" fadein 1.5
    show ao com_stand eye_closed_smile:
        xalign 0.49
        linear 0.1 xalign 0.51
        linear 0.1 xalign 0.49
        repeat
    "苍把我一把推倒。"
    "羽依里" "！？"
    "苍" "上次在我睡觉的时候挠痒是吧？我今天也要让你来体验一下……"
    "羽依里" "哈哈哈……快停下……"
    "没想到苍的力气如此大，我根本无法动弹。"
    stop music fadeout 3.0
    "不过，能够见到珍视的人，本身就已经很令人高兴了。"
    play music "bgm/bgm21.ogg" fadein 2.0
    "我不再挣扎，感受着面前少女手心传来的温度。"
    "……"
    scene bg019a1 with fade
    "梦醒了。"
    "醒来的时候，嘴上似乎带着一抹微笑。"
    "羽依里" "原来是梦。为什么那种感觉那么真实啊。"
    "羽依里" "能见到珍视的人，真是太好了……"
    "……突然发现身上被蚊子咬了。"
    "从来没有在这里被咬过啊。海己牌人体蚊虫诱捕器失效了吗？"
    "我起身之后，才发现桌上放着一张小纸条。"
    "我要走了哦～再见，羽依里同学。"
    "是海己的留言。似乎昨天就在这里了。"
    "背面还有一行小字。"
    "早饭在冰箱里了哟。"
    scene bg017a with fade
    "重新加热的炒饭果然没有平时好吃啊。突然发现自己竟然已经习惯了有海己的生活。"
    stop music fadeout 3.0
    "好了，今天要做什么呢？"
    "先去诊所吧，苍还等着我呢。"
    scene cg_ao04_0103 with fade
    "羽依里" "早上好。"
    play music "bgm/bgm12.ogg" fadein 1.0
    scene cg_ao04_0205 with dissolve
    "蓝" "早上好啊，今天要和苍结婚吗？"
    "蓝手中拿着苍的身体检查报告，其中“年龄”一栏上画了一个大大的红圈。显然这个数值是小于18的。"
    "羽依里" "这话和这个圈是怎么回事啊！"
    "看来蓝的气还没消。"
    "羽依里" "我也没说要这么快结婚吧！？"
    scene cg_ao04_0204 with dissolve
    "蓝" "虽然我已经把苍许诺给你了，不过你可别想在她睡着的时候做什么坏事哦？"
    "这家伙对苍还真的有一种很强的占有欲。"
    "羽依里" "……"
    scene cg_ao09_0102 with fade
    "还是和苍说说话吧。"
    "羽依里" "苍，灯笼我已经挂好了哦。"
    "羽依里" "昨天我做了一个梦……"
    "等等，这个还是不要说好了。"
    "毕竟蓝还在旁边。"
    "羽依里" "我梦见你醒过来了……"
    "我省去了挠痒痒的部分。"
    "这样就好了。虽然不完整，但毕竟不是错误的记忆。"
    "羽依里" "话说，我好像暑假作业还没写完。"
    "蓝" "你这话题转换得是否有点太快了？"
    "羽依里" "是因为想到了苍昨天晚上的事情嘛。"
    "蓝" "昨晚发生了什么？"
    "我把昨天晚上苍在迷途橘下释放出七影蝶，并且被蝴蝶包裹告诉了蓝。"
    "蓝" "你的意思是，苍通过七影蝶获得的知识，已经不复存在了？"
    "羽依里" "没错。"
    "蓝" "苍之前说过，是靠自己触碰七影蝶才知道了很多知识……"
    "蓝" "她在学校里经常睡觉啊。"
    "羽依里" "也就是说，苍她现在的认知水平已经倒退了好几年？"
    "蓝" "大概是这样吧。"
    "我突然感觉责任重大。"
    "如果苍醒来的时候无法跟上同龄人，那么她这几年不就白过了吗？即使醒来，我们还能正常沟通吗？"
    "为了蓝，她付出了10年，现在即使醒过来也要落得这样的结局……"
    "不，我绝对不允许那种事情发生。"
    "我立即从包里掏出……暑假作业？"
    "……开始读上面的内容。"
    "蓝" "你这是在干什么呢？希望苍梦游帮你写作业？"
    "羽依里" "你在说什么啊。当然是为了提升苍的认知能力啊。"
    "蓝" "暑假作业也太不靠谱了点吧！好歹拿个课本啊！"
    "羽依里" "没办法嘛～毕竟书全在家里。"
    "羽依里" "我下次带过来吧。我不在的时候，就拜托蓝了。"
    "蓝" "嗯。除此之外，我就把苍跟我说过的事情再复述一遍吧。"
    "羽依里" "嗯，拜托你了。"
    stop music fadeout 2.0
    scene bg009e with fade
    "离开医院之后已经是下午了。"
    play music "bgm/bgm01b.ogg" fadein 2.0
    "心里突然有点舍不得。"
    "这个暑假就要结束了啊。"
    "明明认识了那么多人，经历了那么多事情，为什么感觉有些空虚？"
    "七影蝶，迷途橘，空门家的职责……"
    "一个个名词和概念盘旋在脑海。"
    "还有什么没有做的事情吗？"
    "……想不出。"
    "既然明天早上就要离开了，那么先和大家道个别吧。"
    "我走向秘密基地。"
    scene bg006e with fade
    "天善和良一正在打乒乓球。"
    "良一" "哟。是羽依里啊。要不要来两局？"
    "羽依里" "……我是来道别的。我明天上午就要走了。"
    "良一" "这样啊。那么，来开送别会吧！"
    "羽依里" "不用了。"
    "羽依里" "况且现在开也来不及了。"
    "良一" "这样啊。那么，提前祝你一路顺风！"
    "羽依里" "啊，谢谢。"
    "天善" "特训的对手又要少一个了呢。可以请你最后来打一局吗？"
    "羽依里" "哦，可以啊。"
    "我拿起了旁边的球拍。"
    "乒乓的声音回荡在秘密基地中。"
    "我们沉默不语。"
    "虽然以后一定会回来，但这样的日常，却也即将变得遥不可及。"
    "我们相视无言。"
    "离别总是伤感的。"
    "因此，必须有人先打破沉默。"
    "羽依里" "那么，再见了。周末和放假我会再回来的！"
    scene bg008e with fade
    "离开秘密基地，我又和小岛上的其他人道了别。"
    scene bg019n1 with fade
    "回到家里，我收拾好了房间里的行李。"
    "羽依里" "最后一天了啊～真的有点舍不得呢。"
    "躺在床上，我认真思考了一下这股不舍中夹杂的空虚。"
    "羽依里" "果然还是因为她不在啊。"
    "不过，很快就释然了。"
    "因为，我还有必须要做的事情。"
    "也就是说，还有希望，不是吗？"
    "羽依里" "苍，等着我……"
    stop music fadeout 3.0
    "就这样进入了梦乡。"
    scene bg_kuro with fade
    show text "～August 30th～" at truecenter with dissolve
    pause 2.0
    scene bg017a with fade
    "八月三十日。"
    "返程的日子。"
    "和镜子阿姨道别后，我早早地来到了医院。"
    scene cg_ao04_0103 with fade
    play music "bgm/bgm16.ogg" fadein 2.0
    "蓝" "要走了吗？"
    "羽依里" "嗯。我下周会回来的。"
    scene cg_ao09_0201 with fade
    "羽依里" "苍，我走了。一定要，等着我哦？"
    "羽依里" "绝对不可以自己，抛下我哦？"
    "苍仍然熟睡着。"
    "蓝" "我有种直觉，苍可能短期内不会醒了。"
    "羽依里" "换句话说，长期还是有希望的。"
    "蓝" "但愿吧。我们也只能做我们该做的事情罢了。"
    "羽依里" "该做的事情吗……"
    "羽依里" "我明白了。那么，下次再见了！"
    scene bg010a with fade
    "离开医院，我走在了鸟白岛的小路上。"
    "还记得刚来的时候沿着这条路前行时的心情，夜晚迷路时的发现，山中的点点亮光。"
    "每一处都包含着这个暑假的记忆。"
    "羽依里" "感觉没怎么变呢。"
    "只是，行走的方向指向港口。"
    "正如每个故事都会走向终结，暑假也是一段有限的时光。"
    scene bg001a with fade
    "野美希" "羽依里！这里这里！"
    "在港口等船的我转头望去，只见一批人正在那里。"
    "镜子阿姨，良一，天善，野美希……甚至还有被野美希拖着的白羽。"
    "众人" "羽依里！来合影吧！"
    "野美希架好相机，顺利地拍了照片。"
    "羽依里" "谢谢你们……谢谢你们来为我送行。不过，我很快就会回来的。"
    scene bg001a1 with dissolve
    "广播" "请旅客们有序登船。"
    "羽依里" "再见了！"
    "在鸟白岛的港口，我们挥手告别。"
    "这个难忘的暑假结束了啊。"
    "现在，我终于明白如何面对暑假的终结。"
    "……留下“念想”，就不会难过。"
    "即使短暂，但只要留下目标，那么就永远不会失去方向。"
    "面对假期的消逝，就是如此。"
    "羽依里" "念念不忘，终有回响。"
    "不知为何，脑中突然蹦出来一句话。"
    "“终有回响”……是吗……"
    scene bg_kuro with fade
    show text "～September 1st～" at truecenter with fade
    pause 2.0
    scene bg_kuro with dissolve
    "新的学期开始了。"
    "熟悉的校园，熟悉的朋友……"
    "鸟白岛的点滴逐渐被埋藏到心灵深处。"
    "只留下了，一丝不可分割，永不消逝的情感。"
    "好似有一条虚无缥缈，又坚固不断的线，连接着我，和那个熟悉的地方。"
    stop music fadeout 3.0
    "……"
    "放学后，我来到了游泳社团。"
    play music "bgm/bgm99.ogg" fadein 2.0

    "羽依里" "各位，我回来了。抱歉让你们担心了。"
    "道歉之后，面对大家的挽留……"
    "羽依里" "很高兴能和大家度过那么一段游泳的时间，不过我已经决定退出了。"
    "羽依里" "我已经有了新的努力方向了。"
    "我已经，找到了人生中最重要的人和事……"
    "没错，只要完成那个目标，就能得到幸福了。"
    "离开社团之后，我便开始寻找一份合适的打工。"
    "便利店售货员？餐厅服务员？还是发传单呢？"
    "不过我都没有经验就是了，毕竟之前放学后都在参加社团活动。"
    "如果算的话，粗点心店打工算不算经验呢？"
    "希望在赚钱的同时，也留下点可以送给苍的回忆啊。"
    "走在路上，总感觉身旁有一股神秘又亲切的气息存在。"
    "是什么呢？"
    scene cg_ao12_0101 with fade
    "感觉这种东西，有时准确，有时却令人疑惑。"
    "我回顾四周。"
    scene bg_kuro with dissolve
    "除了几个陌生人，真的什么都没有。"
    "还是先专注于眼前的事物吧。"
    "前面，还有很长的路要走呢。"
    "我也要，努力才行。"
    "……"
    jump ch1_1
label ch1_1:
    show text "～September Week 1～" at truecenter with fade
    scene bg001a1 with fade
    play music "bgm/bgm01.ogg" fadein 2.0
    "夏季的炎热仍未过去。"
    "时隔一周，我再次回到了鸟白岛。"
    "羽依里" "苍，我回来了！"
    "一旁的旅客投以怪异的目光。"
    scene bg009a with fade
    "……来到了医院。"
    show ai_smile with dissolve:
        zoom 0.63
        xalign 0.65
        yalign 1
    "蓝" "羽依里！欢迎回来！"
    "羽依里" "我回来了。蓝已经可以下床活动了吗？"
    "蓝" "医生说恢复得很好，大概再过几个月就可以出院了。"
    "蓝正在做伸展运动。"
    "羽依里" "苍最近怎么样？"
    "蓝" "还是先前的状态……"
    "也是，毕竟记忆还没有找回来。"
    scene cg_ao09_0103 with dissolve
    stop music fadeout 2.0
    "病房里的空调提供着令人舒适的温度。"
    "我放下书包，突然想起临行前特意放进包里的东西。"
    "羽依里" "这是课本和我家里的一些藏书。"
    "蓝" "嗯。谢谢了，我会给苍朗读的。"
    "蓝" "嗯？等等，这个是……？"
    "只见一些教科书中，夹着一本令人眼熟的东西。"
    play music "bgm/bgm36.ogg" fadein 2.0
    "蓝手中拿着的是……这不是我正在读的同人志吗！？"
    "羽依里" "啊啊啊不是，那个是拿错了……"
    "蓝" "哦？R－18？我没收了。羽依里还没满18岁吧？"
    "……看来下次这种东西还是藏好点吧。"
    stop music fadeout 3.0
    "苍" "阿嚏！哈……"
    "转头望去，苍的被子已经有一半落到床下了。"
    play music "bgm/bgm10.ogg" fadein 2.0
    "帮她盖好吧。"
    scene cg_ao09_0201 with dissolve
    "羽依里" "要好好睡觉……感冒了可就不好了……"
    "羽依里" "苍，我已经找到打工的地方了哦。虽然辛苦，但是没关系的。我每周都会来的……"
    "一周的经历如潮水般奔涌而出。"
    "希望这记忆的洪流，能在苍心中留下一点点回忆吧。"
    "羽依里" "这就是这周发生的事情了。苍，明天见。"
    "我和蓝相视一笑，告别了这家医院。"
    stop music fadeout 3.0
    scene bg009a with fade
    "外面的天气仍然和八月份没什么区别。"
    play music "bgm/bgm04.ogg" fadein 3.0
    "羽依里" "欸？什么东西掉了？"
    "我捡起那张从口袋里掉出来的东西。"
    "羽依里" "啊，原来是船票啊。"
    "羽依里" "可是我现在只有1000日元。这不是完全不够吗！"
    "现在有一件非常紧急的事情。"
    "今天是周五，我必须在后天下午前攒够钱，来买回程的船票。"
    "该怎么做呢？"
    menu:
        "打工":
            jump ch1_1_c1
        "捡垃圾":
            jump ch1_1_c2
        "借钱":
            jump ch1_1_c3
label ch1_1_c1:
    "羽依里" "还是靠最朴实的方法吧。"
    scene bg002a with fade
    "羽依里" "说到打工，也只有这里了吧。"
    "来到了粗点心店。"
    "老奶奶" "欢迎光临。这不是小苍的熟人吗？要买点什么？"
    "羽依里" "其实，我不是来买东西的。"
    "老奶奶" "是来替小苍看店的吗？"
    "羽依里" "是……不，也不是。"
    "老奶奶" "？？？"
    "羽依里" "其实，是想来打工赚钱的。"
    "老奶奶" "哦？那么你要这盒糕点还是薯片？还是要和小苍一样的东西？"
    "老奶奶以笑脸相迎。"
    "羽依里" "啊，那就薯片吧。"
    "和糕点相比，薯片很好吃……"
    "不对，我在想什么啊！"
    "看到老奶奶的笑容，根本就没办法拒绝了！面对这样的老奶奶要怎么把拿钱说出口啊！"
    "本来想看店一会儿之后就鼓起勇气对老奶奶说出实话，不过老奶奶把店托付给我之后，就走了啊！"
    scene bg002e with dissolve
    "结果直到关店，只带了几罐薯片回家……"
    jump ch1_2
label ch1_1_c2:
    scene bg402a with fade
    "来到了灯塔旁边。"
    "……似乎、有点安静啊？"
    "紬不在吗？"
    "长椅上摆放着一个个玩偶。"
    "似乎……曾经发生过什么重要的事情。"
    "是什么呢？"
    "但是，直觉告诉我，这与现在的我已经无关了。"
    "开始捡垃圾吧。"
    "……"
    "一个下午过去了，赚到的钱……只够买份晚饭。"
    jump ch1_2
label ch1_1_c3:
    scene bg006a with fade
    "来到了秘密基地。"
    "良一" "哟，这不是羽依里吗～你回来啦！"
    "天善" "要来局乒乓球吗？"
    "羽依里" "其实，我遇到了一点小困境。"
    "良一" "哦？是什么呢？"
    "羽依里" "我没钱买回程的船票了。"
    "良一" "我来帮你……欸？"
    "羽依里" "我已经走投无路了……"
    "良一" "你这已经不是‘小’困境了吧。对了，我曾经有一个大胆的想法来赚钱，要听吗？"
    "羽依里" "你说吧。"
    "虽然大概率没什么用就是了。"
    "良一" "去粗点心店进货，然后高价卖出！"
    "羽依里" "别人都知道你的价格比较高吧。毕竟粗点心店不是岛上知名的店铺吗？"
    "良一" "不不不，我们只要把店里的东西买空，不就行了？"
    "听起来似乎可行。"
    "羽依里" "不过，你哪里找那么多钱？"
    "良一" "……是哦。嘿嘿。"
    "算了，还是我自己想想办法吧。"
    "虽然良一还想出一些主意，不过被我拒绝了。"
    "良一" "那么，你一个人加油啊！"
    "离开了秘密基地。"
    "什么都没赚到。"
    jump ch1_2
label ch1_2:
    stop music fadeout 3.0
    scene bg008e with fade
    "虽然不是很想这么做，但是一进家门，我还是向镜子阿姨求助了。"
    "镜子" "羽依里！？你怎么回来了！"
    "羽依里" "嗯，我回来了……关于为什么回来，其实说来话长……"
    "镜子" "啊，那么进来慢慢说吧。"
    scene bg017e with dissolve
    play music "bgm/bgm08.ogg" fadein 3.0
    "进屋坐到了沙发上，我仔细斟酌着话语。"
    "……毕竟这种事情有些超现实。"
    "羽依里" "这次回来，是来看苍的。"
    "镜子" "啊～是羽依里的恋人吗？"
    "事到如今，也没有其他选择了！"
    "羽依里" "嗯。我就是来探望她的。"
    "镜子" "啊，这件事已经在岛上传开了呢。"
    "镜子" "不过，到底是为什么迟迟不醒来呢？"
    "啊，那个蝴蝶标本我还带着。"
    "就拿这个解释吧。"
    "镜子阿姨全程面带笑容地听着我的讲述，似乎早已看透一切。"
    "羽依里" "大概就是这样。"
    "镜子" "看来，羽依里在暑假里有了一段很有意思的经历呢。那么我也就放心了。"
    "羽依里" "不过，我现在遇到了一点问题，我没钱买回去的船票了。"
    "镜子" "啊，没事没事，仓库里不重要的东西本来就卖出去一部分了，有不少钱哦。"
    "羽依里" "我真的可以拿吗？"
    "镜子" "本来就是羽依里的那部分哦～作为帮忙整理的工钱。"
    "虽然我这个暑假什么也没做就是了。"
    "羽依里" "那么我就不客气地收下了。"
    "看来，问题似乎解决了。"
    "羽依里" "我出门了～"
    "解决作业后，我百无聊赖地走出了家门。"
    scene bg008n with dissolve
    "就如来到岛上的第一个夜晚一样，漫无目的地在岛上闲逛。"
    "毕竟居民区有着几盏路灯，也不至于摔倒。"
    "脑海里突然冒出一个想法。"
    "做点恋人该做的事情吧。"
    "和苍一起度过一晚。"
    "脚步不知不觉变更了方向。"
    scene bg009n with dissolve
    "回过神来时，已经到了医院的门口。"
    scene cg_ao09_0103 with dissolve
    stop music fadeout 3.0
    "已经是深夜了，对前台的护士表明身份之后，没有敲门便悄悄进入病房。"
    "蓝已经睡着了啊。"
    "一旁的苍一如既往地沉睡着。"
    "不过，被子似乎再次落了下来。"
    "要怎么做呢？"
    menu:
        "帮她盖好被子":
            jump ch1_2_c1
        "钻进去一起睡":
            scene cg_ao09_0201 with dissolve
            play music "bgm/bgm35.ogg" fadein 3.0
            jump ch1_2_c2
label ch1_2_c1:
    "羽依里" "苍，睡觉要好好睡哦。"
    scene cg_ao09_0201 with dissolve
    "帮苍盖好了被子。"
    "摊开旁边的折叠床，默默守护在苍的身旁。"
    "这是我现在唯一能做的事情了。"
    "我知道，她就在那里，不会离去。"
    "不过，一想到身边睡着两个美少女，又有些激动。"
    "有什么声音。"
    scene cg_ao09_0103 with dissolve
    "苍的被子似乎被她在睡梦中拉了下来。"
    "上半身一览无余。"
    "‘好想和她在一起。’"
    "脑海中突然蹦出一个念头。"
    play music "bgm/bgm35.ogg" fadein 3.0
    "我站起来，偷偷亲了苍那水灵的嘴唇。"
    "一个大胆的想法在脑中产生。"
    jump ch1_2_c2
label ch1_2_c2:
    "脱掉外套之后，我偷偷爬进了苍的被窝。"
    "面前的苍不知为何，突然动了起来。"
    "她把我紧紧抱在怀里，根本不给我任何挣脱的机会。"
    "羽依里" "唔唔唔！？"
    "整个脸都被苍的某个部位包裹住了！"
    "我拼命挣扎，露出了鼻孔来呼吸。"
    "虽然那个地方很柔软，不过差点被闷死。"
    "‘死里逃生’的我试图把一半落在地上的被子拉上来，却发现我根本动不了。"
    "苍" "羽依里，不要走……不要……"
    "耳畔传来朦胧的低语，身上的束缚又增添了几分力道。"
    "不过，这样也挺不错的，不是吗？"
    stop music fadeout 3.0
    play music "bgm/bgm28b.ogg" fadein 3.0
    "我细细体会着小苍的体温，同时为她因外露而微凉的身体提供热量。"
    "窗外吹来了一阵风。"
    "我抱紧了苍。"
    "一阵阵暖流正逐渐流过两个人的全身。"
    "苍微微放松了警惕，我也得以自由呼吸。"
    "羽依里" "哈……呼……"
    "大口喘气的同时，突然意识到刚覆盖在我的脸上的东西，似乎是……"
    "两座大山？"
    "……"
    "赶紧移动了一下头部，避开了这个柔软的部分。"
    "和苍在一起，似乎有一种特殊的安心感。"
    "虽然已经有过好几次了，不过抱住女孩子的身体，每次都能带来不一样的体验。"
    "想永远能和苍呆在一起，每晚搂着她入睡。"
    "虽然今晚已经冲动做了这种事情……"
    "但眼下最重要的事情，还是让苍醒过来啊。"
    "我逐渐进入了梦乡……"
    "……"
    stop music fadeout 3.0
    "清晨的阳光照入病房。"
    "阳光被什么东西挡住了。"
    "我睁开了眼睛。"
    "面前是苍那熟悉的睡脸。"
    play music "bgm/bgm24.ogg" fadein 3.0
    "不过，似乎有一个黑影挡住了阳光。"
    "脊背升起一股凉意。"
    "我勉强转过头去，和蓝的目光相撞。"
    play music "bgm/bgm35.ogg" fadeout 3.0 fadein 3.0
    scene cg_ao04_0206 with fade
    "蓝" "哟，你们的感情还真好啊～"
    "羽依里" "不是不是，那个听我解释……"
    "我试图先从苍的怀里挣脱出来，再找点什么借口。"
    "结果苍抱得更紧了。"
    "苍" "呜呜，羽依里……不要嘛……"
    "这家伙到底是为什么突然变成这样的啊？"
    "蓝" "哼，罢了，我就不打扰二位了。"
    "蓝" "啊~毕竟总有一天苍要嫁出去的，先熟悉一下也不错。"
    "羽依里" "谢……谢谢？"
    "完全不知道应该说什么……"
    scene cg_ao04_0205 with dissolve
    "蓝" "谢什么谢啊！你把苍抢走了知道吗！？"
    "……"
    "羽依里" "嗯……可以请你帮我把她拉开吗？"
    "蓝" "……自己来！"
    "……"
    "花了好大力气才挣脱。"
    stop music fadeout 3.0
    "直到我离开病房，蓝都呆呆地望着窗外。"
    "下次给她带点什么有意思的东西好了。"
    jump ch1_3
label ch1_3:
    scene bg009a with fade
    "好了，接下来做什么呢？"
    "百无聊赖地在岛上闲逛。"
    play music "bgm/bgm07.ogg" fadein 1.0
    "我到底是来干什么的啊？"
    "明明时间是那么宝贵的东西……"
    "好，那就珍惜一下时间吧！"
    scene bg019a with dissolve
    "回到家里，打开课本开始学习。"
    "早上精神就是好啊，竟然涌起了学习的欲望。"
    "……"
    window hide
    scene bg_kuro with wipedown
    scene bg019a with wipeup
    window auto
    "羽依里" "哈……啊！已经中午了吗！？"
    "刚才还说精神好！？明明马上就睡着了啊！"
    "算了，事已至此，先吃饭吧。"
    stop music fadeout 1.0
    scene bg017a with dissolve
    "……？"
    "不对。"
    play music "bgm/bgm24.ogg" fadein 0.5
    "为什么我会自动坐到客厅的桌子前呢？"
    "明明上面空空如也。"
    "说起来，昨天来这里的时候就觉得有些奇怪了。"
    "为什么……客厅里有{=red_highlight}3张坐垫{/red_highlight}呢？"
    "为什么厨房里，有{=red_highlight}3双筷子{/red_highlight}放在外面？"
    "为什么，我的房间旁边，还有{=red_highlight}一间看起来有人居住的房间{/red_highlight}？"
    "我、镜子阿姨，不应该是{=red_highlight}2个人{/red_highlight}吗？"
    "整个暑假好像{=red_highlight}都是如此{/red_highlight}啊？"
    "不，不对，我好像忘掉了什么很重要的东西。"
    "似乎连{=red_highlight}遗忘本身{/red_highlight}都要忘却了。"
    "啊！好像有{=red_highlight}一张纸条{/red_highlight}……"
    "那是过去的自己留下的提示，是重要的东西。"
    scene bg019a with dissolve
    "我奔回房间，试图寻找到它。"
    "什么都没有。"
    "垃圾桶也被清空了。"
    "最后一缕思绪消失在了脑海。"
    stop music fadeout 2.0
    "我……在做什么来着？"
    "啊，对了，我要先去食堂吃饭。"
    scene bg_kuro with fade
    play music "bgm/bgm15.ogg" fadein 2.0
    "……"
    show text "时间是线性的。" at truecenter with dissolve
    ""
    show text "在当前做的选择，会影响到{=red_highlight}后面的发展{/red_highlight}。" at truecenter with dissolve
    ""
    "有点像{=red_highlight}GalGame{/red_highlight}，是不是？"
    "那么我们作为时间线中的人，是世界的控制者吗？"
    "或许是吧。"
    "只是我们不能存档，回溯罢了……"
    "真的不能吗？"
    show text "除非有{=red_highlight}一种能力{/red_highlight}……" at truecenter with dissolve
    ""
    "……"
    stop music fadeout 2.0
    scene cg_ao09_0201 with fade
    play music "bgm/bgm01.ogg" fadein 1.5
    "鸟白岛的下午。"
    "下午也继续陪在苍身边。"
    "绞尽脑汁却说不出一个字来。"
    "蓝" "明明陪着她，却一句话也不说……"
    "蓝" "啊，吵架也是情侣间学会相处的必要部分啊。"
    "抬头和做完了身体活动的蓝对上了视线……"
    "羽依里" "苍还没醒呢！不要默认我是个得了妄想症的疯子好吗！"
    "羽依里" "对了，可以带苍出去走走吗？"
    "羽依里" "我去和医生说说吧。"
    "医生" "哦，是苍的恋人啊。"
    "羽依里" "……"
    "羽依里" "可以带苍出去吗？"
    "医生" "可以啊，看她这样也没什么身体问题，轮椅在那边……"
    "医生" "哦对了，如果想经常带她出去的话，建议你自己买个轮椅哦。"
    "医生" "毕竟……医院的轮椅已经有些破了……万一散架了还要麻烦你把她背回来。"
    "羽依里" "好的。"
    "把轮椅加入购物清单吧。"
    "医生" "啊对了，不要离开医院太远哦。尽量往大路上推。"
    "羽依里" "明白了！"
    "走吧。"
    "是时候踏上新的旅途了。"
    scene bg009a with fade
    "我要带着苍，一起游览这个给我们留下一个暑假回忆的地方。"
    "去找到吧，那些美好的回忆——"
    scene bg_kuro with fade
    stop music fadeout 3.0
    "……"
    "有人认为，平行世界是存在的。"
    "当你在一条时间线上做出一种选择，在同一个时间点的另一个你可能做出另一种选择。"
    "选择可以决定时间线发展。"
    "所以就产生了树枝状的结构。"
    "啊，就是GalGame里的树状图。"
    "一般来说，树枝不会碰撞。"
    "但万一……有外力把树枝折了一下呢？"
    "时间线发生了交错……"
    "那么，不属于这个世界的东西，就会出现……"
    "……"
    show text "～October Week 1～" at truecenter with fade
    scene bg009a with fade
    play music "bgm/bgm07.ogg" fadein 3.0
    "入秋了。"
    show ai_smile with dissolve:
        zoom 0.63
        xalign 0.65
        yalign 1
    "蓝的身体似乎正在恢复，已经能够在医院内自由走动了。"
    "过一段时间估计就可以出院了吧。"
    "今天也带苍出去走走吧。"
    scene bg011a with fade
    "推着轮椅走到了一处陌生由熟悉的地方。"
    "上山的入口处，一阵秋风吹过。"
    "羽依里" "好久没有去看过迷途橘了。"
    "鬼使神差般的，我背上了轮椅上的苍。"
    "当然，她一点也没有要醒来的样子。"
    "或许是退出社团的缘故，总觉得背着苍变得更累了。"
    "走到半路上已是大汗淋漓。"
    "在这里休息一下吧。"
    scene cg_ao05_0103 with fade
    "放下背上的苍，我用背部支撑着她坐了下来。"
    "羽依里" "还记得吗？当初我们一起找蝴蝶的时候，也是这样的情形呢。"
    "苍并没有回应。"
    "我想象了一下她的回复。"
    "苍" "是啊。"
    "不不不，太平淡了点吧。"
    "好吧，我承认也没什么想象力……"
    "羽依里" "好！我们继续走吧！"
    scene bg202a1 with fade
    "大块空地上，迷途橘静静地等待在那里。"
    if ending == 1:
        jump end_1
    else:
        jump ch1_4
label end_1:
    stop music fadeout 1.0
    "这时，一个光亮的东西慢慢落到了我的手边。"
    "是一只七影蝶。"
    "我心里一紧，伸出了手……"
    "然而，蝴蝶飞走了。"
    "羽依里" "怎么回事？"
    "羽依里" "啊，山之祭祀的时间已经过了。"
    "脑中突然冒出一个想法。"
    "一个可能性很小，但却十分重要的猜想。"
    play music "bgm/bgm28.ogg" fadein 1.0
    "羽依里" "等等！别走！等等我！"
    show bs happy with ease:
        xoffset 700
        yoffset 700
    "稻荷" "蹦——蹦——"
    "身边的稻荷跳了出去。"
    "羽依里" "不可以！等等！把你的记忆给我看啊！！！"
    "我跑了过去……"
    "伸出我的双手——"
    "但七影蝶擦手而过。"
    "羽依里" "不要走！！！"
    "七影蝶消失了。"
    "我什么都没看到。"
    "为什么啊！"
    hide bs with ease
    "这时，我的身旁突然聚集了一群七影蝶……"
    "？？？" "时间是线性的。"
    "？？？" "这句话，可没人能证明哦~"
    "？？？" "在走之前，把我的记忆，给你看看吧。"
    "脑中突然涌出了巨量的信息。"
    "白羽、羽末……"
    "羽末？海己？女儿？"
    "这都是什么啊！"
    "羽依里" "我不承认！这不是我的记忆！"
    "？？？" "那么，看看这个吧。"
    "羽末为了拯救自己的母亲，回到了羽依里和白羽相遇的鸟白岛。"
    "？？？" "你已经，满足了吧？"
    "羽末" "是时候，去见妈妈了……"
    "新的夏日冒险，开始了——"
    show text "～BAD END 新的轮回～" at truecenter with dissolve
    pause 2.0
    return
label ch1_4:
    "啊，突然想起来之前把书放在这里了来着。"
    "趁着这个机会，把书读给苍听听吧。"
    "羽依里" "啊！找到了！"
    "但是，感觉有点奇怪啊？"
    stop music fadeout 3.0
    "这本书有这么薄吗？"
    "轻轻抹去上面的泥土，一串文字映入眼帘——"
    play music "bgm/bgm37.ogg" fadein 1.0
    "ALKA TALE"
    "羽依里" "这是……什么东西？"
    "打开它的一瞬间，似乎有什么东西永远地消失了。"
    "耳边似乎传来什么声音。"
    "？？？" "再见，▯▯。祝▯们▯福。"
    "？？？" "我已▯▯足了，是▯▯走了。"
    "？？？" "我▯，▯会▯见吗？"
    "一个特殊的名字，羽末，留在了脑海中。"
    "虽然只有一瞬间，立刻就抛之脑后了。"
    "手中只是一本普通的日记本而已。"
    "大片的空白。"
    "一定是哪个孩子把它埋在这里的吧。"
    "或许那本古书译本，被某个喜欢探险的孩子挖走了。"
    "下次找镜子阿姨再翻译一遍吧。"
    "这次一定要去复印店做个备份！"
    scene bg011e with fade
    "抬头一看，夕阳已经染红了天空。"
    "啊，已经那么晚了啊。"
    "该走了，否则医院可能就要来找人了。"
    "背起熟睡的苍，一口气走到了山脚的轮椅旁……"
    "To be continued...v2.0暂时到这里，即将返回主界面，请立即存档！"
    return
    # 此处为游戏结尾。