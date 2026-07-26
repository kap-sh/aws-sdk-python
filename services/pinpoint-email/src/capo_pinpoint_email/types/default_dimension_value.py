"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DefaultDimensionValue``."""

from typing import TypeAlias

"""<p>The default value of the dimension that is published to Amazon CloudWatch if you don't provide the value of the dimension when you send an email. This value has to meet the following criteria:</p> <ul> <li> <p>It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>It can contain no more than 256 characters.</p> </li> </ul>"""
DefaultDimensionValue: TypeAlias = str
