"""Generated from Smithy shape ``com.amazonaws.appintegrations#Subscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appintegrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.description
    import aws_sdk_appintegrations.types.event_name


class Subscription(TypedDict, closed=True):
    event: "aws_sdk_appintegrations.types.event_name.EventName"
    """<p>The name of the subscription.</p>"""
    description: NotRequired["aws_sdk_appintegrations.types.description.Description"]
    """<p>The description of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Subscription) -> dict:
    out: dict = {}
    out["Event"] = value["event"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if "Event" in data:
        out["event"] = data["Event"]
    else:
        raise DeserializationError("Subscription.event required")
    if "Description" in data:
        out["description"] = data["Description"]
    return out
