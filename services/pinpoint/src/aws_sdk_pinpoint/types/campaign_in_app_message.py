"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignInAppMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.layout
    import aws_sdk_pinpoint.types.list_of_in_app_message_content
    import aws_sdk_pinpoint.types.map_of__string


class CampaignInAppMessage(TypedDict, closed=True):
    body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message body of the notification, the email body or the text message.</p>"""
    content: NotRequired[
        "aws_sdk_pinpoint.types.list_of_in_app_message_content.ListOfInAppMessageContent"
    ]
    """<p>In-app message content.</p>"""
    custom_config: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>Custom config to be sent to client.</p>"""
    layout: NotRequired["aws_sdk_pinpoint.types.layout.Layout"]
    """<p>In-app message layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignInAppMessage) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    if "content" in value:
        import aws_sdk_pinpoint.types.list_of_in_app_message_content

        out["Content"] = (
            aws_sdk_pinpoint.types.list_of_in_app_message_content.serialize_json(
                value["content"]
            )
        )
    if "custom_config" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["CustomConfig"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["custom_config"]
        )
    if "layout" in value:
        import aws_sdk_pinpoint.types.layout

        out["Layout"] = aws_sdk_pinpoint.types.layout.serialize_json(value["layout"])
    return out


def deserialize_json(data: dict) -> CampaignInAppMessage:
    out: CampaignInAppMessage = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        out["body"] = data["Body"]
    if "Content" in data:
        import aws_sdk_pinpoint.types.list_of_in_app_message_content

        out["content"] = (
            aws_sdk_pinpoint.types.list_of_in_app_message_content.deserialize_json(
                data["Content"]
            )
        )
    if "CustomConfig" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["custom_config"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["CustomConfig"]
        )
    if "Layout" in data:
        import aws_sdk_pinpoint.types.layout

        out["layout"] = aws_sdk_pinpoint.types.layout.deserialize_json(data["Layout"])
    return out
