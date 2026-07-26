"""Generated from Smithy shape ``com.amazonaws.m2#RecordLength``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_m2.types.integer


class RecordLength(TypedDict, closed=True):
    min: "capo_m2.types.integer.Integer"
    """<p>The minimum record length of a record.</p>"""
    max: "capo_m2.types.integer.Integer"
    """<p>The maximum record length. In case of fixed, both minimum and maximum are the same.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordLength) -> dict:
    out: dict = {}
    out["min"] = value.get("min", 0)
    out["max"] = value.get("max", 0)
    return out


def deserialize_json(data: dict) -> RecordLength:
    out: RecordLength = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    else:
        out["min"] = 0
    if "max" in data:
        out["max"] = data["max"]
    else:
        out["max"] = 0
    return out
