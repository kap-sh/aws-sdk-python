"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentChunkLocation``."""

from typing_extensions import NotRequired, TypedDict


class DocumentChunkLocation(TypedDict, closed=True):
    document_index: NotRequired["int"]
    """<p>The index of the document within the array of documents provided in the request.</p>"""
    start: NotRequired["int"]
    """<p>The starting chunk identifier or index of the cited content within the document.</p>"""
    end: NotRequired["int"]
    """<p>The ending chunk identifier or index of the cited content within the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentChunkLocation) -> dict:
    out: dict = {}
    if "document_index" in value:
        out["documentIndex"] = value["document_index"]
    if "start" in value:
        out["start"] = value["start"]
    if "end" in value:
        out["end"] = value["end"]
    return out


def deserialize_json(data: dict) -> DocumentChunkLocation:
    out: DocumentChunkLocation = {}  # type: ignore[typeddict-item]
    if "documentIndex" in data:
        out["document_index"] = data["documentIndex"]
    if "start" in data:
        out["start"] = data["start"]
    if "end" in data:
        out["end"] = data["end"]
    return out
