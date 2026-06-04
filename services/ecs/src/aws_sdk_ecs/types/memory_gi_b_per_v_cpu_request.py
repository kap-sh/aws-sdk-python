"""Generated from Smithy shape ``com.amazonaws.ecs#MemoryGiBPerVCpuRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_double


class MemoryGiBPerVCpuRequest(TypedDict):
    min: NotRequired["aws_sdk_ecs.types.boxed_double.BoxedDouble"]
    """<p>The minimum amount of memory per vCPU in GiB. Instance types with a lower memory-to-vCPU ratio are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_double.BoxedDouble"]
    """<p>The maximum amount of memory per vCPU in GiB. Instance types with a higher memory-to-vCPU ratio are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemoryGiBPerVCpuRequest) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MemoryGiBPerVCpuRequest:
    out: MemoryGiBPerVCpuRequest = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    return out
