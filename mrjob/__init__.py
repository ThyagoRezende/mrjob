# Copyright 2009-2012 Yelp
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Write and run Hadoop Streaming jobs on Amazon Elastic MapReduce or your own
Hadoop cluster.
"""

__author__ = 'David Marin <dave@yelp.com>'

__credits__ = [
    'Jordan Andersen <jordandandersen@gmail.com>',
    'Hunter Blanks <hblanks@monetate.com>',
    'Jim Blomo <jblomo@yelp.com>',
    'James Brown <jbrown@yelp.com>',
    'Kevin Burke <kevin@twilio.com>',
    'David Dehghan <ddehghan@gmail.com>',
    'Adam Derewecki <derewecki@gmail.com>',
    'Dan Frank <danielhfrank@gmail.com>',
    'Benjamin Goldenberg <benjamin@yelp.com',
    'Peter Harrington <peter.b.harrington@gmail.com>',
    'Brandon Haynes <bhaynes@fas.harvard.edu>',
    'Brett Hoerner <brett@bretthoerner.com>',
    'Tom Janofsky <tjanofsky@monetate.com>',
    'Stephen Johnson <sjohnson@yelp.com>',
    'Matt Jones <mattj@yelp.com>',
    'Nikolaos Koutsopoulos <nhk@mochimedia.com>',
    'Julian Krause <juliank@yelp.com>',
    'Robert Leftwich <rl.0x0@eml.cc>',
    'Tetsuya Morimoto <tetsuya.morimoto@gmail.com>',
    'Wahbeh Qardaji <wqardaji@yelp.com>',
    'Jimmy Retzlaff <jretz@yelp.com>',
    'Ned Rockson <ned@tellapart.com>',
    'Paul Scott <paul@duedil.com>',
    'Jesse Shieh <jesse@adku.com>',
    'Steve Spencer <steve@bigfrog.net>',
    'Jyry Suvilehto <jyry.suvilehto@iki.fi>',
    'Matthew Tai <mtai@adku.com>',
    'Paul Wais <pwais@yelp.com>',
    'Derek Wilson <jderekwilson@gmail.com>',
]

__version__ = '0.4-dev'
