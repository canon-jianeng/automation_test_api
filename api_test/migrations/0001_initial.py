# Generated by Django 2.0.2 on 2020-03-18 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiGroupLevelFirst',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='接口一级分组名称')),
            ],
            options={
                'verbose_name': '接口分组',
                'verbose_name_plural': '接口分组',
            },
        ),
        migrations.CreateModel(
            name='ApiHead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024, verbose_name='标签')),
                ('value', models.CharField(blank=True, max_length=1024, null=True, verbose_name='内容')),
            ],
            options={
                'verbose_name': '请求头',
                'verbose_name_plural': '请求头管理',
            },
        ),
        migrations.CreateModel(
            name='ApiInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='接口名称')),
                ('httpType', models.CharField(choices=[('HTTP', 'HTTP'), ('HTTPS', 'HTTPS')], default='HTTP', max_length=50, verbose_name='http/https')),
                ('requestType', models.CharField(choices=[('POST', 'POST'), ('GET', 'GET'), ('PUT', 'PUT'), ('DELETE', 'DELETE')], max_length=50, verbose_name='请求方式')),
                ('apiAddress', models.CharField(max_length=1024, verbose_name='接口地址')),
                ('requestParameterType', models.CharField(choices=[('form-data', '表单(form-data)'), ('raw', '源数据(raw)'), ('Restful', 'Restful')], max_length=50, verbose_name='请求参数格式')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('mockStatus', models.BooleanField(default=False, verbose_name='mock状态')),
                ('mockCode', models.CharField(blank=True, choices=[('200', '200'), ('404', '404'), ('400', '400'), ('502', '502'), ('500', '500'), ('302', '302')], max_length=50, null=True, verbose_name='HTTP状态')),
                ('data', models.TextField(blank=True, null=True, verbose_name='mock内容')),
                ('lastUpdateTime', models.DateTimeField(auto_now=True, verbose_name='最近更新')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('apiGroupLevelFirst', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='First', to='api_test.ApiGroupLevelFirst', verbose_name='所属一级分组')),
            ],
            options={
                'verbose_name': '接口',
                'verbose_name_plural': '接口管理',
            },
        ),
        migrations.CreateModel(
            name='ApiOperationHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='操作内容')),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.ApiInfo', verbose_name='接口')),
                ('user', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户姓名')),
            ],
            options={
                'verbose_name': '接口操作历史',
                'verbose_name_plural': '接口操作历史',
            },
        ),
        migrations.CreateModel(
            name='ApiParameter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024, verbose_name='参数名')),
                ('_type', models.CharField(choices=[('Int', 'Int'), ('String', 'String')], default='String', max_length=1024, verbose_name='参数类型')),
                ('value', models.CharField(blank=True, max_length=1024, null=True, verbose_name='参数值')),
                ('required', models.BooleanField(default=True, verbose_name='是否必填')),
                ('restrict', models.CharField(blank=True, max_length=1024, null=True, verbose_name='输入限制')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestParameter', to='api_test.ApiInfo', verbose_name='所属接口')),
            ],
            options={
                'verbose_name': '请求参数',
                'verbose_name_plural': '请求参数管理',
            },
        ),
        migrations.CreateModel(
            name='ApiParameterRaw',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('api', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='requestParameterRaw', to='api_test.ApiInfo', verbose_name='所属接口')),
            ],
            options={
                'verbose_name': '请求参数Raw',
            },
        ),
        migrations.CreateModel(
            name='APIRequestHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('requestTime', models.DateTimeField(auto_now_add=True, verbose_name='请求时间')),
                ('requestType', models.CharField(max_length=50, verbose_name='请求方法')),
                ('requestAddress', models.CharField(max_length=1024, verbose_name='请求地址')),
                ('httpCode', models.CharField(max_length=50, verbose_name='HTTP状态')),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.ApiInfo', verbose_name='接口')),
            ],
            options={
                'verbose_name': '接口请求历史',
                'verbose_name_plural': '接口请求历史',
            },
        ),
        migrations.CreateModel(
            name='ApiResponse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024, verbose_name='参数名')),
                ('_type', models.CharField(choices=[('Int', 'Int'), ('String', 'String')], default='String', max_length=1024, verbose_name='参数类型')),
                ('value', models.CharField(blank=True, max_length=1024, null=True, verbose_name='参数值')),
                ('required', models.BooleanField(default=True, verbose_name='是否必含')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='api_test.ApiInfo', verbose_name='所属接口')),
            ],
            options={
                'verbose_name': '返回参数',
                'verbose_name_plural': '返回参数管理',
            },
        ),
        migrations.CreateModel(
            name='AutomationCaseApi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='接口名称')),
                ('httpType', models.CharField(choices=[('HTTP', 'HTTP'), ('HTTPS', 'HTTPS')], default='HTTP', max_length=50, verbose_name='HTTP/HTTPS')),
                ('requestType', models.CharField(choices=[('POST', 'POST'), ('GET', 'GET'), ('PUT', 'PUT'), ('DELETE', 'DELETE')], max_length=50, verbose_name='请求方式')),
                ('apiAddress', models.CharField(max_length=1024, verbose_name='接口地址')),
                ('requestParameterType', models.CharField(choices=[('form-data', '表单(form-data)'), ('raw', '源数据(raw)'), ('Restful', 'Restful')], max_length=50, verbose_name='参数请求格式')),
                ('formatRaw', models.BooleanField(default=False, verbose_name='是否转换成源数据')),
                ('examineType', models.CharField(choices=[('no_check', '不校验'), ('only_check_status', '校验http状态'), ('json', 'JSON校验'), ('entirely_check', '完全校验'), ('Regular_check', '正则校验')], default='no_check', max_length=50, verbose_name='校验方式')),
                ('httpCode', models.CharField(blank=True, choices=[('200', '200'), ('404', '404'), ('400', '400'), ('502', '502'), ('500', '500'), ('302', '302')], max_length=50, null=True, verbose_name='HTTP状态')),
                ('responseData', models.TextField(blank=True, null=True, verbose_name='返回内容')),
            ],
            options={
                'verbose_name': '用例接口',
                'verbose_name_plural': '用例接口管理',
            },
        ),
        migrations.CreateModel(
            name='AutomationCaseTestResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('header', models.CharField(blank=True, max_length=1024, null=True, verbose_name='请求头')),
                ('parameter', models.TextField(blank=True, null=True, verbose_name='请求参数')),
                ('result', models.CharField(choices=[('PASS', '成功'), ('FAIL', '失败')], max_length=50, verbose_name='测试结果')),
                ('httpStatus', models.CharField(blank=True, choices=[('200', '200'), ('404', '404'), ('400', '400'), ('502', '502'), ('500', '500'), ('302', '302')], max_length=50, null=True, verbose_name='http状态')),
                ('responseHeader', models.TextField(blank=True, null=True, verbose_name='返回头')),
                ('responseData', models.TextField(blank=True, null=True, verbose_name='实际返回内容')),
                ('testTime', models.CharField(blank=True, max_length=128, null=True, verbose_name='测试时间')),
                ('automationCaseApi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auto_result', to='api_test.AutomationCaseApi', verbose_name='接口')),
            ],
            options={
                'verbose_name': '自动测试结果',
                'verbose_name_plural': '自动测试结果管理',
            },
        ),
        migrations.CreateModel(
            name='AutomationGroupLevelFirst',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='用例一级分组')),
            ],
            options={
                'verbose_name': '用例分组',
                'verbose_name_plural': '用例分组管理',
            },
        ),
        migrations.CreateModel(
            name='AutomationHead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024, verbose_name='参数名')),
                ('value', models.CharField(max_length=1024, verbose_name='内容')),
                ('interrelate', models.BooleanField(default=False, verbose_name='是否关联')),
                ('automationCaseApi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='header', to='api_test.AutomationCaseApi', verbose_name='接口')),
            ],
            options={
                'verbose_name': '请求头',
                'verbose_name_plural': '请求头管理',
            },
        ),
        migrations.CreateModel(
            name='AutomationParameter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024, verbose_name='参数名')),
                ('value', models.CharField(blank=True, max_length=1024, null=True, verbose_name='内容')),
                ('interrelate', models.BooleanField(default=False, verbose_name='是否关联')),
                ('automationCaseApi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameterList', to='api_test.AutomationCaseApi', verbose_name='接口')),
            ],
            options={
                'verbose_name': '接口参数',
                'verbose_name_plural': '接口参数管理',
            },
        ),
        migrations.CreateModel(
            name='AutomationParameterRaw',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.TextField(blank=True, null=True, verbose_name='源数据请求参数')),
                ('automationCaseApi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parameterRaw', to='api_test.AutomationCaseApi', verbose_name='接口')),
            ],
            options={
                'verbose_name': '源数据参数',
                'verbose_name_plural': '源数据参数管理',
            },
        ),
        migrations.CreateModel(
            name='AutomationReportSendConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reportFrom', models.EmailField(blank=True, max_length=1024, null=True, verbose_name='发送人邮箱')),
                ('mailUser', models.CharField(blank=True, max_length=1024, null=True, verbose_name='用户名')),
                ('mailPass', models.CharField(blank=True, max_length=1024, null=True, verbose_name='口令')),
                ('mailSmtp', models.CharField(blank=True, max_length=1024, null=True, verbose_name='邮箱服务器')),
            ],
            options={
                'verbose_name': '邮件发送配置',
                'verbose_name_plural': '邮件发送配置',
            },
        ),
        migrations.CreateModel(
            name='AutomationResponseJson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=1024, null=True, verbose_name='JSON参数')),
                ('tier', models.CharField(blank=True, max_length=1024, null=True, verbose_name='层级关系')),
                ('type', models.CharField(choices=[('json', 'json'), ('Regular', 'Regular')], default='json', max_length=1024, verbose_name='关联类型')),
                ('automationCaseApi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='api_test.AutomationCaseApi', verbose_name='接口')),
            ],
            options={
                'verbose_name': '结果JSON参数',
                'verbose_name_plural': '结果JSON参数管理',
            },
        ),
        migrations.CreateModel(
            name='AutomationTaskRunTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('startTime', models.CharField(max_length=50, verbose_name='开始时间')),
                ('host', models.CharField(blank=True, max_length=1024, null=True, verbose_name='测试地址')),
                ('elapsedTime', models.CharField(max_length=50, verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '用例任务执行时间',
                'verbose_name_plural': '用例任务执行时间',
            },
        ),
        migrations.CreateModel(
            name='AutomationTestCase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('caseName', models.CharField(max_length=50, verbose_name='用例名称')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('automationGroupLevelFirst', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='automationGroup', to='api_test.AutomationGroupLevelFirst', verbose_name='所属用例一级分组')),
            ],
            options={
                'verbose_name': '自动化测试用例',
                'verbose_name_plural': '自动化测试用例',
            },
        ),
        migrations.CreateModel(
            name='AutomationTestResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=1024, verbose_name='请求地址')),
                ('requestType', models.CharField(choices=[('POST', 'POST'), ('GET', 'GET'), ('PUT', 'PUT'), ('DELETE', 'DELETE')], max_length=1024, verbose_name='请求方式')),
                ('host', models.CharField(blank=True, max_length=1024, null=True, verbose_name='测试地址')),
                ('header', models.CharField(blank=True, max_length=1024, null=True, verbose_name='请求头')),
                ('parameter', models.TextField(blank=True, null=True, verbose_name='请求参数')),
                ('statusCode', models.CharField(blank=True, choices=[('200', '200'), ('404', '404'), ('400', '400'), ('502', '502'), ('500', '500'), ('302', '302')], max_length=1024, null=True, verbose_name='期望HTTP状态')),
                ('examineType', models.CharField(max_length=1024, verbose_name='匹配规则')),
                ('data', models.TextField(blank=True, null=True, verbose_name='规则内容')),
                ('result', models.CharField(choices=[('PASS', '成功'), ('FAIL', '失败')], max_length=50, verbose_name='测试结果')),
                ('httpStatus', models.CharField(blank=True, choices=[('200', '200'), ('404', '404'), ('400', '400'), ('502', '502'), ('500', '500'), ('302', '302')], max_length=50, null=True, verbose_name='http状态')),
                ('responseData', models.TextField(blank=True, null=True, verbose_name='实际返回内容')),
                ('testTime', models.DateTimeField(auto_now_add=True, verbose_name='测试时间')),
                ('automationCaseApi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='test_result', to='api_test.AutomationCaseApi', verbose_name='接口')),
            ],
            options={
                'verbose_name': '手动测试结果',
                'verbose_name_plural': '手动测试结果管理',
            },
        ),
        migrations.CreateModel(
            name='AutomationTestTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='任务名称')),
                ('type', models.CharField(choices=[('circulation', '循环'), ('timing', '定时')], max_length=50, verbose_name='类型')),
                ('frequency', models.IntegerField(blank=True, null=True, verbose_name='间隔')),
                ('unit', models.CharField(blank=True, choices=[('m', '分'), ('h', '时'), ('d', '天'), ('w', '周')], max_length=50, null=True, verbose_name='单位')),
                ('startTime', models.DateTimeField(max_length=50, verbose_name='开始时间')),
                ('endTime', models.DateTimeField(max_length=50, verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '用例定时任务',
                'verbose_name_plural': '用例定时任务管理',
            },
        ),
        migrations.CreateModel(
            name='CustomMethod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='方法名')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('type', models.CharField(max_length=50, verbose_name='类型')),
                ('dataCode', models.TextField(verbose_name='代码')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '自定义方法',
                'verbose_name_plural': '自定义方法',
            },
        ),
        migrations.CreateModel(
            name='GlobalHost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('host', models.CharField(max_length=1024, verbose_name='Host地址')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': 'HOST',
                'verbose_name_plural': 'HOST管理',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='项目名称')),
                ('version', models.CharField(max_length=50, verbose_name='版本')),
                ('type', models.CharField(choices=[('Web', 'Web'), ('App', 'App')], max_length=50, verbose_name='类型')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('LastUpdateTime', models.DateTimeField(auto_now=True, verbose_name='最近修改时间')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(max_length=1024, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.CreateModel(
            name='ProjectDynamic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(max_length=128, verbose_name='操作时间')),
                ('type', models.CharField(max_length=50, verbose_name='操作类型')),
                ('operationObject', models.CharField(max_length=50, verbose_name='操作对象')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='描述')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dynamic_project', to='api_test.Project', verbose_name='所属项目')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userName', to=settings.AUTH_USER_MODEL, verbose_name='操作人')),
            ],
            options={
                'verbose_name': '项目动态',
                'verbose_name_plural': '项目动态',
            },
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('permissionType', models.CharField(choices=[('超级管理员', '超级管理员'), ('开发人员', '开发人员'), ('测试人员', '测试人员')], max_length=50, verbose_name='权限角色')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_project', to='api_test.Project', verbose_name='所属项目')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_user', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '项目成员',
                'verbose_name_plural': '项目成员',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='无', max_length=11, verbose_name='手机号')),
                ('openId', models.CharField(default=0, max_length=50, verbose_name='唯一标识')),
                ('unionid', models.CharField(default=0, max_length=50, verbose_name='企业内唯一标识')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='VisitorsRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('formattedAddress', models.CharField(blank=True, max_length=1024, null=True, verbose_name='访客地址')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='国家')),
                ('province', models.CharField(blank=True, max_length=50, null=True, verbose_name='省份')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='城市')),
                ('district', models.CharField(blank=True, max_length=50, null=True, verbose_name='县级')),
                ('township', models.CharField(blank=True, max_length=50, null=True, verbose_name='镇')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='街道')),
                ('number', models.CharField(blank=True, max_length=50, null=True, verbose_name='门牌号')),
                ('success', models.CharField(blank=True, max_length=50, null=True, verbose_name='成功')),
                ('reason', models.CharField(blank=True, max_length=1024, null=True, verbose_name='原因')),
                ('callTime', models.DateTimeField(auto_now_add=True, verbose_name='访问时间')),
            ],
            options={
                'verbose_name': '访客',
                'verbose_name_plural': '访客查看',
            },
        ),
        migrations.AddField(
            model_name='globalhost',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='custommethod',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='automationtesttask',
            name='Host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.GlobalHost', verbose_name='HOST'),
        ),
        migrations.AddField(
            model_name='automationtesttask',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='automationtestcase',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='所属项目'),
        ),
        migrations.AddField(
            model_name='automationtestcase',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createUser', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AddField(
            model_name='automationtaskruntime',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='automationreportsendconfig',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='automationgrouplevelfirst',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='automationcaseapi',
            name='automationTestCase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api', to='api_test.AutomationTestCase', verbose_name='用例'),
        ),
        migrations.AddField(
            model_name='apiinfo',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_project', to='api_test.Project', verbose_name='所属项目'),
        ),
        migrations.AddField(
            model_name='apiinfo',
            name='userUpdate',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ApiUpdateUser', to=settings.AUTH_USER_MODEL, verbose_name='更新人'),
        ),
        migrations.AddField(
            model_name='apihead',
            name='api',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='headers', to='api_test.ApiInfo', verbose_name='所属接口'),
        ),
        migrations.AddField(
            model_name='apigrouplevelfirst',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_test.Project', verbose_name='项目'),
        ),
    ]
