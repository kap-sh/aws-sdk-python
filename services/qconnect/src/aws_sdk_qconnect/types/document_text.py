"""Generated from Smithy shape ``com.amazonaws.qconnect#DocumentText``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.highlights
    import aws_sdk_qconnect.types.sensitive_string


class DocumentText(TypedDict):
    text: NotRequired["aws_sdk_qconnect.types.sensitive_string.SensitiveString"]
    """<p>Text in the document.</p>"""
    highlights: NotRequired["aws_sdk_qconnect.types.highlights.Highlights"]
    """<p>Highlights in the document text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentText) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "highlights" in value:
        import aws_sdk_qconnect.types.highlights

        out["highlights"] = aws_sdk_qconnect.types.highlights.serialize_json(
            value["highlights"]
        )
    return out


def deserialize_json(data: dict) -> DocumentText:
    out: DocumentText = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    if "highlights" in data:
        import aws_sdk_qconnect.types.highlights

        out["highlights"] = aws_sdk_qconnect.types.highlights.deserialize_json(
            data["highlights"]
        )
    return out
