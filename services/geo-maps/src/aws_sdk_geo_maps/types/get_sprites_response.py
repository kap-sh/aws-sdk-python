"""Generated from Smithy shape ``com.amazonaws.geomaps#GetSpritesResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetSpritesResponse(TypedDict, closed=True):
    blob: NotRequired["bytes"]
    """<p>The body of the sprite sheet or JSON offset file (image/png or application/json, depending on input).</p>"""
    content_type: NotRequired["str"]
    """<p>Header that represents the format of the response. The response returns the following as the HTTP body.</p>"""
    cache_control: NotRequired["str"]
    """<p>Header that instructs caching configuration for the client.</p>"""
    e_tag: NotRequired["str"]
    """<p>The sprite's Etag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpritesResponse) -> dict:
    out: dict = {}
    if "blob" in value:
        import aws_sdk_geo_maps.types._prelude.blob

        out["Blob"] = aws_sdk_geo_maps.types._prelude.blob.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> GetSpritesResponse:
    out: GetSpritesResponse = {}  # type: ignore[typeddict-item]
    if "Blob" in data:
        import aws_sdk_geo_maps.types._prelude.blob

        out["blob"] = aws_sdk_geo_maps.types._prelude.blob.deserialize_json(
            data["Blob"]
        )
    return out
