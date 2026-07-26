"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfInAppMessageCampaign``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.in_app_message_campaign

ListOfInAppMessageCampaign: TypeAlias = list[
    "capo_pinpoint.types.in_app_message_campaign.InAppMessageCampaign"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfInAppMessageCampaign) -> list:
    import capo_pinpoint.types.in_app_message_campaign

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.in_app_message_campaign.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfInAppMessageCampaign:
    import capo_pinpoint.types.in_app_message_campaign

    out: ListOfInAppMessageCampaign = []
    for item in data:
        out.append(capo_pinpoint.types.in_app_message_campaign.deserialize_json(item))
    return out
