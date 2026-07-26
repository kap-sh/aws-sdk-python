"""Generated from Smithy shape ``com.amazonaws.connect#NewSessionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attributes
    import capo_connect.types.chat_streaming_configuration
    import capo_connect.types.participant_details
    import capo_connect.types.supported_messaging_content_types


class NewSessionDetails(TypedDict, closed=True):
    supported_messaging_content_types: NotRequired[
        "capo_connect.types.supported_messaging_content_types.SupportedMessagingContentTypes"
    ]
    """<p> The supported chat message content types. Supported types are <code>text/plain</code>, <code>text/markdown</code>, <code>application/json</code>, <code>application/vnd.amazonaws.connect.message.interactive</code>, and <code>application/vnd.amazonaws.connect.message.interactive.response</code>. </p> <p>Content types must always contain <code> text/plain</code>. You can then put any other supported type in the list. For example, all the following lists are valid because they contain <code>text/plain</code>: <code>[text/plain, text/markdown, application/json]</code>, <code> [text/markdown, text/plain]</code>, <code>[text/plain, application/json, application/vnd.amazonaws.connect.message.interactive.response]</code>. </p>"""
    participant_details: NotRequired[
        "capo_connect.types.participant_details.ParticipantDetails"
    ]
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p> A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows just like any other contact attributes. </p> <p> There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters. </p>"""
    streaming_configuration: NotRequired[
        "capo_connect.types.chat_streaming_configuration.ChatStreamingConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: NewSessionDetails) -> dict:
    out: dict = {}
    if "supported_messaging_content_types" in value:
        import capo_connect.types.supported_messaging_content_types

        out["SupportedMessagingContentTypes"] = (
            capo_connect.types.supported_messaging_content_types.serialize_json(
                value["supported_messaging_content_types"]
            )
        )
    if "participant_details" in value:
        import capo_connect.types.participant_details

        out["ParticipantDetails"] = (
            capo_connect.types.participant_details.serialize_json(
                value["participant_details"]
            )
        )
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "streaming_configuration" in value:
        import capo_connect.types.chat_streaming_configuration

        out["StreamingConfiguration"] = (
            capo_connect.types.chat_streaming_configuration.serialize_json(
                value["streaming_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> NewSessionDetails:
    out: NewSessionDetails = {}  # type: ignore[typeddict-item]
    if "SupportedMessagingContentTypes" in data:
        import capo_connect.types.supported_messaging_content_types

        out["supported_messaging_content_types"] = (
            capo_connect.types.supported_messaging_content_types.deserialize_json(
                data["SupportedMessagingContentTypes"]
            )
        )
    if "ParticipantDetails" in data:
        import capo_connect.types.participant_details

        out["participant_details"] = (
            capo_connect.types.participant_details.deserialize_json(
                data["ParticipantDetails"]
            )
        )
    if "Attributes" in data:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if "StreamingConfiguration" in data:
        import capo_connect.types.chat_streaming_configuration

        out["streaming_configuration"] = (
            capo_connect.types.chat_streaming_configuration.deserialize_json(
                data["StreamingConfiguration"]
            )
        )
    return out
