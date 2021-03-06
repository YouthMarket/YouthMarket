# Generated by Django 3.2.13 on 2022-07-16 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('idx', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idx')),
                ('category', models.CharField(max_length=10, verbose_name='카테고리명')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('idx', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idx')),
                ('schoolIdx', models.IntegerField(verbose_name='학교idx')),
                ('userId', models.CharField(max_length=50, verbose_name='사용자id')),
                ('userPw', models.CharField(max_length=256, verbose_name='사용자pw')),
                ('userName', models.CharField(max_length=10, verbose_name='사용자이름')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users', verbose_name='이미지경로')),
                ('addrCode', models.CharField(max_length=256, verbose_name='우편번호')),
                ('addr', models.CharField(max_length=256, verbose_name='집주소')),
                ('detailAddr', models.CharField(max_length=256, verbose_name='상세주소')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('updatedDate', models.DateTimeField(blank=True, null=True, verbose_name='수정시간')),
                ('status', models.BooleanField(default=False, verbose_name='상태')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('idx', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idx')),
                ('title', models.CharField(max_length=256, verbose_name='제목')),
                ('text', models.TextField(verbose_name='내용')),
                ('price', models.CharField(max_length=10, verbose_name='금액')),
                ('count', models.IntegerField(verbose_name='방문자 수')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='posts')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('updatedDate', models.DateTimeField(blank=True, null=True, verbose_name='수정시간')),
                ('status', models.BooleanField(default=True, verbose_name='상태')),
                ('categoryIdx', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='post.category', verbose_name='카테고리idx')),
                ('sellerIdx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.user', verbose_name='판매자idx')),
            ],
        ),
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('idx', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idx')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('updatedDate', models.DateTimeField(blank=True, null=True, verbose_name='수정시간')),
                ('status', models.BooleanField(default=False, verbose_name='상태')),
                ('postIdx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='게시글idx')),
                ('userIdx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.user', verbose_name='사용자idx')),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('idx', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idx')),
                ('sellerIdx', models.IntegerField(verbose_name='판매자idx')),
                ('message', models.JSONField(verbose_name='메시지내용')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('updatedDate', models.DateTimeField(blank=True, null=True, verbose_name='수정시간')),
                ('status', models.BooleanField(default=True, verbose_name='상태')),
                ('buyerIdx', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='post.user', verbose_name='방만든이idx')),
                ('postIdx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='게시글idx')),
            ],
        ),
    ]
