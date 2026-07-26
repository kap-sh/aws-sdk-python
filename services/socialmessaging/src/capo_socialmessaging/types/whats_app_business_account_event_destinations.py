"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppBusinessAccountEventDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_business_account_event_destination

WhatsAppBusinessAccountEventDestinations: TypeAlias = list[
    "capo_socialmessaging.types.whats_app_business_account_event_destination.WhatsAppBusinessAccountEventDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppBusinessAccountEventDestinations) -> list:
    import capo_socialmessaging.types.whats_app_business_account_event_destination

    out: list = []
    for item in value:
        out.append(
            capo_socialmessaging.types.whats_app_business_account_event_destination.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WhatsAppBusinessAccountEventDestinations:
    import capo_socialmessaging.types.whats_app_business_account_event_destination

    out: WhatsAppBusinessAccountEventDestinations = []
    for item in data:
        out.append(
            capo_socialmessaging.types.whats_app_business_account_event_destination.deserialize_json(
                item
            )
        )
    return out
