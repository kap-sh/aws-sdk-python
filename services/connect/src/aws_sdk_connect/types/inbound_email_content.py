"""Generated from Smithy shape ``com.amazonaws.connect#InboundEmailContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.inbound_message_source_type
    import aws_sdk_connect.types.inbound_raw_message


class InboundEmailContent(TypedDict):
    message_source_type: (
        "aws_sdk_connect.types.inbound_message_source_type.InboundMessageSourceType"
    )
    """<p>The message source type, that is, <code>RAW</code>.</p>"""
    raw_message: NotRequired[
        "aws_sdk_connect.types.inbound_raw_message.InboundRawMessage"
    ]
    """<p>The raw email body content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InboundEmailContent) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.inbound_message_source_type

    out["MessageSourceType"] = (
        aws_sdk_connect.types.inbound_message_source_type.serialize_json(
            value["message_source_type"]
        )
    )
    if "raw_message" in value:
        import aws_sdk_connect.types.inbound_raw_message

        out["RawMessage"] = aws_sdk_connect.types.inbound_raw_message.serialize_json(
            value["raw_message"]
        )
    return out


def deserialize_json(data: dict) -> InboundEmailContent:
    out: InboundEmailContent = {}  # type: ignore[typeddict-item]
    if "MessageSourceType" in data:
        import aws_sdk_connect.types.inbound_message_source_type

        out["message_source_type"] = (
            aws_sdk_connect.types.inbound_message_source_type.deserialize_json(
                data["MessageSourceType"]
            )
        )
    else:
        raise DeserializationError("InboundEmailContent.message_source_type required")
    if "RawMessage" in data:
        import aws_sdk_connect.types.inbound_raw_message

        out["raw_message"] = aws_sdk_connect.types.inbound_raw_message.deserialize_json(
            data["RawMessage"]
        )
    return out
