"""Generated from Smithy shape ``com.amazonaws.deadline#VCpuCountRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.min_one_max_ten_thousand


class VCpuCountRange(TypedDict, closed=True):
    min: "capo_deadline.types.min_one_max_ten_thousand.MinOneMaxTenThousand"
    """<p>The minimum amount of vCPU.</p>"""
    max: NotRequired[
        "capo_deadline.types.min_one_max_ten_thousand.MinOneMaxTenThousand"
    ]
    """<p>The maximum amount of vCPU.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VCpuCountRange) -> dict:
    out: dict = {}
    out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_json(data: dict) -> VCpuCountRange:
    out: VCpuCountRange = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    else:
        raise DeserializationError("VCpuCountRange.min required")
    if "max" in data:
        out["max"] = data["max"]
    return out
