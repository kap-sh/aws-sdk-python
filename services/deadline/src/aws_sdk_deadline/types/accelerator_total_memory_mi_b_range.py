"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorTotalMemoryMiBRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.min_zero_max_integer


class AcceleratorTotalMemoryMiBRange(TypedDict, closed=True):
    min: "aws_sdk_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    """<p>The minimum amount of memory to use for the accelerator, measured in MiB.</p>"""
    max: NotRequired["aws_sdk_deadline.types.min_zero_max_integer.MinZeroMaxInteger"]
    """<p>The maximum amount of memory to use for the accelerator, measured in MiB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorTotalMemoryMiBRange) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> AcceleratorTotalMemoryMiBRange:
    out: AcceleratorTotalMemoryMiBRange = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    else:
        raise DeserializationError("AcceleratorTotalMemoryMiBRange.min required")
    if "max" in data:
        out["max"] = data["max"]
    return out
