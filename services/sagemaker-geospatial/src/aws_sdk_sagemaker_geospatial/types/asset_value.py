"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#AssetValue``."""

from typing import TypedDict
from typing_extensions import NotRequired

class AssetValue(TypedDict):
    href: NotRequired["str"]
    """<p>Link to the asset object.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssetValue) -> dict:
    out: dict = {}
    if "href" in value:
        out["Href"] = value["href"]
    return out


def deserialize_json(data: dict) -> AssetValue:
    out: AssetValue = {}  # type: ignore[typeddict-item]
    if "Href" in data:
        out["href"] = data["Href"]
    return out