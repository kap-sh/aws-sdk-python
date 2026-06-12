"""Generated from Smithy shape ``com.amazonaws.iot#TimeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.string_date_time


class TimeFilter(TypedDict):
    after: NotRequired["aws_sdk_iot.types.string_date_time.StringDateTime"]
    """<p>Filter to display command executions that started or completed only after a particular date and time.</p>"""
    before: NotRequired["aws_sdk_iot.types.string_date_time.StringDateTime"]
    """<p>Filter to display command executions that started or completed only before a particular date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeFilter) -> dict:
    out: dict = {}
    if "after" in value:
        out["after"] = value["after"]
    if "before" in value:
        out["before"] = value["before"]
    return out


def deserialize_json(data: dict) -> TimeFilter:
    out: TimeFilter = {}  # type: ignore[typeddict-item]
    if "after" in data:
        out["after"] = data["after"]
    if "before" in data:
        out["before"] = data["before"]
    return out
