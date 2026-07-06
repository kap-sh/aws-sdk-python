"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.list_of_in_app_message_campaign


class InAppMessagesResponse(TypedDict, closed=True):
    in_app_message_campaigns: NotRequired[
        "aws_sdk_pinpoint.types.list_of_in_app_message_campaign.ListOfInAppMessageCampaign"
    ]
    """<p>List of targeted in-app message campaigns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppMessagesResponse) -> dict:
    out: dict = {}
    if "in_app_message_campaigns" in value:
        import aws_sdk_pinpoint.types.list_of_in_app_message_campaign

        out["InAppMessageCampaigns"] = (
            aws_sdk_pinpoint.types.list_of_in_app_message_campaign.serialize_json(
                value["in_app_message_campaigns"]
            )
        )
    return out


def deserialize_json(data: dict) -> InAppMessagesResponse:
    out: InAppMessagesResponse = {}  # type: ignore[typeddict-item]
    if "InAppMessageCampaigns" in data:
        import aws_sdk_pinpoint.types.list_of_in_app_message_campaign

        out["in_app_message_campaigns"] = (
            aws_sdk_pinpoint.types.list_of_in_app_message_campaign.deserialize_json(
                data["InAppMessageCampaigns"]
            )
        )
    return out
