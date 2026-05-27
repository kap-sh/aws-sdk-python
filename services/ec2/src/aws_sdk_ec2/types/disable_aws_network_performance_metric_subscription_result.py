"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAwsNetworkPerformanceMetricSubscriptionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class DisableAwsNetworkPerformanceMetricSubscriptionResult(TypedDict):
    output: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the unsubscribe action was successful.</p>"""
