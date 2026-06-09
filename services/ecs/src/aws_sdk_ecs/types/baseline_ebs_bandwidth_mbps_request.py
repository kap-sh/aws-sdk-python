"""Generated from Smithy shape ``com.amazonaws.ecs#BaselineEbsBandwidthMbpsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class BaselineEbsBandwidthMbpsRequest(TypedDict):
    min: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The minimum baseline Amazon EBS bandwidth in Mbps. Instance types with lower Amazon EBS bandwidth are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum baseline Amazon EBS bandwidth in Mbps. Instance types with higher Amazon EBS bandwidth are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BaselineEbsBandwidthMbpsRequest) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BaselineEbsBandwidthMbpsRequest:
    out: BaselineEbsBandwidthMbpsRequest = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    return out
