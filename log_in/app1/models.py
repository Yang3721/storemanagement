

# Create your models here.
from django.db import models

# Create your models here.
# class User(models.Model):
# username = models.CharField(max_length=100)
# password = models.CharField(max_length=100, default='888888')


TYPE_CHOICES = (
    (u'通用测试设备', u'通用测试设备'),
    (u'机载测试设备', u'机载测试设备'),
    (u'改装装机设备', u'改装装机设备'),
    (u'一般耗材', u'一般耗材'),
    (u'电连接器', u'电连接器'),
    (u'改装标准件', u'改装标准件'),
    (u'非标件', u'非标件'),
    (u'成品线缆', u'成品线缆'),
    (u'系统物资', u'系统物资'),
)
STATE_CHOICES = (
    (u'在库', u'在库'),
    (u'出库', u'出库'),
    (u'送校', u'送校'),
    (u'故障', u'故障'),
    (u'停用', u'停用'),
)

STORAGEROOM_CHOICES = (
    (u'主库房', u'主库房'),
    (u'装机库房', u'装机库房'),
    (u'隔离库房', u'隔离库房'),
)


class Staff(models.Model):
    name = models.CharField('姓名', max_length=30)
    jobNum = models.CharField('工号', max_length=30)
    department = models.CharField('科室', max_length=30)
    email = models.EmailField('邮箱')
    tel = models.CharField('电话', max_length=30)
    password = models.CharField('密码', max_length=30, default='123456')
    remarks = models.TextField('备注', default=None)

    # class Materials(models.Model):
    # serial_number = models.CharField(max_length=100)
    # name = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)
    # model = models.CharField(max_length=100)
    # status = models.CharField(max_length=100)
    # number = models.IntegerField()
    # location = models.CharField(max_length=100)
    # comment = models.CharField(max_length=100)

class all_object(models.Model):
    name = models.CharField('物资名称', max_length=30)
    type = models.CharField('物资类型', max_length=30, choices=TYPE_CHOICES)
    modelNum = models.CharField('物资型号', max_length=30)
    roomNum = models.CharField('库房编号', max_length=30)
    state = models.CharField('库存状态', max_length=30, choices=STATE_CHOICES)
    number = models.CharField('库存数量', max_length=10)
    location = models.CharField('存放地点', max_length=100)
    department = models.CharField('维护科室', max_length=30)
    meteringNum = models.CharField('计量编号', max_length=30)
    useLife = models.CharField('有效期限', max_length=30)
    serialNum = models.CharField('出厂编号', max_length=30)
    countingUnit = models.CharField('计数单位', max_length=30)
    coreNum = models.CharField('芯数', max_length=10)
    measurement = models.CharField('度量单位', max_length=30)
    mountingNum = models.CharField('装机件号', max_length=30)
    threshold = models.CharField('阈值', max_length=10)  # 需要自己定义一个值
    remarks = models.TextField('备注')


class ReturnManagement(models.Model):
    formNum_de = models.CharField('出库单号', max_length=30)
    operator_re = models.CharField('还库经办人', max_length=30)
    deliveryDate = models.DateField('出库日期')
    returnDate = models.DateField('还库日期')
    type = models.CharField('出库物品类型',max_length=30,choices=TYPE_CHOICES)
    storageroom = models.CharField('所属库房',max_length=30,choices=STORAGEROOM_CHOICES)
    manager = models.CharField('库房管理员', max_length=30)
    materialName = models.CharField('物资名称', max_length=30)
    modelNum = models.CharField('物资型号', max_length=30)
    storoomNum = models.CharField('库房编号', max_length=30)
    returnState = models.CharField('还库品状态', max_length=30)
    attachState = models.CharField('附件状态', max_length=30)
    returnNum = models.CharField('还库数量/单位',max_length=30)
    remarks = models.TextField('备注')