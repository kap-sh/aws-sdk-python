"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultCustomDocumentLocation``."""

from typing_extensions import NotRequired, TypedDict


class RetrievalResultCustomDocumentLocation(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID of the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultCustomDocumentLocation) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> RetrievalResultCustomDocumentLocation:
    out: RetrievalResultCustomDocumentLocation = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    return out
