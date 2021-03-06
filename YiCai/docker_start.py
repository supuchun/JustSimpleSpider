'''
参考： https://docker-py.readthedocs.io/en/stable/index.html
安装： pip install docker



'''
import json
import pprint
import sys
import threading
import time
import docker


def create_docker_client():
    # 创建 docker python 客户端
    # docker_client = docker.from_env()
    docker_client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    docker_version_info = docker_client.version()
    # 查看 docker 的版本信息
    # print(pprint.pformat(docker_version_info))
    # 查看 docker 的内存占用信息
    docker_df_info = docker_client.df()
    # print(pprint.pformat(docker_df_info))
    docker_info = docker_client.info()
    # print(pprint.pformat(docker_info))
    # 登录
    '''
    username (str) – The registry username
    password (str) – The plaintext password
    email (str) – The email for the registry account
    registry (str) – URL to the registry. E.g. https://index.docker.io/v1/
    reauth (bool) – Whether or not to refresh existing authentication on the Docker server.
    dockercfg_path (str) – Use a custom path for the Docker config file (default $HOME/.docker/config.json if present, otherwise``$HOME/.dockercfg``)
    '''
    # login_info = {
    #     "username": "",
    #     "password": '',
    #     "registry": 'registry.cn-shenzhen.aliyuncs.com',
    # }
    # login_resp = docker_client.login(**login_info)
    # print(login_resp)   # {'IdentityToken': '', 'Status': 'Login Succeeded'}


def monite_docker_events():
    docker_client = docker.from_env()
    docker_events = docker_client.events()

    def monitor():
        for event in docker_events:
            event_info = json.loads(event.decode())
            print(pprint.pformat(event_info))

    # 在其他线程中进行关闭
    threading.Thread(target=monitor).start()
    time.sleep(50)
    docker_events.close()


def docker_containers_test():
    docker_client = docker.from_env()
    # 创建一个容器管理器对象
    docker_containers_col = docker_client.containers
    # 查看当前运行容器的列表
    containers = docker_containers_col.list()
    # 查看全部的容器列表
    all_containers = docker_containers_col.list(all=True)
    # print(all_containers)

    # 使用容器管理器运行起一个镜像 最简单的阻塞模式的
    # docker_containers_col.run("c39ad7322e", 'python SpidersSchedule/main_switch.py')
    # 对于运行起一个镜像添加更多的参数
    # 以守护进程的方式执行
    '''
    sudo docker run --log-opt max-size=10m --log-opt max-file=3 -itd \
        --env LOCAL=0 \
        --name spi_all \
        registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/spi:v1 \
        python SpidersSchedule/main_switch.py 
    '''
    # ret = docker_containers_col.run(
    #     "registry.cn-shenzhen.aliyuncs.com/jzdev/jzdata/spi:v1",
    #     environment={"LOCAL": 1},
    #     name='spi_test',
    #     command='python SpidersSchedule/main_switch.py',
    #     detach=True,
    # )
    # # 只能启动一次 无法重复启动
    # print(ret)

    one_container = docker_containers_col.get("test_spi")
    # print(one_container)
    # 针对单个容器的操作
    one_container_attrs = one_container.attrs
    # print(pprint.pformat(one_container_attrs))
    its_image = one_container_attrs['Config']['Image']
    # print(its_image)
    # 查看容器的日志
    # one_container_logs = one_container.logs()
    # print(one_container_logs.decode())
    # 查看容器的 id
    print(one_container.id)
    # 容器的镜像
    print(one_container.image)
    print(one_container.labels)
    # 容器的名称
    print(one_container.name)
    print(one_container.short_id)
    print(one_container.status)

    print(one_container.start())
    print(one_container.top())
    print(one_container.stop())
    print(one_container.restart())

    # print(one_container.rename("test_spi"))


def docker_prune_test():
    # 删除不再运行的容器
    docker_client = docker.from_env()
    coll = docker_client.containers
    coll.prune()


def docker_images_test():
    docker_client = docker.from_env()
    docker_images_col = docker_client.images
    # print(docker_images_col)
    # docker_images = docker_images_col.list(all=True)
    docker_images = docker_images_col.list()
    # print(len(docker_images))

    pass


# monite_docker_events()
# create_docker_client()
docker_containers_test()
# docker_images_test()
# docker_prune_test()
