"""Generated from Smithy shape ``com.amazonaws.location#GetMapStyleDescriptorResponse``."""

from typing_extensions import NotRequired, TypedDict


class GetMapStyleDescriptorResponse(TypedDict, closed=True):
    blob: NotRequired["bytes"]
    """<p>Contains the body of the style descriptor.</p>"""
    content_type: NotRequired["str"]
    """<p>The style descriptor's content type. For example, <code>application/json</code>.</p>"""
    cache_control: NotRequired["str"]
    """<p>The HTTP Cache-Control directive for the value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMapStyleDescriptorResponse) -> dict:
    out: dict = {}
    if "blob" in value:
        import capo_location.types._prelude.blob

        out["Blob"] = capo_location.types._prelude.blob.serialize_json(value["blob"])
    return out


def deserialize_json(data: dict) -> GetMapStyleDescriptorResponse:
    out: GetMapStyleDescriptorResponse = {}  # type: ignore[typeddict-item]
    if "Blob" in data:
        import capo_location.types._prelude.blob

        out["blob"] = capo_location.types._prelude.blob.deserialize_json(data["Blob"])
    return out
