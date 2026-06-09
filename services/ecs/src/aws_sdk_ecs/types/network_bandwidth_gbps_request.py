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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkBandwidthGbpsRequest) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkBandwidthGbpsRequest:
    out: NetworkBandwidthGbpsRequest = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    return out
