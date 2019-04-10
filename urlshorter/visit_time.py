from .models import *


def visit_time(request):
    count_nums = VisitNumber.objects.filter(id=1)
    if count_nums:  #判断记录是否存在
        count_nums = count_nums[0]
        count_nums.count += 1
    else:
        count_nums = VisitNumber()
        count_nums.count = 1
    count_nums.save()

    if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # 所以这里是真实的ip
    else:
        client_ip = request.META['REMOTE_ADDR']  # 这里获得代理ip

    ip_exist = IpVisitNumber.objects.filter(ip=str(client_ip))
    if ip_exist:  # 判断ip是否存在
        ivn_nums = ip_exist[0]
        ivn_nums.count += 1
    else:
        ivn_nums = IpVisitNumber()
        ivn_nums.ip = client_ip
        ivn_nums.count = 1
        ivn_nums.save()

