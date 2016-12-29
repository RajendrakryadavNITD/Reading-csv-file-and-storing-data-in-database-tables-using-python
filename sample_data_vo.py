class SampleDataVo (object):
    def __init__(self):
        self._id=None
        self._id_number = None
        self._database_Category = None
        self._business_name = None
        self._add1 = None
        self._add2 = None
        self._locality = None
        self._town = None
        self._county = None
        self._postcode = None
        self._Area = None
        self._postcodearea = None
        self._postcodesubarea = None
        self._LineOfBusiness = None
        self._sicnumeric = None
        self._SIC_Description = None
        self._telephone = None
        self._tps = None
        self._fax = None
        self._fps = None
        self._employeesnumeric = None
        self._premises_type = None
        self._title1 = None
        self._fname1 = None
        self._sname1 = None
        self._position1 = None
        self._email = None
        self._Email_Address = None

    @property
    def id(self):
        self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def locality(self):
        self._locality

    @locality.setter
    def locality(self, value):
        self._locality = value

    @property
    def id_number(self):
        self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value

    @property
    def database_Category(self):
        self._database_Category

    @database_Category.setter
    def database_Category(self, value):
        self._database_Category = value

    @property
    def business_name(self):
        self._business_name

    @business_name.setter
    def business_name(self, value):
        self._business_name = value

    @property
    def add2(self):
        self._add2

    @add2.setter
    def add2(self, value):
        self._add2 = value

    @property
    def add1(self):
        self._add1

    @add1.setter
    def add1(self, value):
        self._add1 = value

    @property
    def town(self):
        self._town

    @town.setter
    def town(self, value):
        self._town = value

    @property
    def county(self):
        self._county

    @county.setter
    def county(self, value):
        self._county = value

    @property
    def postcode(self):
        self._postcode

    @postcode.setter
    def postcode(self, value):
        self._postcode = value

    @property
    def Area(self):
        self._Area

    @Area.setter
    def Area(self, value):
        self._Area = value

    @property
    def postcodearea(self):
        self._postcodearea

    @postcodearea.setter
    def postcodearea(self, value):
        self._postcodearea = value

    @property
    def postcodesubarea(self):
        self._postcodesubarea

    @postcodesubarea.setter
    def postcodesubarea(self, value):
        self._postcodesubarea = value

    @property
    def LineOfBusiness(self):
        self._LineOfBusiness

    @LineOfBusiness.setter
    def LineOfBusiness(self, value):
        self._LineOfBusiness = value

    @property
    def sicnumeric(self):
        self._sicnumeric

    @sicnumeric.setter
    def sicnumeric(self, value):
        self._sicnumeric = value

    @property
    def SIC_Description(self):
        self._SIC_Description

    @SIC_Description.setter
    def SIC_Description(self, value):
        self._SIC_Description = value

    @property
    def telephone(self):
        self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value

    @property
    def tps(self):
        self._tps

    @tps.setter
    def tps(self, value):
        self._tps = value

    @property
    def fax(self):
        self._fax

    @fax.setter
    def fax(self, value):
        self._fax = value

    @property
    def fps(self):
        self._fps

    @fps.setter
    def fps(self, value):
        self._fps = value

    @property
    def employeesnumeric(self):
        self._employeesnumeric

    @employeesnumeric.setter
    def employeesnumeric(self, value):
        self._employeesnumeric = value

    @property
    def premises_type(self):
        self._premises_type

    @premises_type.setter
    def premises_type(self, value):
        self._premises_type = value

    @property
    def title1(self):
        self._title1

    @title1.setter
    def title1(self, value):
        self._title1 = value

    @property
    def sname1(self):
        self._sname1

    @sname1.setter
    def sname1(self, value):
        self._sname1 = value

    @property
    def fname1(self):
        self._fname1

    @fname1.setter
    def fname1(self, value):
        self._fname1 = value

    @property
    def position1(self):
        self._position1

    @position1.setter
    def position1(self, value):
        self._position1 = value

    @property
    def email(self):
        self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def Email_Address(self):
        self._Email_Address

    @Email_Address.setter
    def Email_Address(self, value):
        self._Email_Address = value

    def serialize(self):
        d = dict()
        d['id'] = self._id
        d['id_number'] = self._id_number
        d['database_Category'] = self._database_Category
        d['business_name'] = self._business_name
        d['add1'] = self._add1
        d['add2'] = self._add2
        d['locality'] = self._locality
        d['town'] = self._town
        d['county'] = self._county
        d['postcode'] = self._postcode
        d['Area'] = self._Area
        d['postcodearea'] = self._postcodearea
        d['postcodesubarea'] = self._postcodesubarea
        d['LineOfBusiness'] = self._LineOfBusiness
        d['sicnumeric'] = self._sicnumeric
        d['SIC_Description'] = self._SIC_Description
        d['telephone'] = self._telephone
        d['tps'] = self._tps
        d['fax'] = self._fax
        d['fps'] = self._fps
        d['employeesnumeric'] = self._employeesnumeric
        d['premises_type'] = self._premises_type
        d['title1'] = self._title1
        d['fname1'] = self._fname1
        d['sname1'] = self._sname1
        d['position1'] = self._position1
        d['email'] = self._email
        d['Email_Address'] = self._Email_Address
        return d
