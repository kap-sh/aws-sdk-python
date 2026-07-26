"""Generated from Smithy shape ``com.amazonaws.fsx#WeeklyTime``."""

from typing import TypeAlias

"""<p>The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.</p> <p>For example, <code>1:05:00</code> specifies maintenance at 5 AM Monday.</p>"""
WeeklyTime: TypeAlias = str
