"""Generated from Smithy shape ``com.amazonaws.xray#Span``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.span_document
    import aws_sdk_xray.types.span_id


class Span(TypedDict):
    id: NotRequired["aws_sdk_xray.types.span_id.SpanId"]
    """<p>The span ID.</p>"""
    document: NotRequired["aws_sdk_xray.types.span_document.SpanDocument"]
    """<p> The span document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Span) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "document" in value:
        out["Document"] = value["document"]
    return out


def deserialize_json(data: dict) -> Span:
    out: Span = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Document" in data:
        out["document"] = data["Document"]
    return out
