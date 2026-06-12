"""Generated from Smithy shape ``com.amazonaws.sesv2#MessageHeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.message_header

MessageHeaderList: TypeAlias = list["aws_sdk_sesv2.types.message_header.MessageHeader"]


# --- restJson1 ser/de ---
def serialize_json(value: MessageHeaderList) -> list:
    import aws_sdk_sesv2.types.message_header

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.message_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> MessageHeaderList:
    import aws_sdk_sesv2.types.message_header

    out: MessageHeaderList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.message_header.deserialize_json(item))
    return out
