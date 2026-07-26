"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#DocumentPageLocation``."""

from typing_extensions import NotRequired, TypedDict


class DocumentPageLocation(TypedDict, closed=True):
    document_index: NotRequired["int"]
    """<p>The index of the document within the array of documents provided in the request.</p>"""
    start: NotRequired["int"]
    """<p>The starting page number of the cited content within the document.</p>"""
    end: NotRequired["int"]
    """<p>The ending page number of the cited content within the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentPageLocation) -> dict:
    out: dict = {}
    if "document_index" in value:
        out["documentIndex"] = value["document_index"]
    if "start" in value:
        out["start"] = value["start"]
    if "end" in value:
        out["end"] = value["end"]
    return out


def deserialize_json(data: dict) -> DocumentPageLocation:
    out: DocumentPageLocation = {}  # type: ignore[typeddict-item]
    if "documentIndex" in data:
        out["document_index"] = data["documentIndex"]
    if "start" in data:
        out["start"] = data["start"]
    if "end" in data:
        out["end"] = data["end"]
    return out
