"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeConversionTasksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_conversion_task_list


class DescribeConversionTasksResult(TypedDict):
    conversion_tasks: NotRequired[
        "aws_sdk_ec2.types.describe_conversion_task_list.DescribeConversionTaskList"
    ]
    """<p>Information about the conversion tasks.</p>"""
