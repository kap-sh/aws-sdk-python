"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#UpdateKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront_keyvaluestore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront_keyvaluestore.types.etag


class UpdateKeysResponse(TypedDict, closed=True):
    item_count: "int"
    """<p>Number of key value pairs in the Key Value Store after the successful update.</p>"""
    total_size_in_bytes: "int"
    """<p>Total size of the Key Value Store after the successful update, in bytes.</p>"""
    e_tag: "aws_sdk_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The current version identifier of the Key Value Store after the successful update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKeysResponse) -> dict:
    out: dict = {}
    out["ItemCount"] = value["item_count"]
    out["TotalSizeInBytes"] = value["total_size_in_bytes"]
    return out


def deserialize_json(data: dict) -> UpdateKeysResponse:
    out: UpdateKeysResponse = {}  # type: ignore[typeddict-item]
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    else:
        raise DeserializationError("UpdateKeysResponse.item_count required")
    if "TotalSizeInBytes" in data:
        out["total_size_in_bytes"] = data["TotalSizeInBytes"]
    else:
        raise DeserializationError("UpdateKeysResponse.total_size_in_bytes required")
    return out
