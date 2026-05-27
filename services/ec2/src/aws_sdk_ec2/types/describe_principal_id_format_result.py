"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePrincipalIdFormatResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.principal_id_format_list
    import aws_sdk_ec2.types.string


class DescribePrincipalIdFormatResult(TypedDict):
    principals: NotRequired[
        "aws_sdk_ec2.types.principal_id_format_list.PrincipalIdFormatList"
    ]
    """<p>Information about the ID format settings for the ARN.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""
