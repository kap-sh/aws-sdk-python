"""Generated from Smithy shape ``com.amazonaws.geomaps#GetGlyphsResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetGlyphsResponse(TypedDict, closed=True):
    blob: NotRequired["bytes"]
    """<p>The Glyph, as a binary blob.</p>"""
    content_type: NotRequired["str"]
    """<p>Header that represents the format of the response. The response returns the following as the HTTP body.</p>"""
    cache_control: NotRequired["str"]
    """<p>Header that instructs caching configuration for the client.</p>"""
    e_tag: NotRequired["str"]
    """<p>The glyph's Etag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlyphsResponse) -> dict:
    out: dict = {}
    if "blob" in value:
        import aws_sdk_geo_maps.types._prelude.blob

        out["Blob"] = aws_sdk_geo_maps.types._prelude.blob.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> GetGlyphsResponse:
    out: GetGlyphsResponse = {}  # type: ignore[typeddict-item]
    if "Blob" in data:
        import aws_sdk_geo_maps.types._prelude.blob

        out["blob"] = aws_sdk_geo_maps.types._prelude.blob.deserialize_json(
            data["Blob"]
        )
    return out
