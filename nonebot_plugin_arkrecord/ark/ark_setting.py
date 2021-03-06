import sqlite3 as sq, os
from .ark_utils import *
from .ark_style import *

#包根目录
package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#资源目录
resource_dir = os.path.join(package_dir, 'resource')
#sqlite文件
arkgacha_db_path = os.path.join(resource_dir, "arkgacha_record.db")
arkgacha_db = sq.connect(arkgacha_db_path)

#干员头像目录
operator_profile_dir = os.path.join(resource_dir, 'profile')

def get_tot_pool_info(pool_name_file):
    with open(pool_name_file, 'r', encoding='utf-8') as f:
        tmp_json = json.load(f)
    return tmp_json

#卡池信息
tot_pool_info_file = os.path.join(resource_dir, 'pool_info.json')
tot_pool_info = get_tot_pool_info(tot_pool_info_file)

#字体路径
ark_text_font_path = os.path.join(resource_dir,'ttf/LXGW-Regular.ttf')
ark_title_font_path = os.path.join(resource_dir,'ttf/hkljh.TTF')


#资源图像目录
image_dir = os.path.join(resource_dir, 'images')
#顶部路径
title_img_path = os.path.join(image_dir, "titleimage.png")
#帮助图像
help_img_path = os.path.join(image_dir, "ark_help.png")
#底部图像
bottom_img_path = os.path.join(image_dir, 'bottom.png')
#六星渐变图像
rainbow_img_path = os.path.join(image_dir, 'rainbow.png')


#结果目录
res_dir = os.path.join(package_dir, 'res_file')
if not os.path.exists(res_dir):os.makedirs(res_dir)

#结果图像目录
record_img_dir = os.path.join(res_dir, 'record_image')
if not os.path.exists(record_img_dir):os.makedirs(record_img_dir)

output_csv_dir = os.path.join(res_dir, 'output_csv')
if not os.path.exists(output_csv_dir):os.makedirs(output_csv_dir)

"""数据库表、字段名称 以后可能改成字典"""
"""
qq_user
"""
qq_user_table = 'qq_user'
qq_id_field = 'qq_id'
user_id_field = 'user_id'
user_name_field = 'user_name'
ark_token_field = 'ark_token'
channel_field = "channel"
""" 
ark_record
"""
ark_record_table = 'ark_record'
record_id_field = 'record_id'
pool_name_field = 'pool_name'
char_name_field = 'char_name'
star_field = 'star'
is_new_field = 'is_new'
timestamp_field = 'ts'
exclusive_field = 'exclusive_type'
exclusive_common_name = '常规up池'


max_char_count = 20 #最多显示几个新角色/6星角色信息
max_pool_count = 8  #最多显示几个卡池信息



