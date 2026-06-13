"""Generated from Smithy shape ``com.amazonaws.qconnect#SpanCitationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.span_citation

SpanCitationList: TypeAlias = list["aws_sdk_qconnect.types.span_citation.SpanCitation"]


# --- restJson1 ser/de ---
def serialize_json(value: SpanCitationList) -> list:
    import aws_sdk_qconnect.types.span_citation

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.span_citation.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpanCitationList:
    import aws_sdk_qconnect.types.span_citation

    out: SpanCitationList = []
    for item in data:
        out.append(aws_sdk_qconnect.types.span_citation.deserialize_json(item))
    return out
