"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultSharePointLocation``."""

from typing_extensions import NotRequired, TypedDict


class RetrievalResultSharePointLocation(TypedDict, closed=True):
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
