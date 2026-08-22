"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RerankTextDocument``."""

from typing_extensions import NotRequired, TypedDict


class RerankTextDocument(TypedDict, closed=True):
    text: NotRequired["str"]
    """<p>The text of the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RerankTextDocument) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> RerankTextDocument:
    out: RerankTextDocument = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out
