"""Generated from Smithy shape ``com.amazonaws.deadline#Stats``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.double


class Stats(TypedDict):
    min: NotRequired["aws_sdk_deadline.types.double.Double"]
    """<p>The minimum of the usage statistics.</p>"""
    max: NotRequired["aws_sdk_deadline.types.double.Double"]
    """<p>The maximum among the usage statistics.</p>"""
    avg: NotRequired["aws_sdk_deadline.types.double.Double"]
    """<p>The average of the usage statistics.</p>"""
    sum: NotRequired["aws_sdk_deadline.types.double.Double"]
    """<p>The sum of the usage statistics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Stats) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    if "avg" in value:
        out["avg"] = value["avg"]
    if "sum" in value:
        out["sum"] = value["sum"]
    return out


def deserialize_json(data: dict) -> Stats:
    out: Stats = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    if "avg" in data:
        out["avg"] = data["avg"]
    if "sum" in data:
        out["sum"] = data["sum"]
    return out
