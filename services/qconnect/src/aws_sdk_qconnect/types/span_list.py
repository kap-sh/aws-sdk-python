"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.span

SpanList: TypeAlias = list["aws_sdk_qconnect.types.span.Span"]


# --- restJson1 ser/de ---
def serialize_json(value: SpanList) -> list:
    import aws_sdk_qconnect.types.span

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.span.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpanList:
    import aws_sdk_qconnect.types.span

    out: SpanList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.span.deserialize_json(item))
    return out
