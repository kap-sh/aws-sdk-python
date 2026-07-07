"""Generated from Smithy shape ``com.amazonaws.ecs#VCpuCountRangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class VCpuCountRangeRequest(TypedDict, closed=True):
    min: "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    """<p>The minimum number of vCPUs. Instance types with fewer vCPUs than this value are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of vCPUs. Instance types with more vCPUs than this value are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VCpuCountRangeRequest) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VCpuCountRangeRequest:
    out: VCpuCountRangeRequest = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    else:
        raise DeserializationError("VCpuCountRangeRequest.min required")
    if "max" in data:
        out["max"] = data["max"]
    return out
