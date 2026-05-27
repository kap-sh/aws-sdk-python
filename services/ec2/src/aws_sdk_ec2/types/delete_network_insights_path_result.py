"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInsightsPathResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_path_id


class DeleteNetworkInsightsPathResult(TypedDict):
    network_insights_path_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path.</p>"""
