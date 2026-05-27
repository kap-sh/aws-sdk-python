"""Generated from Smithy shape ``com.amazonaws.ec2#PrincipalIdFormat``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.id_format_list
    import aws_sdk_ec2.types.string


class PrincipalIdFormat(TypedDict):
    arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>PrincipalIdFormatARN description</p>"""
    statuses: NotRequired["aws_sdk_ec2.types.id_format_list.IdFormatList"]
    """<p>PrincipalIdFormatStatuses description</p>"""
