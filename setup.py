from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='TerminalDesigner',
  version='0.0.1',
  description='This is a Terminal designer like(Text Processing) ForeGround, BackGround we can change the colors in 3 different ways using this module.',
  long_description_content_type='text/markdown',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://nagipragalathan.github.io/Personal_website/home.html',
  author='NagiPragalathan',
  author_email='nagipragalathan@gmail.com',
  license='MIT', 
  classifiers=classifiers,          
  keywords=['Designer','terminal designer','color designer'], 
  packages=find_packages(),
  install_requires=[''] 
)