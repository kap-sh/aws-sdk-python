"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#PutKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront_keyvaluestore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.etag


class PutKeyResponse(TypedDict, closed=True):
    item_count: "int"
    """<p>Number of key value pairs in the Key Value Store after the successful put.</p>"""
    total_size_in_bytes: "int"
    """<p>Total size of the Key Value Store after the successful put, in bytes.</p>"""
    e_tag: "capo_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The current version identifier of the Key Value Store after the successful put.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutKeyResponse) -> dict:
    out: dict = {}
    out["ItemCount"] = value["item_count"]
    out["TotalSizeInBytes"] = value["total_size_in_bytes"]
    return out


def deserialize_json(data: dict) -> PutKeyResponse:
    out: PutKeyResponse = {}  # type: ignore[typeddict-item]
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    else:
        raise DeserializationError("PutKeyResponse.item_count required")
    if "TotalSizeInBytes" in data:
        out["total_size_in_bytes"] = data["TotalSizeInBytes"]
    else:
        raise DeserializationError("PutKeyResponse.total_size_in_bytes required")
    return out
