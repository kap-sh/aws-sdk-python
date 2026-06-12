"""Generated from Smithy shape ``com.amazonaws.pinpoint#ContactCenterActivity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class ContactCenterActivity(TypedDict):
    next_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the next activity to perform after the this activity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactCenterActivity) -> dict:
    out: dict = {}
    if "next_activity" in value:
        out["NextActivity"] = value["next_activity"]
    return out


def deserialize_json(data: dict) -> ContactCenterActivity:
    out: ContactCenterActivity = {}  # type: ignore[typeddict-item]
    if "NextActivity" in data:
        out["next_activity"] = data["NextActivity"]
    return out
