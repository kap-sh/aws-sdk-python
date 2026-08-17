"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationSourceContentDelta``."""

from typing_extensions import NotRequired, TypedDict


class CitationSourceContentDelta(TypedDict, closed=True):
    text: NotRequired["str"]
    """<p>An incremental update to the text content from the source document that is being cited.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CitationSourceContentDelta) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> CitationSourceContentDelta:
    out: CitationSourceContentDelta = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out
