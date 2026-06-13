"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultConfluenceLocation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RetrievalResultConfluenceLocation(TypedDict):
    url: NotRequired["str"]
    """<p>The Confluence host URL for the data source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultConfluenceLocation) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RetrievalResultConfluenceLocation:
    out: RetrievalResultConfluenceLocation = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out
