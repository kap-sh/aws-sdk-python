"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyEmailMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string


class JourneyEmailMessage(TypedDict, closed=True):
    from_address: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The verified email address to send the email message from. The default address is the FromAddress specified for the email channel for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyEmailMessage) -> dict:
    out: dict = {}
    if "from_address" in value:
        out["FromAddress"] = value["from_address"]
    return out


def deserialize_json(data: dict) -> JourneyEmailMessage:
    out: JourneyEmailMessage = {}  # type: ignore[typeddict-item]
    if "FromAddress" in data:
        out["from_address"] = data["FromAddress"]
    return out
