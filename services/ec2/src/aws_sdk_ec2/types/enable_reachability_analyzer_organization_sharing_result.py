"""Generated from Smithy shape ``com.amazonaws.ec2#EnableReachabilityAnalyzerOrganizationSharingResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class EnableReachabilityAnalyzerOrganizationSharingResult(TypedDict):
    return_value: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Returns <code>true</code> if the request succeeds; otherwise, returns an error.</p>"""
