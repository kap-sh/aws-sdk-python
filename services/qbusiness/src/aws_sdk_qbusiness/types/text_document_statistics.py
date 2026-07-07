"""Generated from Smithy shape ``com.amazonaws.qbusiness#TextDocumentStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.indexed_text_bytes
    import aws_sdk_qbusiness.types.indexed_text_document


class TextDocumentStatistics(TypedDict, closed=True):
    indexed_text_bytes: NotRequired[
        "aws_sdk_qbusiness.types.indexed_text_bytes.IndexedTextBytes"
    ]
    """<p>The total size, in bytes, of the indexed documents.</p>"""
    indexed_text_document_count: NotRequired[
        "aws_sdk_qbusiness.types.indexed_text_document.IndexedTextDocument"
    ]
    """<p>The number of text documents indexed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextDocumentStatistics) -> dict:
    out: dict = {}
    if "indexed_text_bytes" in value:
        out["indexedTextBytes"] = value["indexed_text_bytes"]
    if "indexed_text_document_count" in value:
        out["indexedTextDocumentCount"] = value["indexed_text_document_count"]
    return out


def deserialize_json(data: dict) -> TextDocumentStatistics:
    out: TextDocumentStatistics = {}  # type: ignore[typeddict-item]
    if "indexedTextBytes" in data:
        out["indexed_text_bytes"] = data["indexedTextBytes"]
    if "indexedTextDocumentCount" in data:
        out["indexed_text_document_count"] = data["indexedTextDocumentCount"]
    return out
