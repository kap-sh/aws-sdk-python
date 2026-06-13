"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultKendraDocumentLocation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RetrievalResultKendraDocumentLocation(TypedDict):
    uri: NotRequired["str"]
    """<p>The document's uri.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultKendraDocumentLocation) -> dict:
    out: dict = {}
    if "uri" in value:
        out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> RetrievalResultKendraDocumentLocation:
    out: RetrievalResultKendraDocumentLocation = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    return out
