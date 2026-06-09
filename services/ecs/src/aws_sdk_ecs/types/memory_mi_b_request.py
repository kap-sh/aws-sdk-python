"""Generated from Smithy shape ``com.amazonaws.ecs#MemoryMiBRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class MemoryMiBRequest(TypedDict):
    min: "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    """<p>The minimum amount of memory in MiB. Instance types with less memory than this value are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum amount of memory in MiB. Instance types with more memory than this value are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemoryMiBRequest) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MemoryMiBRequest:
    out: MemoryMiBRequest = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    else:
        raise DeserializationError("MemoryMiBRequest.min required")
    if "max" in data:
        out["max"] = data["max"]
    return out
