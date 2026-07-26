"""Generated from Smithy shape ``com.amazonaws.workdocs#LongRangeType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.long_type


class LongRangeType(TypedDict, closed=True):
    start_value: NotRequired["capo_workdocs.types.long_type.LongType"]
    """<p>The size start range (in bytes).</p>"""
    end_value: NotRequired["capo_workdocs.types.long_type.LongType"]
    """<p>The size end range (in bytes).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LongRangeType) -> dict:
    out: dict = {}
    if "start_value" in value:
        out["StartValue"] = value["start_value"]
    if "end_value" in value:
        out["EndValue"] = value["end_value"]
    return out


def deserialize_json(data: dict) -> LongRangeType:
    out: LongRangeType = {}  # type: ignore[typeddict-item]
    if "StartValue" in data:
        out["start_value"] = data["StartValue"]
    if "EndValue" in data:
        out["end_value"] = data["EndValue"]
    return out
