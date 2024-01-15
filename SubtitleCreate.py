import re

# Input string
input_string = """[00:00.000 --> 00:03.000]  I'm a woman. I grew up in a single-parent family.
[00:03.000 --> 00:05.000]  And...
[00:09.000 --> 00:11.000]  I'm a man.
[00:12.000 --> 00:14.000]  I'm a man.
[00:14.000 --> 00:16.000]  I'm a man.
[00:16.000 --> 00:18.000]  I'm a man.
[00:18.000 --> 00:20.000]  I'm a man.
[00:20.000 --> 00:22.000]  I'm a man.
[00:22.000 --> 00:24.000]  I'm a man.
[00:24.000 --> 00:26.000]  I'm a man.
[00:26.000 --> 00:28.000]  I'm a man.
[00:29.000 --> 00:31.000]  Sis.
[00:32.000 --> 00:34.000]  Let's go to mom's place.
[00:39.000 --> 00:41.000]  My beloved mother...
[00:41.000 --> 00:43.000]  ...has passed away.
[00:48.000 --> 00:50.000]  Karen?
[00:50.000 --> 00:52.000]  Yuzuru?
[00:52.000 --> 00:54.000]  You must be hungry.
[00:54.000 --> 00:56.000]  Dinner is ready.
[00:59.000 --> 01:01.000]  I'm hungry.
[01:03.000 --> 01:05.000]  Is mom doing well over there?
[01:05.000 --> 01:07.000]  Yes.
[01:07.000 --> 01:09.000]  She's smiling.
[01:09.000 --> 01:11.000]  I know.
[01:11.000 --> 01:13.000]  That's why...
[01:13.000 --> 01:15.000]  ...we have to get along.
[01:15.000 --> 01:17.000]  Yes.
[01:28.000 --> 01:30.000]  Yuzuru...
[01:41.000 --> 01:43.000]  Yuzuru doesn't change at all.
[01:55.000 --> 01:57.000]  Today is your favorite day.
[01:57.000 --> 01:59.000]  Yes.
[01:59.000 --> 02:01.000]  Let's go.
[02:03.000 --> 02:05.000]  Let's go.
[02:11.000 --> 02:15.000]  Ten years have passed since then.
[02:17.000 --> 02:19.000]  Let's eat.
[02:19.000 --> 02:21.000]  It looks delicious.
[02:21.000 --> 02:23.000]  Thank you.
[02:23.000 --> 02:25.000]  You like vegetables, don't you?
[02:25.000 --> 02:27.000]  Eat vegetables.
[02:32.000 --> 02:34.000]  Don't you eat vegetables?
[02:34.000 --> 02:36.000]  I do.
[02:36.000 --> 02:38.000]  I like vegetables.
[02:48.000 --> 02:50.000]  You have something on your face.
[02:50.000 --> 02:52.000]  No, I don't.
[02:52.000 --> 02:54.000]  Really?
[02:54.000 --> 02:56.000]  Yes.
[02:56.000 --> 02:58.000]  You two get along very well.
[02:58.000 --> 03:00.000]  I'm embarrassed to look at you.
[03:00.000 --> 03:02.000]  You're older than me.
[03:02.000 --> 03:04.000]  She's still a child.
[03:04.000 --> 03:06.000]  No, I'm not.
[03:10.000 --> 03:12.000]  Karen is a good girl.
[03:12.000 --> 03:14.000]  She's like a real mother.
[03:14.000 --> 03:16.000]  I think so.
[03:16.000 --> 03:18.000]  She's a sweet girl.
[03:23.000 --> 03:25.000]  No.
[03:25.000 --> 03:27.000]  The person who raised me...
[03:27.000 --> 03:29.000]  ...is my sister.
[03:53.000 --> 03:55.000]  Yuzuru...
[04:01.000 --> 04:03.000]  Yuzuru...
[04:03.000 --> 04:05.000]  Where's mom?
[04:07.000 --> 04:09.000]  Yuzuru...
[04:09.000 --> 04:11.000]  Mom's gone.
[04:13.000 --> 04:15.000]  I tried my best.
[04:19.000 --> 04:21.000]  Please understand.
[04:22.000 --> 04:24.000]  I can't help it.
[04:25.000 --> 04:27.000]  Why?
[04:27.000 --> 04:29.000]  No, no, no.
[04:29.000 --> 04:31.000]  Without mom, I...
[04:37.000 --> 04:39.000]  Don't worry.
[04:39.000 --> 04:41.000]  From now on...
[04:41.000 --> 04:43.000]  ...I'll be Yuzuru's mother.
[04:46.000 --> 04:48.000]  Really?
[04:49.000 --> 04:51.000]  Okay, okay.
[04:53.000 --> 04:55.000]  It's okay.
[05:06.000 --> 05:08.000]  Yuzuru...
[05:08.000 --> 05:10.000]  It's time to brush your teeth.
[05:18.000 --> 05:20.000]  Okay.
[05:49.000 --> 05:51.000]  Yuzuru...
[05:52.000 --> 05:54.000]  When you're lonely...
[05:55.000 --> 05:57.000]  ...I'll always be there for you.
[05:59.000 --> 06:01.000]  Don't cry anymore.
[06:18.000 --> 06:20.000]  Mom...
[06:20.000 --> 06:22.000]  Mom...
[06:23.000 --> 06:25.000]  Honey...
[06:25.000 --> 06:27.000]  What's wrong?
[06:30.000 --> 06:32.000]  It's okay.
[06:32.000 --> 06:34.000]  It's okay.
[06:40.000 --> 06:45.000]  I wasn't able to grow up at all.
[06:45.000 --> 06:48.000]  I wasn't able to leave my father yet.
[06:48.000 --> 06:50.000]  And then...
[06:51.000 --> 06:54.000]  ...I grew up...
[06:54.000 --> 06:57.000]  ...in my sister's place.
[06:58.000 --> 07:00.000]  Yuzuru...
[07:15.000 --> 07:18.000]  I get sleepy when I'm full.
[07:22.000 --> 07:24.000]  Karen...
[07:25.000 --> 07:27.000]  It's time for your part-time job.
[07:27.000 --> 07:29.000]  Yes.
[07:29.000 --> 07:31.000]  Yuzuru...
[07:31.000 --> 07:34.000]  You have to do your summer homework.
[07:36.000 --> 07:38.000]  I'm counting on you.
[07:38.000 --> 07:40.000]  Okay.
[07:40.000 --> 07:42.000]  Good luck.
[07:45.000 --> 07:47.000]  Yuzuru...
[07:47.000 --> 07:50.000]  You have to finish your homework first.
[07:50.000 --> 07:52.000]  I don't want to.
[07:52.000 --> 07:54.000]  You don't want to?
[07:54.000 --> 07:56.000]  I don't want to.
[07:56.000 --> 07:58.000]  I'm going to take a nap.
[07:58.000 --> 08:00.000]  Okay.
[08:00.000 --> 08:02.000]  When you take a nap...
[08:02.000 --> 08:04.000]  ...will you be able to do it later?
[08:04.000 --> 08:05.000]  Yes.
[08:05.000 --> 08:07.000]  It's a promise.
[08:07.000 --> 08:09.000]  Yes.
[08:23.000 --> 08:25.000]  What's wrong?
[08:25.000 --> 08:27.000]  Aren't you sleepy?
[08:28.000 --> 08:30.000]  I think...
[08:30.000 --> 08:33.000]  ...it's time for a snack.
[08:34.000 --> 08:38.000]  You're always like that when I'm not around.
[08:52.000 --> 08:54.000]  Okay.
[09:22.000 --> 09:25.000]  I'm sleepy.
[09:52.000 --> 09:54.000]  What's wrong?
[10:12.000 --> 10:14.000]  What's wrong?
[10:22.000 --> 10:24.000]  I'm sleepy.
[10:24.000 --> 10:26.000]  I'm sleepy.
[10:49.000 --> 10:51.000]  It's hard, isn't it?
[10:51.000 --> 10:53.000]  Yes.
[10:54.000 --> 10:56.000]  I'm sleepy.
[10:56.000 --> 10:58.000]  I'm sleepy.
[11:27.000 --> 11:29.000]  I'm fine.
[11:29.000 --> 11:31.000]  I'm sleepy.
[11:55.000 --> 11:57.000]  Come here.
[11:59.000 --> 12:01.000]  Come here.
[12:10.000 --> 12:12.000]  This is the most relaxing, isn't it?
[12:12.000 --> 12:14.000]  Yes.
[12:30.000 --> 12:34.000]  You really like boobs, don't you?
[12:34.000 --> 12:36.000]  Yes.
[12:59.000 --> 13:01.000]  It's good.
[13:30.000 --> 13:34.000]  You have a very nice face.
[13:34.000 --> 13:36.000]  It's cute.
[13:42.000 --> 13:44.000]  You're so sweet.
[13:51.000 --> 13:53.000]  Do you like my boobs?
[13:53.000 --> 13:55.000]  Yes.
[14:00.000 --> 14:03.000]  Do you feel like you're going to puke?
[14:13.000 --> 14:15.000]  Are you going to puke?
[14:19.000 --> 14:22.000]  You look like you're in a lot of pain.
[14:26.000 --> 14:28.000]  Do you want me to turn you over?
[14:29.000 --> 14:31.000]  Yes.
[14:34.000 --> 14:36.000]  I'm sleepy.
[14:36.000 --> 14:38.000]  Are you sleepy?
[14:39.000 --> 14:41.000]  I'm sleepy.
[14:41.000 --> 14:43.000]  I'm sleepy.
[14:53.000 --> 14:55.000]  You're in a lot of pain.
[14:56.000 --> 14:58.000]  Do you feel better?
[14:58.000 --> 15:00.000]  Yes.
[15:00.000 --> 15:02.000]  That's good.
[15:15.000 --> 15:17.000]  You're in a lot of pain.
[15:17.000 --> 15:19.000]  Yes.
[15:20.000 --> 15:22.000]  You're in a lot of pain.
[15:23.000 --> 15:25.000]  You're beautiful.
[15:26.000 --> 15:28.000]  Thank you.
[15:29.000 --> 15:31.000]  You're only growing up here.
[15:31.000 --> 15:33.000]  Yes.
[15:33.000 --> 15:35.000]  It feels good.
[15:35.000 --> 15:37.000]  I have a lot of boobs.
[15:38.000 --> 15:43.000]  Your boobs have enveloped me.
[15:44.000 --> 15:46.000]  For the past 10 years.
[15:46.000 --> 15:48.000]  Forever.
[15:49.000 --> 15:51.000]  Thank you.
[16:19.000 --> 16:21.000]  Thank you.
[16:34.000 --> 16:36.000]  Aren't you going to sleep?
[16:36.000 --> 16:38.000]  No.
[16:38.000 --> 16:40.000]  Have you gone to bed?
[16:40.000 --> 16:42.000]  No.
[16:44.000 --> 16:46.000]  Come here.
[16:50.000 --> 16:52.000]  Come here.
[17:04.000 --> 17:06.000]  You have to have boobs, too.
[17:10.000 --> 17:12.000]  I know.
[17:19.000 --> 17:21.000]  Thank you.
[17:49.000 --> 17:51.000]  Thank you.
[18:19.000 --> 18:21.000]  Thank you.
[18:50.000 --> 18:53.000]  You really like boobs, don't you?
[18:54.000 --> 18:56.000]  Yes.
[19:09.000 --> 19:11.000]  You're licking them a lot today.
[19:19.000 --> 19:21.000]  Thank you.
[19:37.000 --> 19:39.000]  Are you sleepy?
[19:39.000 --> 19:41.000]  No.
[19:45.000 --> 19:47.000]  You can't stand it today, can you?
[19:47.000 --> 19:49.000]  Yes.
[19:50.000 --> 19:52.000]  It can't be helped.
[20:17.000 --> 20:19.000]  I'm sleepy.
[20:37.000 --> 20:39.000]  I remember strange things more and more.
[20:47.000 --> 20:49.000]  Thank you.
[21:17.000 --> 21:19.000]  Thank you.
[21:30.000 --> 21:32.000]  Thank you.
[21:38.000 --> 21:42.000]  I'm glad you didn't get sick.
[21:43.000 --> 21:45.000]  Yes.
[21:47.000 --> 21:49.000]  Thank you.
[22:09.000 --> 22:11.000]  Can you sleep well?
[22:11.000 --> 22:13.000]  Yes.
[22:17.000 --> 22:19.000]  Thank you.
[22:20.000 --> 22:22.000]  Thank you.
[22:22.000 --> 22:24.000]  Thank you.
[22:46.000 --> 22:48.000]  Come here.
[22:52.000 --> 22:54.000]  Thank you.
[23:23.000 --> 23:27.000]  It's intense today, isn't it?
[23:27.000 --> 23:29.000]  Yes.
[23:32.000 --> 23:34.000]  Did something bad happen to you?
[23:34.000 --> 23:36.000]  No.
[23:43.000 --> 23:46.000]  You haven't changed since you had boobs.
[23:47.000 --> 23:49.000]  You've grown up.
[23:53.000 --> 23:55.000]  Thank you.
[24:05.000 --> 24:07.000]  Do you like my voice?
[24:07.000 --> 24:09.000]  Yes.
[24:22.000 --> 24:24.000]  Thank you.
[24:30.000 --> 24:32.000]  Does it feel good?
[24:32.000 --> 24:34.000]  Yes.
[24:45.000 --> 24:48.000]  It's been a while since you had boobs, so they're still there, aren't they?
[24:48.000 --> 24:50.000]  Yes.
[24:52.000 --> 24:55.000]  Thank you.
[25:22.000 --> 25:24.000]  Thank you.
[25:42.000 --> 25:44.000]  You can have a lot of boobs.
[25:44.000 --> 25:46.000]  Yes.
[25:52.000 --> 25:54.000]  Thank you.
[26:22.000 --> 26:24.000]  Thank you.
[26:44.000 --> 26:46.000]  Your favorite boobs.
[26:47.000 --> 26:49.000]  Thank you.
[26:50.000 --> 26:52.000]  Doesn't it hurt?
[26:52.000 --> 26:54.000]  No.
[26:55.000 --> 26:57.000]  Thank you.
[26:59.000 --> 27:02.000]  I'm glad you're happy.
[27:07.000 --> 27:09.000]  I'm going to sleep.
[27:09.000 --> 27:11.000]  What?
[27:17.000 --> 27:19.000]  What's wrong?
[27:31.000 --> 27:33.000]  Do you want to play?
[27:33.000 --> 27:35.000]  Yes.
[27:35.000 --> 27:37.000]  I'm going to sleep.
[27:44.000 --> 27:48.000]  I want to play with your boobs.
[27:49.000 --> 27:51.000]  Okay.
[27:56.000 --> 27:59.000]  But don't stay up too late.
[27:59.000 --> 28:01.000]  Okay.
[28:05.000 --> 28:08.000]  I'm going to sleep.
[28:36.000 --> 28:38.000]  You're still a child.
[28:39.000 --> 28:41.000]  You're talking nonsense.
[29:05.000 --> 29:07.000]  I'm going to sleep.
[29:15.000 --> 29:17.000]  I'm going to sleep.
[29:17.000 --> 29:19.000]  Your eyes are big.
[29:28.000 --> 29:30.000]  Your eyes are very big.
[29:35.000 --> 29:37.000]  I'm going to sleep.
[30:05.000 --> 30:07.000]  I'm going to sleep.
[30:35.000 --> 30:37.000]  I'm going to sleep.
[31:05.000 --> 31:07.000]  I'm going to sleep.
[31:35.000 --> 31:37.000]  I'm going to sleep.
[32:01.000 --> 32:03.000]  I'm going to sleep.
[32:05.000 --> 32:07.000]  I'm going to sleep.
[32:13.000 --> 32:15.000]  I'm going to sleep.
[32:19.000 --> 32:25.000]  I'm going to make you happy.
[32:28.000 --> 32:31.000]  I'm very happy.
[32:31.000 --> 32:33.000]  I'm glad.
[32:35.000 --> 32:37.000]  I'm going to sleep.
[32:42.000 --> 32:44.000]  I'm going to sleep.
[32:47.000 --> 32:49.000]  I'm going to sleep.
[32:52.000 --> 32:54.000]  I'm going to sleep.
[32:59.000 --> 33:01.000]  I'm going to sleep.
[33:06.000 --> 33:08.000]  I'm going to sleep.
[33:11.000 --> 33:13.000]  You're an adult.
[33:13.000 --> 33:15.000]  You like this, don't you?
[33:20.000 --> 33:22.000]  I'm going to sleep.
[33:35.000 --> 33:37.000]  I'm going to sleep.
[33:51.000 --> 33:53.000]  I'm going to sleep.
[34:01.000 --> 34:03.000]  I'm fine.
[34:05.000 --> 34:07.000]  I'm fine.
[34:36.000 --> 34:38.000]  I'm going to sleep.
[34:40.000 --> 34:42.000]  I'm fine.
[34:44.000 --> 34:46.000]  I'm fine.
[34:56.000 --> 34:58.000]  Water is kind.
[35:05.000 --> 35:07.000]  I'm going to sleep.
[35:35.000 --> 35:37.000]  I'm going to sleep.
[36:05.000 --> 36:07.000]  I'm going to sleep.
[36:11.000 --> 36:13.000]  You don't have to do that.
[36:15.000 --> 36:17.000]  You can't sleep, can you?
[36:35.000 --> 36:37.000]  I'm going to sleep.
[36:37.000 --> 36:39.000]  I'm going to sleep.
[36:41.000 --> 36:43.000]  I'm going to sleep.
[36:43.000 --> 36:45.000]  I'm going to sleep.
[36:45.000 --> 36:47.000]  I'm going to sleep.
[36:47.000 --> 36:49.000]  I'm going to sleep.
[36:49.000 --> 36:51.000]  I'm going to sleep.
[36:51.000 --> 36:53.000]  I'm going to sleep.
[36:53.000 --> 36:55.000]  I'm going to sleep.
[36:59.000 --> 37:01.000]  I'm going to sleep.
[37:05.000 --> 37:07.000]  I'm going to sleep.
[37:11.000 --> 37:13.000]  I can't stand it anymore.
[37:15.000 --> 37:17.000]  Does it hurt?
[37:17.000 --> 37:19.000]  It hurts.
[37:36.000 --> 37:38.000]  Are you all right?
[37:40.000 --> 37:42.000]  I'm fine.
[37:42.000 --> 37:44.000]  I'm going to sleep.
[38:04.000 --> 38:06.000]  I'm going to give you a lot of medicine.
[38:08.000 --> 38:10.000]  I want you to feel better.
[38:12.000 --> 38:14.000]  You don't have to worry about me.
[38:14.000 --> 38:16.000]  I'm fine.
[38:26.000 --> 38:28.000]  Help me.
[38:33.000 --> 38:35.000]  Does it hurt?
[38:37.000 --> 38:39.000]  Are you all right?
[38:42.000 --> 38:45.000]  I'm going to sleep.
[39:12.000 --> 39:14.000]  I'm going to sleep.
[39:36.000 --> 39:38.000]  You can move as you like.
[39:42.000 --> 39:44.000]  I'm going to sleep.
[39:58.000 --> 40:00.000]  I'm going to sleep.
[40:04.000 --> 40:06.000]  I'm going to sleep.
[40:13.000 --> 40:15.000]  How do you feel?
[40:15.000 --> 40:17.000]  I feel great.
[40:17.000 --> 40:19.000]  I'm glad.
[40:19.000 --> 40:21.000]  How do you feel?
[40:33.000 --> 40:35.000]  I'm sleepy.
[40:42.000 --> 40:44.000]  I'm sleepy.
[41:01.000 --> 41:03.000]  You can talk a lot.
[41:12.000 --> 41:14.000]  You can talk a lot.
[41:42.000 --> 41:44.000]  I'm sorry.
[41:48.000 --> 41:50.000]  I'm sorry.
[42:12.000 --> 42:14.000]  I'm sorry.
[42:17.000 --> 42:19.000]  I'm sorry.
[42:21.000 --> 42:23.000]  I'm fine.
[42:27.000 --> 42:29.000]  I'm sorry.
[42:42.000 --> 42:44.000]  I'm sorry.
[42:57.000 --> 42:59.000]  I want you to feel better.
[43:01.000 --> 43:03.000]  I'm fine.
[43:05.000 --> 43:07.000]  I feel great.
[43:08.000 --> 43:10.000]  I'm sorry.
[43:12.000 --> 43:14.000]  I want you to feel better.
[43:14.000 --> 43:16.000]  I feel great.
[43:19.000 --> 43:21.000]  If you feel better, you can sleep soundly.
[43:37.000 --> 43:39.000]  I feel great.
[43:46.000 --> 43:48.000]  I feel great.
[43:51.000 --> 43:53.000]  I feel great.
[44:08.000 --> 44:10.000]  I feel great.
[44:10.000 --> 44:12.000]  I feel great.
[44:22.000 --> 44:24.000]  I feel great.
[44:38.000 --> 44:40.000]  I feel great.
[44:43.000 --> 44:45.000]  I feel great.
[44:45.000 --> 44:47.000]  I'm glad.
[44:54.000 --> 44:56.000]  I feel great.
[44:57.000 --> 44:59.000]  I feel great.
[45:04.000 --> 45:06.000]  I feel great.
[45:08.000 --> 45:10.000]  I feel great.
[45:21.000 --> 45:23.000]  How do you feel?
[45:24.000 --> 45:26.000]  I feel great.
[45:37.000 --> 45:39.000]  I feel great.
[45:45.000 --> 45:47.000]  I like this.
[45:47.000 --> 45:49.000]  Do you like this?
[45:49.000 --> 45:51.000]  I like this.
[45:51.000 --> 45:53.000]  I like this.
[45:55.000 --> 45:57.000]  I want you to feel better.
[45:57.000 --> 45:59.000]  I want you to feel better.
[46:07.000 --> 46:09.000]  I want you to feel better.
[46:37.000 --> 46:39.000]  I want you to feel better.
[46:41.000 --> 46:43.000]  I can't do this.
[46:43.000 --> 46:45.000]  This?
[46:45.000 --> 46:47.000]  I can't do this.
[46:47.000 --> 46:49.000]  I can't do this.
[47:00.000 --> 47:02.000]  I can't do this.
[47:04.000 --> 47:06.000]  I can't do this.
[47:07.000 --> 47:09.000]  I can't do this.
[47:11.000 --> 47:13.000]  I want you to feel better.
[47:15.000 --> 47:17.000]  I want you to feel better.
[47:17.000 --> 47:19.000]  But...
[47:19.000 --> 47:21.000]  But what?
[47:27.000 --> 47:29.000]  And...
[47:29.000 --> 47:31.000]  You can't see the back of my body.
[47:31.000 --> 47:33.000]  You can't see the back of my body.
[47:37.000 --> 47:39.000]  You can't see the back of my body.
[48:07.000 --> 48:09.000]  You can do this a lot.
[48:27.000 --> 48:29.000]  You can do this a lot.
[48:37.000 --> 48:40.000]  Do you feel good?
[49:07.000 --> 49:09.000]  Do you feel good?
[49:11.000 --> 49:13.000]  Do you feel good?
[49:25.000 --> 49:27.000]  It's okay.
[49:27.000 --> 49:29.000]  It's okay.
[49:37.000 --> 49:39.000]  It's okay.
[49:39.000 --> 49:41.000]  It's okay.
[50:05.000 --> 50:07.000]  I want you to feel better.
[50:09.000 --> 50:11.000]  I want you to feel better.
[50:15.000 --> 50:17.000]  I want you to feel better.
[50:31.000 --> 50:33.000]  I can't do this.
[50:33.000 --> 50:35.000]  I can't do this.
[50:35.000 --> 50:37.000]  I can't do this.
[50:37.000 --> 50:45.000]  I want to go out and make a lot of noise.
[50:46.000 --> 50:52.000]  I want to make a lot of noise, too.
[50:53.000 --> 50:56.000]  Make a lot of noise? Okay.
[50:59.000 --> 51:01.000]  Make a lot of noise.
[51:07.000 --> 51:09.000]  Make a lot of noise.
[51:37.000 --> 51:39.000]  Make a lot of noise.
[51:46.000 --> 51:48.000]  Oh, my God.
[52:07.000 --> 52:15.000]  Make a lot of noise.
[52:16.000 --> 52:18.000]  Make a lot of noise.
[52:36.000 --> 52:38.000]  Make a lot of noise.
[52:45.000 --> 52:47.000]  Make a lot of noise.
[52:47.000 --> 52:49.000]  Make a lot of noise.
[53:12.000 --> 53:16.000]  I'm getting sleepy.
[53:17.000 --> 53:19.000]  You did your best.
[53:19.000 --> 53:21.000]  Good night.
[53:21.000 --> 53:23.000]  Good night.
[53:23.000 --> 53:25.000]  You can go to bed.
[53:40.000 --> 53:44.000]  I remember a lot of strange things.
[53:47.000 --> 53:50.000]  Good night.
[54:17.000 --> 54:19.000]  I'm getting sleepy.
[54:40.000 --> 54:42.000]  Are you free today?
[54:42.000 --> 54:45.000]  You have an important appointment today, right?
[54:45.000 --> 54:48.000]  I'm fine. I'm ready.
[54:49.000 --> 54:51.000]  I'm fine.
[55:12.000 --> 55:16.000]  I have something to do, so I'll be back.
[55:16.000 --> 55:18.000]  I don't want to.
[55:18.000 --> 55:20.000]  I want to drink more.
[55:20.000 --> 55:22.000]  I don't want to.
[55:22.000 --> 55:24.000]  I don't want to.
[55:24.000 --> 55:26.000]  I don't want to.
[55:47.000 --> 55:49.000]  It's almost time.
[55:51.000 --> 55:53.000]  Where are you going?
[55:53.000 --> 55:56.000]  I have an appointment with my friend.
[55:59.000 --> 56:01.000]  What kind of appointment?
[56:01.000 --> 56:02.000]  Date?
[56:02.000 --> 56:03.000]  It's not a date.
[56:03.000 --> 56:04.000]  I have a friend.
[56:04.000 --> 56:06.000]  Is he a man?
[56:06.000 --> 56:08.000]  I don't think so.
[56:08.000 --> 56:10.000]  Is he a woman?
[56:10.000 --> 56:12.000]  What's wrong with you?
[56:17.000 --> 56:19.000]  I don't have time.
[56:19.000 --> 56:21.000]  I don't have time.
[56:21.000 --> 56:23.000]  Your mother will come.
[56:26.000 --> 56:28.000]  I'll do it when I get home.
[56:35.000 --> 56:37.000]  I can't get ready.
[56:40.000 --> 56:42.000]  I'm tired.
[56:44.000 --> 56:46.000]  Let me get ready.
[56:50.000 --> 56:52.000]  Hey.
[56:54.000 --> 56:56.000]  I'll do it when I get home.
[57:01.000 --> 57:03.000]  Hey.
[57:04.000 --> 57:06.000]  My voice will come out.
[57:06.000 --> 57:08.000]  I'm not a man.
[57:08.000 --> 57:10.000]  I'm not a man.
[57:13.000 --> 57:15.000]  I have to get ready.
[57:19.000 --> 57:21.000]  I'm tired.
[57:31.000 --> 57:33.000]  Your mother will come.
[57:37.000 --> 57:39.000]  It's not a date.
[57:39.000 --> 57:41.000]  It's not a date.
[57:42.000 --> 57:44.000]  Why do you ask me that?
[57:44.000 --> 57:46.000]  Why do you ask me that?
[57:47.000 --> 57:49.000]  You're wearing makeup.
[57:50.000 --> 57:52.000]  It's not like that.
[57:55.000 --> 57:57.000]  What's wrong with you?
[58:00.000 --> 58:02.000]  Don't disturb me.
[58:10.000 --> 58:12.000]  Hey.
[58:14.000 --> 58:16.000]  Hey.
[58:20.000 --> 58:22.000]  Your mother will find out.
[58:22.000 --> 58:24.000]  It's not good.
[58:36.000 --> 58:38.000]  Let me get ready.
[58:38.000 --> 58:40.000]  I'll be late.
[58:41.000 --> 58:43.000]  Hey.
[58:43.000 --> 58:45.000]  It's against the rules.
[58:46.000 --> 58:48.000]  Your mother will find out.
[58:49.000 --> 58:51.000]  Hey.
[58:51.000 --> 58:53.000]  Hey.
[58:53.000 --> 58:55.000]  Hey.
[59:10.000 --> 59:12.000]  Hey.
[59:34.000 --> 59:36.000]  Why do you do that?
[59:41.000 --> 59:43.000]  Hey.
[59:43.000 --> 59:45.000]  Stop.
[59:46.000 --> 59:48.000]  It's not good.
[59:48.000 --> 59:50.000]  I'll be late.
[59:51.000 --> 59:53.000]  Hey.
[59:53.000 --> 59:55.000]  It's not good.
[59:55.000 --> 59:57.000]  I can't hold my voice.
[59:58.000 --> 01:00:00.000]  No.
[01:00:00.000 --> 01:00:02.000]  It's not good.
[01:00:12.000 --> 01:00:14.000]  It's not good.
[01:00:30.000 --> 01:00:32.000]  It's not good.
[01:00:32.000 --> 01:00:34.000]  Hey.
[01:00:34.000 --> 01:00:36.000]  Don't touch me.
[01:00:39.000 --> 01:00:41.000]  Hey.
[01:00:50.000 --> 01:00:52.000]  I'm coming.
[01:00:53.000 --> 01:00:55.000]  It's late. Are you okay?
[01:00:57.000 --> 01:00:59.000]  I'm okay.
[01:01:00.000 --> 01:01:02.000]  I'm sorry.
[01:01:11.000 --> 01:01:13.000]  What's wrong with you?
[01:01:14.000 --> 01:01:16.000]  What do you mean?
[01:01:16.000 --> 01:01:18.000]  Nothing.
[01:01:20.000 --> 01:01:22.000]  We played together, didn't we?
[01:01:22.000 --> 01:01:24.000]  But we're friends.
[01:01:27.000 --> 01:01:29.000]  We went on a date, didn't we?
[01:01:29.000 --> 01:01:31.000]  It wasn't a date.
[01:01:31.000 --> 01:01:33.000]  I wanted you to be my friend.
[01:01:35.000 --> 01:01:37.000]  What?
[01:01:37.000 --> 01:01:39.000]  Really?
[01:01:39.000 --> 01:01:41.000]  You were very fashionable.
[01:01:43.000 --> 01:01:45.000]  We haven't been friends for a long time.
[01:01:47.000 --> 01:01:49.000]  Not a man?
[01:01:49.000 --> 01:01:51.000]  A woman.
[01:01:51.000 --> 01:01:53.000]  I don't know.
[01:01:53.000 --> 01:01:55.000]  I only have you.
[01:02:00.000 --> 01:02:02.000]  Did you bake me a cake?
[01:02:02.000 --> 01:02:04.000]  No.
[01:02:04.000 --> 01:02:06.000]  Really?
[01:02:07.000 --> 01:02:09.000]  Yes.
[01:02:11.000 --> 01:02:13.000]  Are you sure?
[01:02:13.000 --> 01:02:15.000]  Yes, I'm sure.
[01:02:18.000 --> 01:02:20.000]  I'm sorry.
[01:02:21.000 --> 01:02:23.000]  I'll do it.
[01:02:23.000 --> 01:02:25.000]  Don't catch a cold.
[01:02:26.000 --> 01:02:28.000]  I'm okay.
[01:02:29.000 --> 01:02:31.000]  I'm sorry.
[01:02:31.000 --> 01:02:33.000]  It's all right.
[01:02:37.000 --> 01:02:39.000]  I'm sorry.
[01:02:43.000 --> 01:02:45.000]  You're cute.
[01:02:47.000 --> 01:02:49.000]  I'm sorry.
[01:02:49.000 --> 01:02:51.000]  I'm sorry.
[01:02:59.000 --> 01:03:01.000]  I'm sorry.
[01:03:17.000 --> 01:03:19.000]  This is a gift for you.
[01:03:19.000 --> 01:03:21.000]  So don't worry.
[01:03:21.000 --> 01:03:23.000]  I'm sorry to make you worry.
[01:03:23.000 --> 01:03:26.000]  You can do as you like.
[01:03:53.000 --> 01:03:55.000]  I'm sorry.
[01:04:09.000 --> 01:04:11.000]  It feels good.
[01:04:23.000 --> 01:04:25.000]  I'm sorry.
[01:04:53.000 --> 01:04:55.000]  I'm sorry.
[01:04:55.000 --> 01:04:57.000]  I'm sorry.
[01:05:22.000 --> 01:05:24.000]  You can breathe.
[01:05:25.000 --> 01:05:27.000]  It's just a breast.
[01:05:48.000 --> 01:05:50.000]  It feels good.
[01:05:55.000 --> 01:05:57.000]  It's just a breast.
[01:06:01.000 --> 01:06:03.000]  What?
[01:06:03.000 --> 01:06:05.000]  Look at me.
[01:06:15.000 --> 01:06:17.000]  You are a sweet boy.
[01:06:19.000 --> 01:06:21.000]  Yes, I am.
[01:06:25.000 --> 01:06:27.000]  It's just a breast.
[01:06:55.000 --> 01:06:57.000]  It's just a breast.
[01:07:01.000 --> 01:07:03.000]  It feels good.
[01:07:17.000 --> 01:07:19.000]  Hey, sis.
[01:07:19.000 --> 01:07:21.000]  What?
[01:07:21.000 --> 01:07:23.000]  I'll wash you.
[01:07:23.000 --> 01:07:25.000]  Are you going to wash me?
[01:07:25.000 --> 01:07:27.000]  Sit here.
[01:07:45.000 --> 01:07:47.000]  I'm embarrassed to wash you.
[01:07:53.000 --> 01:07:55.000]  I'll wash you.
[01:07:55.000 --> 01:07:57.000]  Can I wash you more?
[01:08:01.000 --> 01:08:03.000]  I often wash you.
[01:08:05.000 --> 01:08:07.000]  I didn't expect you to wash me.
[01:08:09.000 --> 01:08:11.000]  What's wrong?
[01:08:11.000 --> 01:08:13.000]  I want to do that today.
[01:08:23.000 --> 01:08:25.000]  I want to do that today.
[01:08:45.000 --> 01:08:47.000]  Don't you think it's a bad idea to wash me?
[01:08:47.000 --> 01:08:49.000]  I don't think so.
[01:08:49.000 --> 01:08:51.000]  You don't think so, do you?
[01:08:51.000 --> 01:08:53.000]  No.
[01:09:19.000 --> 01:09:21.000]  Yuzuru always attacks my nipples.
[01:09:21.000 --> 01:09:23.000]  Yuzuru always attacks my nipples.
[01:09:23.000 --> 01:09:25.000]  That's why I'm standing here.
[01:09:31.000 --> 01:09:33.000]  I have to wash your nipples.
[01:09:35.000 --> 01:09:37.000]  Where?
[01:09:37.000 --> 01:09:39.000]  I don't know.
[01:09:39.000 --> 01:09:41.000]  Does it feel good?
[01:09:41.000 --> 01:09:43.000]  It feels good.
[01:09:43.000 --> 01:09:45.000]  It feels good.
[01:09:45.000 --> 01:09:47.000]  But I don't want to wash your nipples.
[01:09:47.000 --> 01:09:49.000]  But I don't want to wash your nipples.
[01:09:49.000 --> 01:09:51.000]  That's not true.
[01:09:51.000 --> 01:09:53.000]  I don't want to wash your nipples.
[01:09:53.000 --> 01:09:55.000]  Where did you learn that?
[01:09:59.000 --> 01:10:01.000]  I'm just trying to be nice to you.
[01:10:01.000 --> 01:10:03.000]  Do you like my brush?
[01:10:11.000 --> 01:10:13.000]  Do you like my brush?
[01:10:19.000 --> 01:10:21.000]  I always wash your nipples.
[01:10:21.000 --> 01:10:23.000]  I always wash your nipples.
[01:10:23.000 --> 01:10:25.000]  I always wash your nipples.
[01:10:25.000 --> 01:10:27.000]  It's getting really close now.
[01:10:27.000 --> 01:10:29.000]  It's getting really close now.
[01:10:29.560 --> 01:10:30.560]  Here?
[01:10:34.340 --> 01:10:36.340]  It's ticklish isn't it?
[01:10:59.000 --> 01:11:01.000]  It feels good.
[01:11:29.000 --> 01:11:31.000]  Wow!
[01:11:31.000 --> 01:11:33.000]  It's clean.
[01:11:35.000 --> 01:11:38.000]  It's clean because I rubbed it a lot.
[01:11:39.000 --> 01:11:41.000]  I'll wash it.
[01:11:53.000 --> 01:11:55.000]  You look like an older brother.
[01:11:59.000 --> 01:12:01.000]  You look like an older brother.
[01:12:06.000 --> 01:12:08.000]  Do you want me to wash your hair?
[01:12:08.000 --> 01:12:09.000]  Yes.
[01:12:09.000 --> 01:12:11.000]  Really?
[01:12:11.000 --> 01:12:13.000]  I'll wash your hair.
[01:12:13.000 --> 01:12:15.000]  I'll wash your hair.
[01:12:29.000 --> 01:12:31.000]  Do you want me to wash your hair?
[01:12:31.000 --> 01:12:33.000]  Yes.
[01:13:00.000 --> 01:13:02.000]  Wow!
[01:13:02.000 --> 01:13:04.000]  It feels good.
[01:13:06.000 --> 01:13:08.000]  You look like you're in pain.
[01:13:10.000 --> 01:13:12.000]  Wow! It feels good.
[01:13:17.000 --> 01:13:19.000]  Hey, Yuzuru.
[01:13:19.000 --> 01:13:20.000]  Yes?
[01:13:20.000 --> 01:13:23.000]  Yuzuru cleaned your boobs.
[01:13:23.000 --> 01:13:25.000]  Yes.
[01:13:25.000 --> 01:13:28.000]  I'll massage your boobs with this.
[01:13:28.000 --> 01:13:30.000]  How?
[01:13:30.000 --> 01:13:32.000]  Like this.
[01:13:32.000 --> 01:13:34.000]  Wow!
[01:13:34.000 --> 01:13:37.000]  I'll massage your boobs with this.
[01:13:40.000 --> 01:13:43.000]  You'll be happy if I massage your boobs, right?
[01:13:43.000 --> 01:13:45.000]  Yes.
[01:13:59.000 --> 01:14:01.000]  Wow!
[01:14:01.000 --> 01:14:03.000]  Wow!
[01:14:27.000 --> 01:14:29.000]  I'll massage your boobs.
[01:14:32.000 --> 01:14:35.000]  Your boobs are rubbing against each other.
[01:14:35.000 --> 01:14:37.000]  Yes.
[01:14:37.000 --> 01:14:39.000]  It feels good.
[01:14:39.000 --> 01:14:41.000]  Does it feel good?
[01:14:41.000 --> 01:14:43.000]  Yes.
[01:14:53.000 --> 01:14:56.000]  I'll massage your hands.
[01:14:57.000 --> 01:14:59.000]  Wow!
[01:14:59.000 --> 01:15:01.000]  It feels good.
[01:15:21.000 --> 01:15:24.000]  I'll massage your neck, too.
[01:15:24.000 --> 01:15:26.000]  Is it okay?
[01:15:36.000 --> 01:15:38.000]  Wow! It feels good.
[01:15:38.000 --> 01:15:40.000]  Does it feel good?
[01:15:40.000 --> 01:15:42.000]  Yes.
[01:15:54.000 --> 01:15:56.000]  Wow!
[01:16:13.000 --> 01:16:15.000]  It feels good.
[01:16:24.000 --> 01:16:26.000]  Wow!
[01:16:32.000 --> 01:16:35.000]  My boobs are rubbing against each other.
[01:16:35.000 --> 01:16:37.000]  Yes.
[01:16:37.000 --> 01:16:39.000]  Wow!
[01:16:42.000 --> 01:16:46.000]  I'll massage your mouth, too.
[01:16:46.000 --> 01:16:49.000]  I want you to do that.
[01:16:55.000 --> 01:16:57.000]  Wow!
[01:16:57.000 --> 01:16:59.000]  It feels good.
[01:17:24.000 --> 01:17:27.000]  Wow!
[01:17:54.000 --> 01:17:56.000]  It feels good.
[01:18:03.000 --> 01:18:05.000]  It feels good.
[01:18:24.000 --> 01:18:26.000]  Oh, it's so good.
[01:18:26.000 --> 01:18:28.000]  Oh, it's so good.
[01:18:28.000 --> 01:18:30.000]  Oh, it's so good.
[01:18:30.000 --> 01:18:32.000]  Oh, it's so good.
[01:18:52.000 --> 01:18:54.000]  Do you want me to give you a massage?
[01:18:54.000 --> 01:18:56.000]  What?
[01:18:56.000 --> 01:18:58.000]  Do you want me to give you a massage?
[01:19:00.000 --> 01:19:02.000]  Do you want me to give you a massage?
[01:19:04.000 --> 01:19:06.000]  Do you want me to give you a massage?
[01:19:06.000 --> 01:19:08.000]  Do you want me to give you a massage?
[01:19:22.000 --> 01:19:24.000]  I'll give you a lot of massage.
[01:19:30.000 --> 01:19:32.000]  Oh, it's so good.
[01:19:50.000 --> 01:19:52.000]  Oh, it's so good.
[01:20:00.000 --> 01:20:02.000]  Oh, it's so good.
[01:20:08.000 --> 01:20:10.000]  Oh, it's so good.
[01:20:12.000 --> 01:20:14.000]  Oh, it's so good.
[01:20:30.000 --> 01:20:32.000]  Oh, it's so good.
[01:20:38.000 --> 01:20:40.000]  Oh, it's so good.
[01:20:40.000 --> 01:20:42.000]  Oh, it's so good.
[01:21:00.000 --> 01:21:02.000]  Oh, it's so good.
[01:21:02.000 --> 01:21:04.000]  Oh, it's so good.
[01:21:04.000 --> 01:21:06.000]  Oh, it's so good.
[01:21:28.000 --> 01:21:30.000]  I'm not back yet.
[01:21:30.000 --> 01:21:32.000]  I'm not back yet.
[01:21:34.000 --> 01:21:36.000]  I'm not back yet.
[01:21:46.000 --> 01:21:48.000]  Oh, it's so good.
[01:21:52.000 --> 01:21:54.000]  Oh, it's so good.
[01:22:04.000 --> 01:22:06.000]  Oh, it's so good.
[01:22:06.000 --> 01:22:08.000]  Oh, it's so good.
[01:22:10.000 --> 01:22:12.000]  Oh, it's so good.
[01:22:34.020 --> 01:22:35.020]  Come on.
[01:22:52.840 --> 01:22:54.260]  Thank you so much.
[01:23:04.000 --> 01:23:05.580]  It hurts.
[01:23:10.260 --> 01:23:11.600]  Definitely.
[01:23:16.340 --> 01:23:18.120]  It's still the same, right?
[01:23:21.320 --> 01:23:23.320] That feeling of it though?
[01:23:24.560 --> 01:23:25.540]  I'll do it.
[01:23:34.960 --> 01:23:38.400]  Wow, that's amazing!
[01:23:41.040 --> 01:23:42.720]  You can see inside it well, right?
[01:24:00.520 --> 01:24:02.560]  That feels good.
[01:24:04.000 --> 01:24:07.000]  Un, un
[01:24:07.000 --> 01:24:10.000]  Un, un
[01:24:10.000 --> 01:24:12.000]  Un, un
[01:24:12.000 --> 01:24:17.000]  Un, un
[01:24:17.000 --> 01:24:21.040]  Ah!
[01:24:21.040 --> 01:24:29.040]  Yes services
[01:24:29.040 --> 01:24:30.040]  Here?
[01:24:30.040 --> 01:24:31.040]  Yes
[01:24:36.040 --> 01:24:38.040]  Does it feel good here?
[01:24:38.040 --> 01:24:40.040]  Yes, I like it here
[01:24:48.040 --> 01:24:49.040]  It feels good
[01:24:56.040 --> 01:24:57.040]  It feels good
[01:25:00.040 --> 01:25:02.040]  Oh no, I can't do it
[01:25:26.040 --> 01:25:28.040]  I'll put some flour
[01:25:29.040 --> 01:25:30.040]  Oh no
[01:26:00.040 --> 01:26:02.040]  It feels good
[01:26:13.040 --> 01:26:15.040]  I'm going to go again
[01:26:18.040 --> 01:26:19.040]  No, I'm going
[01:26:29.040 --> 01:26:31.040]  Oh no, I can't do it
[01:26:34.040 --> 01:26:36.040]  Oh no, I can't do it
[01:26:40.040 --> 01:26:41.040]  Oh no
[01:26:55.040 --> 01:26:56.040]  Oh no
[01:26:59.040 --> 01:27:00.040]  Here?
[01:27:00.040 --> 01:27:01.040]  Yes
[01:27:01.040 --> 01:27:02.040]  Yes
[01:27:03.040 --> 01:27:04.040]  I'm going
[01:27:05.040 --> 01:27:06.040]  Oh no
[01:27:10.040 --> 01:27:11.040]  Oh no
[01:27:29.040 --> 01:27:31.040]  Oh no, I can't do it
[01:27:32.040 --> 01:27:34.040]  It feels good
[01:28:00.040 --> 01:28:01.040]  Oh no
[01:28:06.040 --> 01:28:07.040]  I can't do it
[01:28:15.040 --> 01:28:16.040]  I can't do it
[01:28:19.040 --> 01:28:20.040]  I can't do it
[01:28:23.040 --> 01:28:24.040]  I'm going
[01:28:29.040 --> 01:28:30.040]  I can't do it
[01:28:39.040 --> 01:28:40.040]  I can't do it
[01:29:00.040 --> 01:29:01.040]  Oh no
[01:29:05.040 --> 01:29:06.040]  I can't do it
[01:29:29.040 --> 01:29:30.040]  I can't do it
[01:29:45.040 --> 01:29:46.040]  I can't do it
[01:29:54.040 --> 01:29:55.040]  Oh no
[01:29:55.040 --> 01:29:56.040]  I can't do it
[01:29:57.040 --> 01:29:58.040]  I can't do it
[01:30:07.040 --> 01:30:08.040]  I can't do it
[01:30:27.040 --> 01:30:28.040]  Oh no
[01:30:40.040 --> 01:30:41.040]  I can't do it
[01:30:43.040 --> 01:30:44.040]  I can't do it
[01:30:46.040 --> 01:30:47.040]  I can't do it
[01:30:56.040 --> 01:30:57.080]  !!
[01:31:05.080 --> 01:31:06.460]  Hey,
[01:31:07.060 --> 01:31:09.060]  What are you doing?
[01:31:09.160 --> 01:31:11.200]  What are you doing?
[01:31:16.400 --> 01:31:18.800]  I'm coming for you
[01:31:18.860 --> 01:31:19.700]  What?
[01:31:26.040 --> 01:31:27.700]  I'm so happy
[01:31:51.660 --> 01:31:53.220]  Do you feel better now?
[01:31:53.480 --> 01:31:54.780]  Yeah, I do
[01:31:56.040 --> 01:31:58.040]  You're such a sweet potato.
[01:31:59.040 --> 01:32:01.040]  But I'm really happy.
[01:32:03.040 --> 01:32:04.040]  That's good.
[01:32:26.040 --> 01:32:44.040]  I heard you're late today.
[01:32:47.040 --> 01:32:48.040]  What's wrong?
[01:32:48.040 --> 01:33:01.040]  Can't I say I want to do it?
[01:33:02.040 --> 01:33:03.040]  No.
[01:33:03.040 --> 01:33:19.040]  You always make me feel good, so it's my turn today.
[01:33:24.040 --> 01:33:26.040]  You couldn't sleep today, could you?
[01:33:28.040 --> 01:33:29.040]  No way.
[01:33:33.040 --> 01:33:34.040]  I'm going to sleep.
[01:34:03.040 --> 01:34:04.040]  I'm going to sleep.
[01:34:33.040 --> 01:34:34.040]  I'm going to sleep.
[01:34:55.040 --> 01:34:58.040]  Talk to me as usual.
[01:35:03.040 --> 01:35:04.040]  I'm going to sleep.
[01:35:17.040 --> 01:35:21.040]  You were going to sleep, weren't you?
[01:35:29.040 --> 01:35:30.040]  I'm going to sleep.
[01:35:33.040 --> 01:35:34.040]  I'm going to sleep.
[01:35:34.040 --> 01:35:35.040]  I'm going to sleep.
[01:35:35.040 --> 01:35:36.040]  I'm going to sleep.
[01:35:36.040 --> 01:35:37.040]  I'm going to sleep.
[01:35:37.040 --> 01:35:38.040]  I'm going to sleep.
[01:36:03.040 --> 01:36:05.040]  I'm going to let you breathe.
[01:36:07.040 --> 01:36:08.040]  I'm going to let you breathe.
[01:36:16.040 --> 01:36:18.040]  So can I feel better?
[01:36:37.040 --> 01:36:38.040]  I'm going to kiss you.
[01:37:03.040 --> 01:37:05.040]  I'm going to kiss you, too.
[01:37:07.040 --> 01:37:08.040]  I'm going to kiss you.
[01:37:32.040 --> 01:37:33.040]  Don't you like to be licked?
[01:37:34.040 --> 01:37:35.040]  Do you like to be licked?
[01:37:35.040 --> 01:37:36.040]  Do you like it?
[01:37:36.040 --> 01:37:37.040]  I like it.
[01:37:46.040 --> 01:37:48.040]  Do you like to be licked and to be licked?
[01:37:49.040 --> 01:37:50.040]  I like it.
[01:37:51.040 --> 01:37:52.040]  You like boobs, don't you?
[01:37:53.040 --> 01:37:54.040]  Yes.
[01:38:05.040 --> 01:38:06.040]  I'm going to kiss you.
[01:38:36.040 --> 01:38:37.040]  I'm going to kiss you.
[01:38:49.040 --> 01:38:50.040]  You're getting bigger.
[01:39:05.040 --> 01:39:06.040]  I'm going to kiss you.
[01:39:22.040 --> 01:39:24.040]  It feels good to be close to you.
[01:39:35.040 --> 01:39:36.040]  I'm going to kiss you.
[01:40:05.040 --> 01:40:06.040]  I'm going to kiss you.
[01:40:35.040 --> 01:40:36.040]  I'm going to kiss you.
[01:41:05.040 --> 01:41:06.040]  I'm going to kiss you.
[01:41:36.040 --> 01:41:37.040]  It's amazing.
[01:41:39.040 --> 01:41:41.040]  You couldn't sleep because you were so sleepy?
[01:41:48.040 --> 01:41:50.040]  I couldn't sleep because I was sleepy, either.
[01:42:01.040 --> 01:42:02.040]  Let me see.
[01:42:05.040 --> 01:42:06.040]  I'm going to kiss you.
[01:42:35.040 --> 01:42:36.040]  I'm going to kiss you.
[01:43:03.040 --> 01:43:04.040]  It feels good.
[01:43:05.040 --> 01:43:06.040]  I'm going to kiss you.
[01:43:36.040 --> 01:43:37.040]  I'm going to kiss you.
[01:43:55.040 --> 01:43:56.040]  It feels good.
[01:44:05.040 --> 01:44:06.040]  I'm going to kiss you.
[01:44:20.040 --> 01:44:21.040]  It feels good.
[01:44:22.040 --> 01:44:23.040]  I'm going to kiss you.
[01:44:26.040 --> 01:44:27.040]  No.
[01:44:29.040 --> 01:44:30.040]  I'm going to kiss you.
[01:44:36.040 --> 01:44:37.040]  I'm going to kiss you.
[01:44:48.040 --> 01:44:49.040]  It feels good.
[01:45:05.040 --> 01:45:06.040]  I'm going to kiss you.
[01:45:31.040 --> 01:45:32.040]  It feels good.
[01:45:35.040 --> 01:45:36.040]  I'm going to kiss you.
[01:46:06.040 --> 01:46:07.040]  I'm going to kiss you.
[01:46:20.040 --> 01:46:21.040]  You want to be pinched, don't you?
[01:46:22.040 --> 01:46:23.040]  I want to be pinched.
[01:46:25.040 --> 01:46:26.040]  You love boobs, don't you?
[01:46:28.040 --> 01:46:29.040]  I love boobs.
[01:46:36.040 --> 01:46:37.040]  I'm going to kiss you.
[01:46:50.040 --> 01:46:51.040]  I'm going to kiss you.
[01:47:05.040 --> 01:47:06.040]  You love boobs, don't you?
[01:47:07.040 --> 01:47:08.040]  I love boobs.
[01:47:08.040 --> 01:47:09.040]  It's hot.
[01:47:31.040 --> 01:47:32.040]  Yuzuru's boobs are big, too.
[01:47:35.040 --> 01:47:36.040]  It's hot.
[01:47:38.040 --> 01:47:39.040]  It's hot.
[01:48:01.040 --> 01:48:02.040]  It feels good.
[01:48:08.040 --> 01:48:09.040]  I'm going to kiss you.
[01:48:38.040 --> 01:48:39.040]  It feels good.
[01:48:45.040 --> 01:48:46.040]  You want to be pinched, don't you?
[01:49:08.040 --> 01:49:09.040]  I'm going to kiss you.
[01:49:12.040 --> 01:49:13.040]  It feels good.
[01:49:19.040 --> 01:49:20.040]  It's hot.
[01:49:20.040 --> 01:49:21.040]  It's hot.
[01:49:34.040 --> 01:49:38.040]  Your boobs are getting bigger and bigger.
[01:49:39.040 --> 01:49:40.040]  It's amazing.
[01:49:51.040 --> 01:49:52.040]  It's hot.
[01:50:05.040 --> 01:50:06.040]  It's amazing.
[01:50:20.040 --> 01:50:21.040]  It's hot.
[01:50:42.040 --> 01:50:43.040]  Yuzuru.
[01:50:46.040 --> 01:50:48.040]  I want to go to your house.
[01:50:50.040 --> 01:50:51.040]  You don't want to?
[01:50:54.040 --> 01:50:55.040]  You want to, don't you?
[01:50:56.040 --> 01:50:57.040]  I want to.
[01:51:15.040 --> 01:51:16.040]  I'm going to kiss you.
[01:51:17.040 --> 01:51:18.040]  I'm going to kiss you.
[01:51:20.040 --> 01:51:21.040]  It's hot.
[01:51:50.040 --> 01:51:51.040]  It's hot.
[01:52:01.040 --> 01:52:02.040]  It feels good.
[01:52:03.040 --> 01:52:04.040]  It feels good.
[01:52:18.040 --> 01:52:19.040]  It feels good.
[01:52:20.040 --> 01:52:21.040]  It feels good.
[01:52:33.040 --> 01:52:34.040]  It feels good.
[01:52:40.040 --> 01:52:41.040]  It's amazing.
[01:52:46.040 --> 01:52:47.040]  It feels good.
[01:52:51.040 --> 01:52:52.040]  It's hot.
[01:53:01.040 --> 01:53:02.040]  It's amazing.
[01:53:05.040 --> 01:53:07.040]  Your waist is moving.
[01:53:08.040 --> 01:53:09.040]  It feels good.
[01:53:20.040 --> 01:53:22.040]  It's amazing.
[01:53:50.040 --> 01:53:51.040]  It feels good.
[01:54:00.040 --> 01:54:01.040]  It's amazing.
[01:54:20.040 --> 01:54:21.040]  It's hot.
[01:54:51.040 --> 01:54:52.040]  It's hot.
[01:54:54.040 --> 01:54:55.040]  It's hot.
[01:55:14.040 --> 01:55:15.040]  It's amazing.
[01:55:15.040 --> 01:55:16.040]  It's amazing.
[01:55:19.040 --> 01:55:20.040]  I can't do it.
[01:55:23.040 --> 01:55:24.040]  I can't do it.
[01:55:43.040 --> 01:55:44.040]  It's amazing.
[01:55:45.040 --> 01:55:46.040]  I can't do it.
[01:55:53.040 --> 01:55:54.040]  Yuzuru licked me.
[01:55:55.040 --> 01:55:56.040]  You're amazing.
[01:56:08.040 --> 01:56:09.040]  It feels good.
[01:56:13.040 --> 01:56:14.040]  I can't do it.
[01:56:15.040 --> 01:56:16.040]  I can't do it.
[01:56:24.040 --> 01:56:25.040]  It feels good.
[01:56:29.040 --> 01:56:30.040]  It feels good.
[01:56:45.040 --> 01:56:46.040]  It feels good.
[01:57:06.040 --> 01:57:07.040]  It feels good.
[01:57:13.040 --> 01:57:14.040]  It feels good.
[01:57:16.040 --> 01:57:17.040]  I can't do it.
[01:57:22.040 --> 01:57:23.040]  Why?
[01:57:24.040 --> 01:57:25.040]  You can't do it?
[01:57:26.040 --> 01:57:27.040]  I can't do it.
[01:57:28.040 --> 01:57:29.040]  It's okay.
[01:57:30.040 --> 01:57:32.040]  It's a safe day today.
[01:57:33.040 --> 01:57:34.040]  You can take it out.
[01:57:35.040 --> 01:57:36.040]  I can't do it.
[01:57:36.040 --> 01:57:37.040]  You don't want to do it?
[01:57:39.040 --> 01:57:40.040]  I can't do it.
[01:57:40.040 --> 01:57:41.040]  I can't do it.
[01:57:43.040 --> 01:57:46.040]  Don't you want to put milk in your sister?
[01:57:52.040 --> 01:57:54.040]  You want to do it, don't you?
[01:57:59.040 --> 01:58:00.040]  You can do it.
[01:58:00.040 --> 01:58:01.040]  I can't do it.
[01:58:09.040 --> 01:58:10.040]  I can't do it.
[01:58:11.040 --> 01:58:12.040]  It feels good.
[01:58:15.040 --> 01:58:16.040]  It's a safe day today.
[01:58:18.040 --> 01:58:19.040]  You can take it out.
[01:58:25.040 --> 01:58:26.040]  It feels good.
[01:58:31.040 --> 01:58:32.040]  I can't do it.
[01:58:36.040 --> 01:58:37.040]  Give me milk.
[01:58:38.040 --> 01:58:39.040]  I can't do it.
[01:58:46.040 --> 01:58:47.040]  You're amazing.
[01:59:01.040 --> 01:59:02.040]  Hey.
[01:59:04.040 --> 01:59:05.040]  You gave me milk.
[01:59:22.040 --> 01:59:23.040]  You're amazing.
[01:59:30.040 --> 01:59:31.040]  Regular milk is good.
[01:59:46.040 --> 01:59:47.040]  You can still do it, can't you?
[01:59:51.040 --> 01:59:52.040]  It's still hard.
[01:59:54.040 --> 01:59:55.040]  One more time?
[01:59:55.040 --> 01:59:56.040]  One more time.
[01:59:57.040 --> 01:59:58.040]  Don't you want to do it?
[01:59:58.040 --> 01:59:59.040]  You want to do it, don't you?
[01:59:59.040 --> 02:00:00.040]  I want to do it.
[02:00:07.040 --> 02:00:08.040]  Kiss me.
[02:00:13.040 --> 02:00:14.040]  It feels good.
[02:00:28.040 --> 02:00:29.040]  You can do it.
[02:00:34.040 --> 02:00:35.040]  You can do it.
[02:00:59.040 --> 02:01:00.040]  It feels good.
[02:01:13.040 --> 02:01:14.040]  You're amazing.
[02:01:17.040 --> 02:01:18.040]  It feels good.
[02:01:28.040 --> 02:01:29.040]  You can do it.
[02:01:51.040 --> 02:01:52.040]  You're amazing.
[02:01:56.040 --> 02:01:57.040]  It feels good.
[02:01:59.040 --> 02:02:00.040]  You're amazing.
[02:02:22.040 --> 02:02:23.040]  I can't do it.
[02:02:23.040 --> 02:02:24.040]  I can't do it.
[02:02:27.040 --> 02:02:28.040]  I can't do it.
[02:02:31.040 --> 02:02:32.040]  I can do it.
[02:02:53.040 --> 02:02:55.040]  You're amazing.
[02:03:23.040 --> 02:03:24.040]  You're amazing.
[02:03:28.040 --> 02:03:29.040]  You're amazing.
[02:03:46.040 --> 02:03:47.040]  It feels good.
[02:03:48.040 --> 02:03:49.040]  It feels good.
[02:03:49.040 --> 02:03:50.040]  You're amazing.
[02:03:53.040 --> 02:03:54.040]  You're amazing.
[02:03:55.040 --> 02:03:56.040]  You can do it.
[02:04:00.040 --> 02:04:01.040]  You can do it.
[02:04:11.040 --> 02:04:12.040]  You're amazing.
[02:04:14.040 --> 02:04:15.040]  It feels good.
[02:04:19.040 --> 02:04:20.040]  You can do it.
[02:04:24.040 --> 02:04:25.040]  You can do it.
[02:04:37.040 --> 02:04:38.040]  You can do it.
[02:04:41.040 --> 02:04:42.040]  Thank you.
[02:04:50.040 --> 02:04:51.040]  You're amazing.
[02:05:16.040 --> 02:05:17.040]  You're amazing.
[02:05:19.040 --> 02:05:20.040]  You're amazing.
[02:05:25.040 --> 02:05:26.040]  It feels good.
[02:05:29.040 --> 02:05:30.040]  It feels good.
[02:05:35.040 --> 02:05:37.040]  It's like I'm touching the earth.
[02:05:39.040 --> 02:05:41.040]  It's like I'm touching the earth.
[02:05:45.040 --> 02:05:46.040]  It feels good.
[02:05:47.040 --> 02:05:48.040]  I can't do it.
[02:05:49.040 --> 02:05:50.040]  You're amazing.
[02:05:53.040 --> 02:05:54.040]  I can't do it.
[02:05:57.040 --> 02:05:58.040]  I can't do it.
[02:06:17.040 --> 02:06:18.040]  I can't do it.
[02:06:42.040 --> 02:06:43.040]  I can't do it.
[02:06:47.040 --> 02:06:48.040]  It feels good.
[02:06:56.040 --> 02:06:57.040]  You can do it, right?
[02:07:17.040 --> 02:07:18.040]  It feels good.
[02:07:23.040 --> 02:07:24.040]  I can't do it.
[02:07:29.040 --> 02:07:30.040]  It feels good.
[02:07:33.040 --> 02:07:34.040]  I can't do it.
[02:07:46.040 --> 02:07:47.040]  I can't do it.
[02:08:16.040 --> 02:08:17.040]  I can't do it.
[02:08:23.040 --> 02:08:24.040]  Hey.
[02:08:25.040 --> 02:08:26.040]  What?
[02:08:28.040 --> 02:08:29.040]  It feels good.
[02:08:31.040 --> 02:08:32.040]  I want to do it again.
[02:08:33.040 --> 02:08:34.040]  It's okay.
[02:08:35.040 --> 02:08:36.040]  Give me more.
[02:08:37.040 --> 02:08:38.040]  Do you want me to do it again?
[02:08:38.040 --> 02:08:39.040]  Yes.
[02:08:41.040 --> 02:08:42.040]  I love you.
[02:08:43.040 --> 02:08:44.040]  Give me more.
[02:08:46.040 --> 02:08:47.040]  I can't do it.
[02:08:55.040 --> 02:08:56.040]  I can't do it.
[02:09:02.040 --> 02:09:03.040]  I can't do it.
[02:09:16.040 --> 02:09:17.040]  I can't do it.
[02:09:34.040 --> 02:09:35.040]  You're amazing.
[02:09:43.040 --> 02:09:44.040]  I made your bed dirty.
[02:09:46.040 --> 02:09:47.040]  I can't do it.
[02:09:51.040 --> 02:09:52.040]  I can't do it.
[02:10:16.040 --> 02:10:17.040]  I can't do it.
[02:10:46.040 --> 02:10:47.040]  I can't do it.
[02:11:16.040 --> 02:11:17.040]  I love you.
[02:11:22.040 --> 02:11:23.040]  It felt so good.
[02:11:24.040 --> 02:11:25.040]  I'm so happy.
[02:11:27.040 --> 02:11:28.040]  I'm so happy, too.
[02:11:34.040 --> 02:11:36.040]  I wish I could stay like this forever.
[02:11:39.040 --> 02:11:40.040]  You can stay like this forever.
[02:11:40.040 --> 02:11:41.040]  You can stay like this forever.
[02:11:42.040 --> 02:11:46.040]  When you like me, you can kiss my boobs.
[02:11:48.040 --> 02:11:50.040]  You can enjoy my boobs.
[02:12:00.040 --> 02:12:01.040]  I'm a strong woman.
[02:12:03.040 --> 02:12:06.040]  You keep giving me boobs.
[02:12:10.040 --> 02:12:17.040]  I can't live without your boobs.
[02:12:19.040 --> 02:12:21.040]  I'm sorry.
[02:12:23.040 --> 02:12:25.040]  Forgive me."""

# Split the input string into lines
lines = input_string.split('\n')

# Output file name
output_file = 'subtitles.srt'

# Open the output file in write mode
with open(output_file, 'w') as f:
    # Iterate through each line and extract timestamp and text
    for i, line in enumerate(lines):
        # Use regular expression to extract timestamp and text
        match = re.match(r'\[(\d+:\d+:\d+\.\d+) --> (\d+:\d+:\d+\.\d+)\]\s*(.+)', line)

        # If the match is found, create a proper subtitle string
        if match:
            start_time = match.group(1)
            end_time = match.group(2)
            text = match.group(3)

            # Create a proper subtitle string
            subtitle = f"{i + 1}\n{start_time} --> {end_time}\n{text}\n\n"

            # Write the result to the output file
            f.write(subtitle)

print(f'Subtitles have been written to {output_file}.')
