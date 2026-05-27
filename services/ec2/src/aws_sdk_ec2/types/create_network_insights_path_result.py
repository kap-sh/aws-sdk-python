"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInsightsPathResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_path


class CreateNetworkInsightsPathResult(TypedDict):
    network_insights_path: NotRequired[
        "aws_sdk_ec2.types.network_insights_path.NetworkInsightsPath"
    ]
    """<p>Information about the path.</p>"""
