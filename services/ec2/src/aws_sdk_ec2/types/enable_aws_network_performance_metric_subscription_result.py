"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAwsNetworkPerformanceMetricSubscriptionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class EnableAwsNetworkPerformanceMetricSubscriptionResult(TypedDict):
    output: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the subscribe action was successful.</p>"""
