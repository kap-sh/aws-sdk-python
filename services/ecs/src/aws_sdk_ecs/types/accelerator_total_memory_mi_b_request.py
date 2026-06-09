"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorTotalMemoryMiBRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class AcceleratorTotalMemoryMiBRequest(TypedDict):
    min: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The minimum total accelerator memory in MiB. Instance types with less accelerator memory are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum total accelerator memory in MiB. Instance types with more accelerator memory are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorTotalMemoryMiBRequest) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceleratorTotalMemoryMiBRequest:
    out: AcceleratorTotalMemoryMiBRequest = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    return out
