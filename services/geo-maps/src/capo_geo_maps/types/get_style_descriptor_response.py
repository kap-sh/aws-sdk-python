"""Generated from Smithy shape ``com.amazonaws.geomaps#GetStyleDescriptorResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetStyleDescriptorResponse(TypedDict, closed=True):
    blob: NotRequired["bytes"]
    """<p>This Blob contains the body of the style descriptor which is in application/json format.</p>"""
    content_type: NotRequired["str"]
    """<p>Header that represents the format of the response. The response returns the following as the HTTP body.</p>"""
    cache_control: NotRequired["str"]
    """<p>Header that instructs caching configuration for the client.</p>"""
    e_tag: NotRequired["str"]
    """<p>The style descriptor's Etag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStyleDescriptorResponse) -> dict:
    out: dict = {}
    if "blob" in value:
        import capo_geo_maps.types._prelude.blob

        out["Blob"] = capo_geo_maps.types._prelude.blob.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> GetStyleDescriptorResponse:
    out: GetStyleDescriptorResponse = {}  # type: ignore[typeddict-item]
    if "Blob" in data:
        import capo_geo_maps.types._prelude.blob

        out["blob"] = capo_geo_maps.types._prelude.blob.deserialize_json(data["Blob"])
    return out
