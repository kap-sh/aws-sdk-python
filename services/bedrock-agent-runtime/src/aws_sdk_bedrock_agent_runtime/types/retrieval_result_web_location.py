"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultWebLocation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RetrievalResultWebLocation(TypedDict):
    url: NotRequired["str"]
    """<p>The web URL/URLs for the data source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultWebLocation) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RetrievalResultWebLocation:
    out: RetrievalResultWebLocation = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out
