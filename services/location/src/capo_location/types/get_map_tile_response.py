"""Generated from Smithy shape ``com.amazonaws.location#GetMapTileResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetMapTileResponse(TypedDict, closed=True):
    blob: NotRequired["bytes"]
    """<p>Contains Mapbox Vector Tile (MVT) data.</p>"""
    content_type: NotRequired["str"]
    """<p>The map tile's content type. For example, <code>application/vnd.mapbox-vector-tile</code>.</p>"""
    cache_control: NotRequired["str"]
    """<p>The HTTP Cache-Control directive for the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMapTileResponse) -> dict:
    out: dict = {}
    if "blob" in value:
        import capo_location.types._prelude.blob

        out["Blob"] = capo_location.types._prelude.blob.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> GetMapTileResponse:
    out: GetMapTileResponse = {}  # type: ignore[typeddict-item]
    if "Blob" in data:
        import capo_location.types._prelude.blob

        out["blob"] = capo_location.types._prelude.blob.deserialize_json(data["Blob"])
    return out
