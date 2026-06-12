"""Generated from Smithy shape ``com.amazonaws.deadline#MemoryMiBRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.memory_amount_mi_b


class MemoryMiBRange(TypedDict):
    min: "aws_sdk_deadline.types.memory_amount_mi_b.MemoryAmountMiB"
    """<p>The minimum amount of memory (in MiB).</p>"""
    max: NotRequired["aws_sdk_deadline.types.memory_amount_mi_b.MemoryAmountMiB"]
    """<p>The maximum amount of memory (in MiB).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryMiBRange) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> MemoryMiBRange:
    out: MemoryMiBRange = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    else:
        raise DeserializationError("MemoryMiBRange.min required")
    if "max" in data:
        out["max"] = data["max"]
    return out
