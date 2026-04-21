from setuptools import setup

package_name = 'traffic_sign_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 👇 THIS LINE FIXES YOUR ERROR
        ('lib/' + package_name, ['traffic_sign_bot/final_model.h5']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='priy2005',
    maintainer_email='priy2005@todo.todo',
    description='Traffic sign detection bot using CNN',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'detector = traffic_sign_bot.detector:main',
        ],
    },
)
