"""Generated from Smithy shape ``com.amazonaws.deadline#AcceleratorCountRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.min_zero_max_integer


class AcceleratorCountRange(TypedDict):
    min: "aws_sdk_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
    """<p>The minimum number of GPU accelerators in the worker host.</p>"""
    max: NotRequired["aws_sdk_deadline.types.min_zero_max_integer.MinZeroMaxInteger"]
    """<p>The maximum number of GPU accelerators in the worker host.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceleratorCountRange) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> AcceleratorCountRange:
    out: AcceleratorCountRange = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    else:
        raise DeserializationError("AcceleratorCountRange.min required")
    if "max" in data:
        out["max"] = data["max"]
    return out
