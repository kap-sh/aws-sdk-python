"""Generated from Smithy shape ``com.amazonaws.connect#OutboundEmailContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.outbound_message_source_type
    import aws_sdk_connect.types.outbound_raw_message
    import aws_sdk_connect.types.templated_message_config


class OutboundEmailContent(TypedDict, closed=True):
    message_source_type: (
        "aws_sdk_connect.types.outbound_message_source_type.OutboundMessageSourceType"
    )
    """<p>The message source type, that is, <code>RAW</code> or <code>TEMPLATE</code>.</p>"""
    templated_message_config: NotRequired[
        "aws_sdk_connect.types.templated_message_config.TemplatedMessageConfig"
    ]
    """<p>Information about template message configuration.</p>"""
    raw_message: NotRequired[
        "aws_sdk_connect.types.outbound_raw_message.OutboundRawMessage"
    ]
    """<p>The raw email body content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundEmailContent) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.outbound_message_source_type

    out["MessageSourceType"] = (
        aws_sdk_connect.types.outbound_message_source_type.serialize_json(
            value["message_source_type"]
        )
    )
    if "templated_message_config" in value:
        import aws_sdk_connect.types.templated_message_config

        out["TemplatedMessageConfig"] = (
            aws_sdk_connect.types.templated_message_config.serialize_json(
                value["templated_message_config"]
            )
        )
    if "raw_message" in value:
        import aws_sdk_connect.types.outbound_raw_message

        out["RawMessage"] = aws_sdk_connect.types.outbound_raw_message.serialize_json(
            value["raw_message"]
        )
    return out


def deserialize_json(data: dict) -> OutboundEmailContent:
    out: OutboundEmailContent = {}  # type: ignore[typeddict-item]
    if "MessageSourceType" in data:
        import aws_sdk_connect.types.outbound_message_source_type

        out["message_source_type"] = (
            aws_sdk_connect.types.outbound_message_source_type.deserialize_json(
                data["MessageSourceType"]
            )
        )
    else:
        raise DeserializationError("OutboundEmailContent.message_source_type required")
    if "TemplatedMessageConfig" in data:
        import aws_sdk_connect.types.templated_message_config

        out["templated_message_config"] = (
            aws_sdk_connect.types.templated_message_config.deserialize_json(
                data["TemplatedMessageConfig"]
            )
        )
    if "RawMessage" in data:
        import aws_sdk_connect.types.outbound_raw_message

        out["raw_message"] = (
            aws_sdk_connect.types.outbound_raw_message.deserialize_json(
                data["RawMessage"]
            )
        )
    return out
