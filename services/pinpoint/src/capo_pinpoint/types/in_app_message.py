"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.layout
    import capo_pinpoint.types.list_of_in_app_message_content
    import capo_pinpoint.types.map_of__string


class InAppMessage(TypedDict, closed=True):
    content: NotRequired[
        "capo_pinpoint.types.list_of_in_app_message_content.ListOfInAppMessageContent"
    ]
    """<p>In-app message content.</p>"""
    custom_config: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>Custom config to be sent to SDK.</p>"""
    layout: NotRequired["capo_pinpoint.types.layout.Layout"]
    """<p>The layout of the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppMessage) -> dict:
    out: dict = {}
    if "content" in value:
        import capo_pinpoint.types.list_of_in_app_message_content

        out["Content"] = (
            capo_pinpoint.types.list_of_in_app_message_content.serialize_json(
                value["content"]
            )
        )
    if "custom_config" in value:
        import capo_pinpoint.types.map_of__string

        out["CustomConfig"] = capo_pinpoint.types.map_of__string.serialize_json(
            value["custom_config"]
        )
    if "layout" in value:
        import capo_pinpoint.types.layout

        out["Layout"] = capo_pinpoint.types.layout.serialize_json(value["layout"])
    return out


def deserialize_json(data: dict) -> InAppMessage:
    out: InAppMessage = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        import capo_pinpoint.types.list_of_in_app_message_content

        out["content"] = (
            capo_pinpoint.types.list_of_in_app_message_content.deserialize_json(
                data["Content"]
            )
        )
    if "CustomConfig" in data:
        import capo_pinpoint.types.map_of__string

        out["custom_config"] = capo_pinpoint.types.map_of__string.deserialize_json(
            data["CustomConfig"]
        )
    if "Layout" in data:
        import capo_pinpoint.types.layout

        out["layout"] = capo_pinpoint.types.layout.deserialize_json(data["Layout"])
    return out
