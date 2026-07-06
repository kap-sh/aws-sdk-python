"""Generated from Smithy shape ``com.amazonaws.qbusiness#ConfigurationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qbusiness._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attribute_filter
    import aws_sdk_qbusiness.types.chat_mode
    import aws_sdk_qbusiness.types.chat_mode_configuration


class ConfigurationEvent(TypedDict, closed=True):
    chat_mode: NotRequired["aws_sdk_qbusiness.types.chat_mode.ChatMode"]
    r"""<p>The chat modes available to an Amazon Q Business end user.</p> <ul> <li> <p> <code>RETRIEVAL_MODE</code> - The default chat mode for an Amazon Q Business application. When this mode is enabled, Amazon Q Business generates responses only from data sources connected to an Amazon Q Business application.</p> </li> <li> <p> <code>CREATOR_MODE</code> - By selecting this mode, users can choose to generate responses only from the LLM knowledge, without consulting connected data sources, for a chat request.</p> </li> <li> <p> <code>PLUGIN_MODE</code> - By selecting this mode, users can choose to use plugins in chat.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html\">Admin controls and guardrails</a>, <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html\">Plugins</a>, and <a href=\"https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope\">Conversation settings</a>.</p>"""
    chat_mode_configuration: NotRequired[
        "aws_sdk_qbusiness.types.chat_mode_configuration.ChatModeConfiguration"
    ]
    attribute_filter: NotRequired[
        "aws_sdk_qbusiness.types.attribute_filter.AttributeFilter"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationEvent) -> dict:
    out: dict = {}
    if "chat_mode" in value:
        import aws_sdk_qbusiness.types.chat_mode

        out["chatMode"] = aws_sdk_qbusiness.types.chat_mode.serialize_json(
            value["chat_mode"]
        )
    if "chat_mode_configuration" in value:
        import aws_sdk_qbusiness.types.chat_mode_configuration

        out["chatModeConfiguration"] = (
            aws_sdk_qbusiness.types.chat_mode_configuration.serialize_json(
                value["chat_mode_configuration"]
            )
        )
    if "attribute_filter" in value:
        import aws_sdk_qbusiness.types.attribute_filter

        out["attributeFilter"] = (
            aws_sdk_qbusiness.types.attribute_filter.serialize_json(
                value["attribute_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationEvent:
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if "chatMode" in data:
        import aws_sdk_qbusiness.types.chat_mode

        out["chat_mode"] = aws_sdk_qbusiness.types.chat_mode.deserialize_json(
            data["chatMode"]
        )
    if "chatModeConfiguration" in data:
        import aws_sdk_qbusiness.types.chat_mode_configuration

        out["chat_mode_configuration"] = (
            aws_sdk_qbusiness.types.chat_mode_configuration.deserialize_json(
                data["chatModeConfiguration"]
            )
        )
    if "attributeFilter" in data:
        import aws_sdk_qbusiness.types.attribute_filter

        out["attribute_filter"] = (
            aws_sdk_qbusiness.types.attribute_filter.deserialize_json(
                data["attributeFilter"]
            )
        )
    return out


def serialize_event_json(value: ConfigurationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "configurationEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ConfigurationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    return out
