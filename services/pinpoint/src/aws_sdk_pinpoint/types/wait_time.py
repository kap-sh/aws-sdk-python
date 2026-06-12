"""Generated from Smithy shape ``com.amazonaws.pinpoint#WaitTime``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class WaitTime(TypedDict):
    wait_for: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The amount of time to wait, as a duration in ISO 8601 format, before determining whether the activity's conditions have been met or moving participants to the next activity in the journey.</p>"""
    wait_until: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when Amazon Pinpoint determines whether the activity's conditions have been met or the activity moves participants to the next activity in the journey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaitTime) -> dict:
    out: dict = {}
    if "wait_for" in value:
        out["WaitFor"] = value["wait_for"]
    if "wait_until" in value:
        out["WaitUntil"] = value["wait_until"]
    return out


def deserialize_json(data: dict) -> WaitTime:
    out: WaitTime = {}  # type: ignore[typeddict-item]
    if "WaitFor" in data:
        out["wait_for"] = data["WaitFor"]
    if "WaitUntil" in data:
        out["wait_until"] = data["WaitUntil"]
    return out
