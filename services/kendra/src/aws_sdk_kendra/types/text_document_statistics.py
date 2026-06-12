"""Generated from Smithy shape ``com.amazonaws.kendra#TextDocumentStatistics``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.indexed_text_bytes
    import aws_sdk_kendra.types.indexed_text_documents_count


class TextDocumentStatistics(TypedDict):
    indexed_text_documents_count: (
        "aws_sdk_kendra.types.indexed_text_documents_count.IndexedTextDocumentsCount"
    )
    """<p>The number of text documents indexed.</p>"""
    indexed_text_bytes: "aws_sdk_kendra.types.indexed_text_bytes.IndexedTextBytes"
    """<p>The total size, in bytes, of the indexed documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextDocumentStatistics) -> dict:
    out: dict = {}
    out["IndexedTextDocumentsCount"] = value.get("indexed_text_documents_count", 0)
    out["IndexedTextBytes"] = value.get("indexed_text_bytes", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TextDocumentStatistics:
    out: TextDocumentStatistics = {}  # type: ignore[typeddict-item]
    if "IndexedTextDocumentsCount" in data:
        out["indexed_text_documents_count"] = data["IndexedTextDocumentsCount"]
    else:
        out["indexed_text_documents_count"] = 0
    if "IndexedTextBytes" in data:
        out["indexed_text_bytes"] = data["IndexedTextBytes"]
    else:
        out["indexed_text_bytes"] = 0
    return out
