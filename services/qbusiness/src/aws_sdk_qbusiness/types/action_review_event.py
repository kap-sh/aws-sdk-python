"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionReviewEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_payload_field_name_separator
    import aws_sdk_qbusiness.types.action_review_payload
    import aws_sdk_qbusiness.types.conversation_id
    import aws_sdk_qbusiness.types.message_id
    import aws_sdk_qbusiness.types.plugin_id
    import aws_sdk_qbusiness.types.plugin_type


class ActionReviewEvent(TypedDict):
    conversation_id: NotRequired[
        "aws_sdk_qbusiness.types.conversation_id.ConversationId"
    ]
    """<p>The identifier of the conversation with which the action review event is associated.</p>"""
    user_message_id: NotRequired["aws_sdk_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of the conversation with which the plugin action is associated.</p>"""
    system_message_id: NotRequired["aws_sdk_qbusiness.types.message_id.MessageId"]
    """<p>The identifier of an Amazon Q Business AI generated associated with the action review event.</p>"""
    plugin_id: NotRequired["aws_sdk_qbusiness.types.plugin_id.PluginId"]
    """<p>The identifier of the plugin associated with the action review event.</p>"""
    plugin_type: NotRequired["aws_sdk_qbusiness.types.plugin_type.PluginType"]
    """<p>The type of plugin.</p>"""
    payload: NotRequired[
        "aws_sdk_qbusiness.types.action_review_payload.ActionReviewPayload"
    ]
    """<p>Field values that an end user needs to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.</p>"""
    payload_field_name_separator: NotRequired[
        "aws_sdk_qbusiness.types.action_payload_field_name_separator.ActionPayloadFieldNameSeparator"
    ]
    """<p>A string used to retain information about the hierarchical contexts within an action review event payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionReviewEvent) -> dict:
    out: dict = {}
    if "conversation_id" in value:
        out["conversationId"] = value["conversation_id"]
    if "user_message_id" in value:
        out["userMessageId"] = value["user_message_id"]
    if "system_message_id" in value:
        out["systemMessageId"] = value["system_message_id"]
    if "plugin_id" in value:
        out["pluginId"] = value["plugin_id"]
    if "plugin_type" in value:
        import aws_sdk_qbusiness.types.plugin_type

        out["pluginType"] = aws_sdk_qbusiness.types.plugin_type.serialize_json(
            value["plugin_type"]
        )
    if "payload" in value:
        import aws_sdk_qbusiness.types.action_review_payload

        out["payload"] = aws_sdk_qbusiness.types.action_review_payload.serialize_json(
            value["payload"]
        )
    if "payload_field_name_separator" in value:
        out["payloadFieldNameSeparator"] = value["payload_field_name_separator"]
    return out


def deserialize_json(data: dict) -> ActionReviewEvent:
    out: ActionReviewEvent = {}  # type: ignore[typeddict-item]
    if "conversationId" in data:
        out["conversation_id"] = data["conversationId"]
    if "userMessageId" in data:
        out["user_message_id"] = data["userMessageId"]
    if "systemMessageId" in data:
        out["system_message_id"] = data["systemMessageId"]
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    if "pluginType" in data:
        import aws_sdk_qbusiness.types.plugin_type

        out["plugin_type"] = aws_sdk_qbusiness.types.plugin_type.deserialize_json(
            data["pluginType"]
        )
    if "payload" in data:
        import aws_sdk_qbusiness.types.action_review_payload

        out["payload"] = aws_sdk_qbusiness.types.action_review_payload.deserialize_json(
            data["payload"]
        )
    if "payloadFieldNameSeparator" in data:
        out["payload_field_name_separator"] = data["payloadFieldNameSeparator"]
    return out


def serialize_event_json(value: ActionReviewEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "actionReviewEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ActionReviewEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ActionReviewEvent = {}  # type: ignore[typeddict-item]
    return out
