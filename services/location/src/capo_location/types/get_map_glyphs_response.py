"""Generated from Smithy shape ``com.amazonaws.location#GetMapGlyphsResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetMapGlyphsResponse(TypedDict, closed=True):
    blob: NotRequired["bytes"]
    """<p>The glyph, as binary blob.</p>"""
    content_type: NotRequired["str"]
    """<p>The map glyph content type. For example, <code>application/octet-stream</code>.</p>"""
    cache_control: NotRequired["str"]
    """<p>The HTTP Cache-Control directive for the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMapGlyphsResponse) -> dict:
    out: dict = {}
    if "blob" in value:
        import capo_location.types._prelude.blob

        out["Blob"] = capo_location.types._prelude.blob.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> GetMapGlyphsResponse:
    out: GetMapGlyphsResponse = {}  # type: ignore[typeddict-item]
    if "Blob" in data:
        import capo_location.types._prelude.blob

        out["blob"] = capo_location.types._prelude.blob.deserialize_json(data["Blob"])
    return out
