"""Generated from Smithy shape ``com.amazonaws.ec2#GetConsoleOutputResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string


class GetConsoleOutputResult(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    timestamp: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time at which the output was last updated.</p>"""
    output: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The console output, base64-encoded. If you are using a command line tool, the tool decodes the output for you.</p>"""
