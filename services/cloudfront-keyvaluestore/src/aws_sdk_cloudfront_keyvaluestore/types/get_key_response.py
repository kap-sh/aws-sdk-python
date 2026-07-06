"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#GetKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront_keyvaluestore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront_keyvaluestore.types.key
    import aws_sdk_cloudfront_keyvaluestore.types.value


class GetKeyResponse(TypedDict, closed=True):
    key: "aws_sdk_cloudfront_keyvaluestore.types.key.Key"
    """<p>The key of the key value pair.</p>"""
    value: "aws_sdk_cloudfront_keyvaluestore.types.value.Value"
    """<p>The value of the key value pair.</p>"""
    item_count: "int"
    """<p>Number of key value pairs in the Key Value Store.</p>"""
    total_size_in_bytes: "int"
    """<p>Total size of the Key Value Store in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKeyResponse) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    out["ItemCount"] = value["item_count"]
    out["TotalSizeInBytes"] = value["total_size_in_bytes"]
    return out


def deserialize_json(data: dict) -> GetKeyResponse:
    out: GetKeyResponse = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("GetKeyResponse.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("GetKeyResponse.value required")
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    else:
        raise DeserializationError("GetKeyResponse.item_count required")
    if "TotalSizeInBytes" in data:
        out["total_size_in_bytes"] = data["TotalSizeInBytes"]
    else:
        raise DeserializationError("GetKeyResponse.total_size_in_bytes required")
    return out
