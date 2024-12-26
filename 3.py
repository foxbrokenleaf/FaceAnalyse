# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import cv2
import sys
from PIL import Image
import numpy
import os

from tkinter import filedialog

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"面部比例分析辅助程序", pos = wx.DefaultPosition, size = wx.Size( 827,530 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        # MainIcon = cv2.imread("./resource/Icon.png")
        filename = self.resource_path(os.path.join("resource","Icon.ico"))
        # self.SetIcon(wx.Icon(wx.Bitmap.FromBuffer(512, 512, cv2.cvtColor(MainIcon, cv2.COLOR_BGR2RGB))))
        self.SetIcon(wx.Icon(filename))

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.EmptyBitmap(width=400, height=500), wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_bitmap3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"实际矩形_上边"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_spinCtrl5 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, -40 )
        gSizer3.Add( self.m_spinCtrl5, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"实际矩形_下边"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        gSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_spinCtrl6 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, 8 )
        gSizer3.Add( self.m_spinCtrl6, 0, wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"实际矩形_左边"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        gSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_spinCtrl7 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, 20 )
        gSizer3.Add( self.m_spinCtrl7, 0, wx.ALL, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, _(u"实际矩形_右边"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        gSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_spinCtrl8 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, -13 )
        gSizer3.Add( self.m_spinCtrl8, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"预期矩形_上边"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        gSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_spinCtrl9 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, -40 )
        gSizer3.Add( self.m_spinCtrl9, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"预期矩形_下边"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        gSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_spinCtrl10 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, 8 )
        gSizer3.Add( self.m_spinCtrl10, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, _(u"预期矩形_左边"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        gSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.m_spinCtrl11 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, 23 )
        gSizer3.Add( self.m_spinCtrl11, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"预期矩形_右边"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        gSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

        self.m_spinCtrl12 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, -18 )
        gSizer3.Add( self.m_spinCtrl12, 0, wx.ALL, 5 )


        gbSizer1.Add( gSizer3, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, _(u"左眼外眼角"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        gSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )

        self.m_spinCtrl13 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, 41 )
        gSizer4.Add( self.m_spinCtrl13, 0, wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, _(u"左眼内眼角"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        gSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )

        self.m_spinCtrl14 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, 77 )
        gSizer4.Add( self.m_spinCtrl14, 0, wx.ALL, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, _(u"右眼外眼角"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        gSizer4.Add( self.m_staticText14, 0, wx.ALL, 5 )

        self.m_spinCtrl15 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, -36 )
        gSizer4.Add( self.m_spinCtrl15, 0, wx.ALL, 5 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, _(u"右眼内眼角"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )

        gSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )

        self.m_spinCtrl16 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, -71 )
        gSizer4.Add( self.m_spinCtrl16, 0, wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, _(u"左耳孔"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        gSizer4.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_spinCtrl17 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, 12 )
        gSizer4.Add( self.m_spinCtrl17, 0, wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, _(u"右耳孔"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        gSizer4.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_spinCtrl18 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, -2000, 2000, -3 )
        gSizer4.Add( self.m_spinCtrl18, 0, wx.ALL, 5 )


        gbSizer1.Add( gSizer4, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, _(u"脸宽=??"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText18.Wrap( -1 )

        bSizer3.Add( self.m_staticText18, 0, wx.ALL, 5 )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, _(u"脸长=??"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        bSizer3.Add( self.m_staticText19, 0, wx.ALL, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, _(u"左眼长=??"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        bSizer3.Add( self.m_staticText20, 0, wx.ALL, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, _(u"右眼长=??"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer3.Add( self.m_staticText21, 0, wx.ALL, 5 )

        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, _(u"左右耳间距=??\n预期长宽比例=??\n预期长宽比例=??"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        bSizer3.Add( self.m_staticText22, 0, wx.ALL, 5 )

        self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, _(u"显示实际矩形"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_checkBox1, 0, wx.ALL, 5 )

        self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, _(u"显示预期矩形"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_checkBox4, 0, wx.ALL, 5 )

        self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, _(u"显示三等分线"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_checkBox2, 0, wx.ALL, 5 )

        self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, _(u"显示五等分线-耳"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_checkBox3, 0, wx.ALL, 5 )

        self.m_checkBox8 = wx.CheckBox( self, wx.ID_ANY, _(u"显示五等分线-眼"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_checkBox8, 0, wx.ALL, 5 )

        self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, _(u"显示左眼参考线"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_checkBox5, 0, wx.ALL, 5 )

        self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, _(u"显示右眼参考线"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_checkBox6, 0, wx.ALL, 5 )

        self.m_checkBox7 = wx.CheckBox( self, wx.ID_ANY, _(u"显示左右耳间距\n参考线\n"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_checkBox7, 0, wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"选择人脸图片"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 1, wx.ALL|wx.EXPAND, 5 )

        gbSizer1.Add( bSizer3, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


        self.SetSizer( gbSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_spinCtrl5.Bind( wx.EVT_SPINCTRL, self.onReallyTopChange )
        self.m_spinCtrl6.Bind( wx.EVT_SPINCTRL, self.onReallyBottomChange )
        self.m_spinCtrl7.Bind( wx.EVT_SPINCTRL, self.onReallyRightChange )
        self.m_spinCtrl8.Bind( wx.EVT_SPINCTRL, self.onReallyLeftChange )
        self.m_spinCtrl9.Bind( wx.EVT_SPINCTRL, self.onWishTopChange )
        self.m_spinCtrl10.Bind( wx.EVT_SPINCTRL, self.onWishBottomChange )
        self.m_spinCtrl11.Bind( wx.EVT_SPINCTRL, self.onWishRightChange )
        self.m_spinCtrl12.Bind( wx.EVT_SPINCTRL, self.onWishLeftChange )
        self.m_spinCtrl13.Bind( wx.EVT_SPINCTRL, self.onRigthEyeOutsideChange )
        self.m_spinCtrl14.Bind( wx.EVT_SPINCTRL, self.onRigthEyeInsideChange )
        self.m_spinCtrl15.Bind( wx.EVT_SPINCTRL, self.onLeftEyeOutsideChange )
        self.m_spinCtrl16.Bind( wx.EVT_SPINCTRL, self.onLeftEyeInsideChange )
        self.m_spinCtrl17.Bind( wx.EVT_SPINCTRL, self.onRigthEarChange )
        self.m_spinCtrl18.Bind( wx.EVT_SPINCTRL, self.onLeftEarChange )
        self.m_spinCtrl5.Bind( wx.EVT_TEXT_ENTER, self.onReallyTopChange )
        self.m_spinCtrl6.Bind( wx.EVT_TEXT_ENTER, self.onReallyBottomChange )
        self.m_spinCtrl7.Bind( wx.EVT_TEXT_ENTER, self.onReallyRightChange )
        self.m_spinCtrl8.Bind( wx.EVT_TEXT_ENTER, self.onReallyLeftChange )
        self.m_spinCtrl9.Bind( wx.EVT_TEXT_ENTER, self.onWishTopChange )
        self.m_spinCtrl10.Bind( wx.EVT_TEXT_ENTER, self.onWishBottomChange )
        self.m_spinCtrl11.Bind( wx.EVT_TEXT_ENTER, self.onWishRightChange )
        self.m_spinCtrl12.Bind( wx.EVT_TEXT_ENTER, self.onWishLeftChange )
        self.m_spinCtrl13.Bind( wx.EVT_TEXT_ENTER, self.onRigthEyeOutsideChange )
        self.m_spinCtrl14.Bind( wx.EVT_TEXT_ENTER, self.onRigthEyeInsideChange )
        self.m_spinCtrl15.Bind( wx.EVT_TEXT_ENTER, self.onLeftEyeOutsideChange )
        self.m_spinCtrl16.Bind( wx.EVT_TEXT_ENTER, self.onLeftEyeInsideChange )
        self.m_spinCtrl17.Bind( wx.EVT_TEXT_ENTER, self.onRigthEarChange )
        self.m_spinCtrl18.Bind( wx.EVT_TEXT_ENTER, self.onLeftEarChange )        
        self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.onCheckReallyRect )
        self.m_checkBox4.Bind( wx.EVT_CHECKBOX, self.onCheckWishRect )
        self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.onCheck3Line )
        self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.onCheck5LineEar )
        self.m_checkBox8.Bind( wx.EVT_CHECKBOX, self.onCheck5LineEye )
        self.m_checkBox5.Bind( wx.EVT_CHECKBOX, self.onCheckRigthEye )
        self.m_checkBox6.Bind( wx.EVT_CHECKBOX, self.onCheckLeftEye )
        self.m_checkBox7.Bind( wx.EVT_CHECKBOX, self.onCheckEar )
        self.m_button1.Bind( wx.EVT_BUTTON, self.onClickbtn )
        self.Bind( wx.EVT_UPDATE_UI, self.drawUI)


        self.BackgroundColour = (255, 255, 255)

        self.Counter = 0
        self.ShowImage = any
        self.ReallyRectFlag = False
        self.WishRectFlag = False
        self.Check3Line = False
        self.Check5LineEar = False
        self.Check5LineEye = False
        self.CheckRigthEye = False
        self.CheckLeftEye = False
        self.CheckEar = False

        self.x_offset = self.m_spinCtrl7.GetValue()
        self.y_offset = self.m_spinCtrl5.GetValue()
        self.width_offset = self.m_spinCtrl8.GetValue()
        self.height_offset = self.m_spinCtrl6.GetValue()

        self.x_wish_offset = self.m_spinCtrl11.GetValue()
        self.y_wish_offset = self.m_spinCtrl9.GetValue()
        self.width_wish_offset = self.m_spinCtrl12.GetValue()
        self.height_wish_offset = self.m_spinCtrl10.GetValue()

        self.x_R_Eye_Outside_Offset = self.m_spinCtrl13.GetValue()
        self.x_R_Eye_Inside_Offset = self.m_spinCtrl14.GetValue()

        self.x_L_Eye_Outside_Offset = self.m_spinCtrl15.GetValue()
        self.x_L_Eye_Inside_Offset = self.m_spinCtrl16.GetValue()

        self.x_R_Ear_Offset = self.m_spinCtrl17.GetValue()
        self.x_L_Ear_Offset = self.m_spinCtrl18.GetValue()

        self.real_Height = 0
        self.real_width = 0
        self.to_Height = 0
        self.to_width = 0
        self.eye_len = 0
        self.eye_len_L = 0        
        self.ear_no_5 = 0
        self.ear_len = 0

        self.FilePath = any

        # self.drawOpencvImage()

    def resource_path( self, relative_path):
        if getattr(sys, 'frozen', False): #是否Bundle Resource
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)    

    def __del__( self ):
        pass

    def drawUI( self, event ):
        self.x_offset = self.m_spinCtrl7.GetValue()
        self.y_offset = self.m_spinCtrl5.GetValue()
        self.width_offset = self.m_spinCtrl8.GetValue()
        self.height_offset = self.m_spinCtrl6.GetValue()

        self.x_wish_offset = self.m_spinCtrl11.GetValue()
        self.y_wish_offset = self.m_spinCtrl9.GetValue()
        self.width_wish_offset = self.m_spinCtrl12.GetValue()
        self.height_wish_offset = self.m_spinCtrl10.GetValue()

        self.x_R_Eye_Outside_Offset = self.m_spinCtrl13.GetValue()
        self.x_R_Eye_Inside_Offset = self.m_spinCtrl14.GetValue()

        self.x_L_Eye_Outside_Offset = self.m_spinCtrl15.GetValue()
        self.x_L_Eye_Inside_Offset = self.m_spinCtrl16.GetValue()

        self.x_R_Ear_Offset = self.m_spinCtrl17.GetValue()
        self.x_L_Ear_Offset = self.m_spinCtrl18.GetValue()

        try:
            if (self.ShowImage.Size.width + 480) < 800 and self.ShowImage.Size.height + 50 < 500:
                self.Size = wx.Size(800, 500)
            else:
                self.Size = wx.Size(self.ShowImage.Size.width + 480, self.ShowImage.Size.height + 50)
        except AttributeError:
            self.Size = wx.Size(400 + 480, 500 + 50)

        event.Skip()

    def CatchUsbVideo( self, camera_idx, window_name = "Test"):
        # cv2.namedWindow(window_name)
        
        #视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
        # cap = cv2.VideoCapture(camera_idx)                
        
        #告诉OpenCV使用人脸识别分类器
        filename = self.resource_path(os.path.join("resource","haarcascade_frontalface_default.xml"))
        classfier = cv2.CascadeClassifier(filename=filename)
            
        frame = cv2.imread(self.FilePath,1)
        t_h, t_w = frame.shape[:2]
        bi_h = 482 / t_h
        bi_w = 344 / t_w
        frame = cv2.resize(frame, None, fx=bi_w, fy=bi_h, interpolation=cv2.INTER_CUBIC)

        #将当前帧转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(faceRects) > 0:            #大于0则检测到人脸                                   
            for faceRect in faceRects:  #单独框出每一张人脸
                x, y, w, h = faceRect
                # 左眼
                if self.CheckRigthEye:
                    cv2.line(frame, (x + self.x_R_Eye_Outside_Offset, y + self.y_offset), (x + self.x_R_Eye_Outside_Offset, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Eye_Inside_Offset, y + self.y_offset), (x + self.x_R_Eye_Inside_Offset, y + h + self.height_offset), (0, 255, 0), 1)
                    pass
                self.eye_len = (x + self.x_R_Eye_Inside_Offset) - (x + self.x_R_Eye_Outside_Offset)
                # 右眼 
                if self.CheckLeftEye:
                    cv2.line(frame, (x + w + self.x_L_Eye_Outside_Offset, y + self.y_offset), (x + w + self.x_L_Eye_Outside_Offset, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + w + self.x_L_Eye_Inside_Offset, y + self.y_offset), (x + w + self.x_L_Eye_Inside_Offset, y + h + self.height_offset), (0, 255, 0), 1)
                    pass
                self.eye_len_L = (x + w + self.x_L_Eye_Outside_Offset) - (x + w + self.x_L_Eye_Inside_Offset)
                # 左右耳
                if self.CheckEar:
                    cv2.line(frame, (x + self.x_R_Ear_Offset, y + self.y_offset), (x + self.x_R_Ear_Offset, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + w + self.x_L_Ear_Offset, y + self.y_offset), (x + w + self.x_L_Ear_Offset, y + h + self.height_offset), (0, 255, 0), 1)
                    pass
                self.ear_no_5 = (x + w + self.x_L_Ear_Offset) - (x + self.x_R_Ear_Offset)          
                #脸型
                if self.ReallyRectFlag:
                    #实际矩形长宽比例
                    cv2.rectangle(frame, (x + self.x_offset, y + self.y_offset), (x + w + self.width_offset, y + h + self.height_offset), (255, 255, 255), 1)
                self.real_width = (x + w + self.width_offset) - (x + self.x_offset)
                self.real_Height =  (y + h + self.height_offset) - (y + self.y_offset)
                print(f"实际矩形长宽比例 -> 长({self.real_Height}):宽({self.real_width})={self.real_Height / self.real_width}")
                #要达到的比例的范围
                if self.WishRectFlag:
                    cv2.rectangle(frame, (x + self.x_wish_offset, y + self.y_wish_offset), (x + w + self.width_wish_offset, y + h + self.height_wish_offset), (0, 255, 0), 1)
                self.to_width = (x + w + self.width_wish_offset) - (x + self.x_wish_offset)
                self.to_Height =  (y + h + self.height_wish_offset) - (y + self.y_wish_offset)
                print(f"要达到的比例的范围 -> 长({self.to_Height}):宽({self.to_width})={self.to_Height / self.to_width}")
                #要达到的比例的椭圆
                if self.WishRectFlag:                
                    cv2.ellipse(frame, ((x + self.x_wish_offset) + (self.to_width // 2), (y + self.y_wish_offset) + (self.to_Height // 2)), (self.to_width // 2, self.to_Height // 2), 0, 0, 360, (0, 255, 0), 1)

                #三庭五眼
                #三庭
                if self.Check3Line:
                    cv2.line(frame, (x + self.x_wish_offset, y + self.y_wish_offset + int(round(self.to_Height / 3,0))), (x + w + self.width_wish_offset, y + self.y_wish_offset + int(round(self.to_Height / 3,0))), (0, 255, 0),1)
                    cv2.line(frame, (x + self.x_wish_offset, y + self.y_wish_offset + int(round(self.to_Height / 3,0) * 2)), (x + w + self.width_wish_offset, y + self.y_wish_offset + int(round(self.to_Height / 3,0) * 2)), (0, 255, 0),1)
                #五眼
                # self.eye_len = (x + 20 - 2 + int(round(self.to_width / 5, 0) * 2)) - (x + 20 - 6 + int(round(self.to_width / 5, 0)))
                # self.ear_len = (x + 20 + 5 + int(round(self.to_width / 5, 0)) + self.eye_len * 4) - (x + 20 - 3 + int(round(self.to_width / 5, 0)) - self.eye_len)
                print(f"眼睛的长度={self.eye_len}\n两耳孔间的距离={self.ear_len}")
                # self.ear_no_5 = self.ear_len
                self.ear_len = self.ear_no_5 // 5
                print(f"两耳孔间的距离五等分={self.ear_len}")
                #根据左右耳孔长度五等份线
                if self.Check5LineEar:                    
                    cv2.line(frame, (x + self.x_R_Ear_Offset, y + self.y_offset), (x + self.x_R_Ear_Offset, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Ear_Offset + self.ear_len, y + self.y_offset), (x + self.x_R_Ear_Offset + self.ear_len, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Ear_Offset + self.ear_len * 2, y + self.y_offset), (x + self.x_R_Ear_Offset + self.ear_len * 2, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Ear_Offset + self.ear_len * 3, y + self.y_offset), (x + self.x_R_Ear_Offset + self.ear_len * 3, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Ear_Offset + self.ear_len * 4, y + self.y_offset), (x + self.x_R_Ear_Offset + self.ear_len * 4, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Ear_Offset + self.ear_len * 5, y + self.y_offset), (x + self.x_R_Ear_Offset + self.ear_len * 5, y + h + self.height_offset), (0, 255, 0), 1)
                #根据眼睛长度五等份线
                if self.Check5LineEye:
                    cv2.line(frame, (x + self.x_R_Eye_Outside_Offset - self.eye_len, y + self.y_offset), (x + self.x_R_Eye_Outside_Offset - self.eye_len, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Eye_Outside_Offset, y + self.y_offset), (x + self.x_R_Eye_Outside_Offset, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Eye_Outside_Offset + self.eye_len, y + self.y_offset), (x + self.x_R_Eye_Outside_Offset + self.eye_len, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Eye_Outside_Offset + self.eye_len * 2, y + self.y_offset), (x + self.x_R_Eye_Outside_Offset + self.eye_len * 2, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Eye_Outside_Offset + self.eye_len * 3, y + self.y_offset), (x + self.x_R_Eye_Outside_Offset + self.eye_len * 3, y + h + self.height_offset), (0, 255, 0), 1)
                    cv2.line(frame, (x + self.x_R_Eye_Outside_Offset + self.eye_len * 4, y + self.y_offset), (x + self.x_R_Eye_Outside_Offset + self.eye_len * 4, y + h + self.height_offset), (0, 255, 0), 1)

        h_temp, w_temp = frame.shape[:2]

        self.ShowImage = wx.Bitmap.FromBuffer(w_temp, h_temp, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        #显示图像
        # cv2.imshow(window_name, frame)        
        
        
        # cv2.imwrite("output.jpg", frame)
        # c = cv2.waitKey(0)
        # input()

        #释放摄像头并销毁所有窗口
        # frame.release()
        # cv2.destroyAllWindows() 

    def drawOpencvImage( self ):
        self.Counter += 1
        print(f"{self.Counter} Ok!")
        self.CatchUsbVideo(self.FilePath)

        self.m_staticText18.SetLabel(f"脸宽={self.real_width}")
        self.m_staticText19.SetLabel(f"脸长={self.real_Height}")
        self.m_staticText20.SetLabel(f"左眼长={self.eye_len}")
        self.m_staticText21.SetLabel(f"右眼长={self.eye_len_L}")
        if self.real_Height != 0:
            self.m_staticText22.SetLabel(f"左右耳间距={self.ear_no_5}\n实际长宽比例={round(self.real_Height / self.real_width,3)}\n预期长宽比例={round(self.to_Height / self.to_width,3)}")

        

        self.m_bitmap3.SetBitmap(self.ShowImage)
        pass

    # Virtual event handlers, override them in your derived class
    def onReallyTopChange( self, event ):
        self.y_offset = self.m_spinCtrl5.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onReallyBottomChange( self, event ):
        self.height_offset = self.m_spinCtrl6.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onReallyRightChange( self, event ):
        self.x_offset = self.m_spinCtrl7.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onReallyLeftChange( self, event ):
        self.width_offset = self.m_spinCtrl8.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onWishTopChange( self, event ):
        self.y_wish_offset = self.m_spinCtrl9.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onWishBottomChange( self, event ):
        self.height_wish_offset = self.m_spinCtrl10.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onWishRightChange( self, event ):
        self.x_wish_offset = self.m_spinCtrl11.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onWishLeftChange( self, event ):
        self.width_wish_offset = self.m_spinCtrl12.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onRigthEyeOutsideChange( self, event ):
        self.x_R_Eye_Outside_Offset = self.m_spinCtrl13.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onRigthEyeInsideChange( self, event ):
        self.x_R_Eye_Inside_Offset = self.m_spinCtrl14.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onLeftEyeOutsideChange( self, event ):
        self.x_L_Eye_Outside_Offset = self.m_spinCtrl15.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onLeftEyeInsideChange( self, event ):
        self.x_L_Eye_Inside_Offset = self.m_spinCtrl16.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onRigthEarChange( self, event ):
        self.x_R_Ear_Offset = self.m_spinCtrl17.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onLeftEarChange( self, event ):
        self.x_L_Ear_Offset = self.m_spinCtrl18.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onCheckReallyRect( self, event ):
        self.ReallyRectFlag = self.m_checkBox1.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onCheckWishRect( self, event ):
        self.WishRectFlag = self.m_checkBox4.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onCheck3Line( self, event ):
        self.Check3Line = self.m_checkBox2.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onCheck5LineEar( self, event ):
        self.Check5LineEar = self.m_checkBox3.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onCheck5LineEye( self, event ):
        self.Check5LineEye = self.m_checkBox8.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onCheckRigthEye( self, event ):
        self.CheckRigthEye = self.m_checkBox5.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onCheckLeftEye( self, event ):
        self.CheckLeftEye = self.m_checkBox6.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onCheckEar( self, event ):
        self.CheckEar = self.m_checkBox7.GetValue()
        self.drawOpencvImage()
        event.Skip()

    def onClickbtn( self, event ):
        self.FilePath = filedialog.askopenfilename()
        self.drawOpencvImage()
        event.Skip()

app = wx.App()
frame = MyFrame1(None)
frame.Show()
app.MainLoop()