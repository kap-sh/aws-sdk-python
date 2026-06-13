"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.span_message

SpanMessageList: TypeAlias = list["aws_sdk_qconnect.types.span_message.SpanMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: SpanMessageList) -> list:
    import aws_sdk_qconnect.types.span_message

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.span_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpanMessageList:
    import aws_sdk_qconnect.types.span_message

    out: SpanMessageList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.span_message.deserialize_json(item))
    return out
