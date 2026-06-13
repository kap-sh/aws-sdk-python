"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultSharePointLocation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RetrievalResultSharePointLocation(TypedDict):
    url: NotRequired["str"]
    """<p>The SharePoint site URL for the data source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultSharePointLocation) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RetrievalResultSharePointLocation:
    out: RetrievalResultSharePointLocation = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out
