"""Generated from Smithy shape ``com.amazonaws.sesv2#DimensionName``."""

from typing import TypeAlias

"""<p>The name of an Amazon CloudWatch dimension associated with an email sending metric. The name has to meet the following criteria:</p> <ul> <li> <p>It can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>It can contain no more than 255 characters.</p> </li> </ul>"""
DimensionName: TypeAlias = str
