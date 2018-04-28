#
#    Metrix++, Copyright 2009-2013, Metrix++ Project
#    Link: http://metrixplusplus.sourceforge.net
#    
#    This file is a part of Metrix++ Tool.
#    
#    Metrix++ is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#    
#    Metrix++ is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with Metrix++.  If not, see <http://www.gnu.org/licenses/>.
#


import unittest

import tests.common

class Test(tests.common.TestCase):

    def test_workflow(self):
        
        #
        # WARNING:
        # files generated by this test are used by project documents page
        # so, if the test is changed, html docs should be updated accordingly
        #
        
        runner = tests.common.ToolRunner('collect',
                                         ['--std.code.complexity.cyclomatic',
                                          '--std.code.lines.code',
                                          '--log-level=INFO'],
                                         check_stderr=[(0, -1)],
                                         save_prev=True)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('collect',
                                         ['--std.code.complexity.cyclomatic',
                                          '--std.code.lines.code',
                                          '--log-level=INFO'],
                                         check_stderr=[(0, -1)],
                                         prefix='second',
                                         cwd="sources_changed",
                                         use_prev=True)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('view',
                                         ['--log-level=INFO'],
                                         check_stderr=[(0, -1)])
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('view',
                                         ['--log-level=INFO', '--scope-mode=all'],
                                         check_stderr=[(0, -1)],
                                         prefix='second_all',
                                         use_prev=True)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('view',
                                         ['--log-level=INFO', '--scope-mode=touched'],
                                         check_stderr=[(0, -1)],
                                         prefix='second_touched',
                                         use_prev=True)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('view',
                                         ['--log-level=INFO', '--scope-mode=new'],
                                         check_stderr=[(0, -1)],
                                         prefix='second_new',
                                         use_prev=True)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('view',
                                         ['--log-level=INFO'],
                                         check_stderr=[(0, -1)],
                                         prefix='second_per_file',
                                         dirs_list=['./interprocess/detail/managed_open_or_create_impl.hpp'],
                                         use_prev=True)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('limit',
                                         ['--log-level=INFO',
                                          '--max-limit=std.code.complexity:cyclomatic:15',
                                          '--hotspots=3'],
                                         check_stderr=[(0, -1)],
                                         exit_code=3)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('limit',
                                         ['--log-level=INFO',
                                          '--max-limit=std.code.complexity:cyclomatic:15',
                                          '--warn-mode=touched'],
                                         check_stderr=[(0, -1)],
                                         prefix='second_touched',
                                         exit_code=6,
                                         use_prev=True)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('limit',
                                         ['--log-level=INFO',
                                          '--max-limit=std.code.complexity:cyclomatic:15',
                                          '--warn-mode=trend'],
                                         check_stderr=[(0, -1)],
                                         prefix='second_trend',
                                         exit_code=2,
                                         use_prev=True)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('limit',
                                         ['--log-level=INFO',
                                          '--max-limit=std.code.complexity:cyclomatic:15',
                                          '--warn-mode=new'],
                                         check_stderr=[(0, -1)],
                                         prefix='second_new',
                                         exit_code=0,
                                         use_prev=True)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('info',
                                         ['--log-level=INFO'],
                                         check_stderr=[(0, -1)],
                                         exit_code=0)
        self.assertExec(runner.run())

        runner = tests.common.ToolRunner('export',
                                         ['--log-level=INFO'],
                                         check_stderr=[(0, -1)],
                                         exit_code=0)
        self.assertExec(runner.run())

if __name__ == '__main__':
    unittest.main()
    