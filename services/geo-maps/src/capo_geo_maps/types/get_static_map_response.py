"""Generated from Smithy shape ``com.amazonaws.geomaps#GetStaticMapResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetStaticMapResponse(TypedDict, closed=True):
    blob: NotRequired["bytes"]
    """<p>The blob represents a map image as a <code>jpeg</code> for the <code>GetStaticMap</code> API.</p>"""
    content_type: NotRequired["str"]
    """<p>Header that represents the format of the response. The response returns the following as the HTTP body.</p>"""
    cache_control: NotRequired["str"]
    """<p>Header that instructs caching configuration for the client.</p>"""
    e_tag: NotRequired["str"]
    """<p>The static map's Etag.</p>"""
    pricing_bucket: "str"
    """<p>The pricing bucket for which the request is charged at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStaticMapResponse) -> dict:
    out: dict = {}
    if "blob" in value:
        import capo_geo_maps.types._prelude.blob

        out["Blob"] = capo_geo_maps.types._prelude.blob.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> GetStaticMapResponse:
    out: GetStaticMapResponse = {}  # type: ignore[typeddict-item]
    if "Blob" in data:
        import capo_geo_maps.types._prelude.blob

        out["blob"] = capo_geo_maps.types._prelude.blob.deserialize_json(data["Blob"])
    return out
