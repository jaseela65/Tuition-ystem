from django import views
from django.urls import path
from.import views
#from dropdown import views

urlpatterns = [
    path('',views.home,name='home'),
    path('homes',views.homes,name='homes'),
    path('ajax/load_usn',views.load_usn,name='ajax/load_usn'),
    path('passwords',views.passwords,name='passwords'),
    path('passwordsm',views.passwordsm,name='passwordsm'),
    path('passwordss',views.passwordss,name='passwordss'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('userhome',views.userhome,name='userhome'),
    path('tcrhome',views.tcrhome,name='tcrhome'),
    path('signup_page',views.signup_page,name='signup_page'),
    path('tlogin',views.tlogin,name='tlogin'), 
    path('usercreate',views.usercreate,name='usercreate'),
    path('SLogin',views.SLogin,name='SLogin'),
    path('SLogout',views.SLogout,name='SLogout'),
    path('cls',views.cls,name='cls'),
    path('addcls',views.addcls,name='addcls'),
    path('sbjt',views.sbjt,name='sbjt'),
    path('addsbjt',views.addsbjt,name='addsbjt'),
    path('tcr',views.tcr,name='tcr'),
    path('addtcr',views.addtcr,name='addtcr'),
    path('showstd',views.showstd,name='showstd'),
    path('delstd/<int:id>',views.delstd,name='delstd'),
    path('showtcr',views.showtcr,name='showtcr'),
    path('ushowtcr',views.ushowtcr,name='ushowtcr'),
    path('deltcr/<int:id>',views.deltcr,name='deltcr'),
    path('stdProfile',views.stdProfile,name='stdProfile'),
    path('ttdProfile',views.ttdProfile,name='ttdProfile'),
    
    path('ats',views.ats,name='ats'),
    path('add_atns',views.add_atns,name='add_atns'),
    path('view_atns',views.view_atns,name='view_atns'),
    path('view_atnss',views.view_atnss,name='view_atnss'),

    path('pyd',views.pyd,name='pyd'),
    path('add_fee',views.add_fee,name='add_fee'),
    path('tsk',views.tsk,name='tsk'),
    path('add_tsk',views.add_tsk,name='add_tsk'),

    path('show_fee',views.show_fee,name='show_fee'),
    path('show_ctsk',views.show_ctsk,name='show_ctsk'),
    path('show_tsk',views.show_tsk,name='show_tsk'),
    path('show_updtsk',views.show_updtsk,name='show_updtsk'),
    path('vupdate_page/<int:id>',views.vupdate_page,name='vupdate_page'),
    path('vupdate_tsk/<int:id>',views.vupdate_tsk,name='vupdate_tsk'),
    
    path('update_page/<int:id>',views.update_page,name='update_page'),
    path('update_tsk/<int:id>',views.update_tsk,name='update_tsk'),
    path('edit_page',views.edit_page,name='edit_page'),
    path('edit_std_details',views.edit_std_details,name='edit_std_details'),
    path('tedit_page',views.tedit_page,name='tedit_page'),
    path('tedit_std_details',views.tedit_std_details,name='tedit_std_details'),
    
    path('leaves',views.leaves,name='leaves'),
    path('add_leave',views.add_leave,name='add_leave'),
    path('showleaves',views.showleaves,name='showleaves'),
    path('approve/<int:id>',views.approve,name='approve'),
    path('rjts/<int:id>',views.rjts,name='rjts'),
    path('showlst',views.showlst,name='showlst'),
    path('rslt_page',views.rslt_page,name='rslt_page'),
    path('reslt',views.reslt,name='reslt'),
    path('show_result',views.show_result,name='show_result'),
    path('approve_appointment/<int:pk>',views.approve_appointment,name='approve_appointment'),
    path('reject_appointment/<int:pk>',views.reject_appointment,name='reject_appointment'),
    path('del_lvs/<int:id>',views.del_lvs,name='del_lvs'),

]