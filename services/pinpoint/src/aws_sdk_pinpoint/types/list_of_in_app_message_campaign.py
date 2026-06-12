"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfInAppMessageCampaign``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.in_app_message_campaign

ListOfInAppMessageCampaign: TypeAlias = list[
    "aws_sdk_pinpoint.types.in_app_message_campaign.InAppMessageCampaign"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfInAppMessageCampaign) -> list:
    import aws_sdk_pinpoint.types.in_app_message_campaign

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.in_app_message_campaign.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfInAppMessageCampaign:
    import aws_sdk_pinpoint.types.in_app_message_campaign

    out: ListOfInAppMessageCampaign = []
    for item in data:
        out.append(
            aws_sdk_pinpoint.types.in_app_message_campaign.deserialize_json(item)
        )
    return out
