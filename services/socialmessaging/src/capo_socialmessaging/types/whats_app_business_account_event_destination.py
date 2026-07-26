"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppBusinessAccountEventDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.event_destination_arn
    import capo_socialmessaging.types.role_arn


class WhatsAppBusinessAccountEventDestination(TypedDict, closed=True):
    event_destination_arn: (
        "capo_socialmessaging.types.event_destination_arn.EventDestinationArn"
    )
    """<p>The ARN of the event destination.</p>"""
    role_arn: NotRequired["capo_socialmessaging.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an Identity and Access Management role that is able to import phone numbers and write events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppBusinessAccountEventDestination) -> dict:
    out: dict = {}
    out["eventDestinationArn"] = value["event_destination_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> WhatsAppBusinessAccountEventDestination:
    out: WhatsAppBusinessAccountEventDestination = {}  # type: ignore[typeddict-item]
    if "eventDestinationArn" in data:
        out["event_destination_arn"] = data["eventDestinationArn"]
    else:
        raise DeserializationError(
            "WhatsAppBusinessAccountEventDestination.event_destination_arn required"
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
