"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIdFormatResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.id_format_list


class DescribeIdFormatResult(TypedDict):
    statuses: NotRequired["aws_sdk_ec2.types.id_format_list.IdFormatList"]
    """<p>Information about the ID format for the resource.</p>"""
