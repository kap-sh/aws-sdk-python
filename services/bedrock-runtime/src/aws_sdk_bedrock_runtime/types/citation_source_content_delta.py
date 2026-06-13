"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CitationSourceContentDelta``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CitationSourceContentDelta(TypedDict):
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
    if "text" in data:
        out["text"] = data["text"]
    return out
