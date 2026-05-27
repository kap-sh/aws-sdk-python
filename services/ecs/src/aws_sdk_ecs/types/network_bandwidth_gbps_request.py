"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkBandwidthGbpsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_double


class NetworkBandwidthGbpsRequest(TypedDict):
    min: NotRequired["aws_sdk_ecs.types.boxed_double.BoxedDouble"]
    """<p>The minimum network bandwidth in Gbps. Instance types with lower network bandwidth are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_double.BoxedDouble"]
    """<p>The maximum network bandwidth in Gbps. Instance types with higher network bandwidth are excluded from selection.</p>"""
