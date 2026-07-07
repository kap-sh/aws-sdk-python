"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#PutKeyRequestListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront_keyvaluestore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront_keyvaluestore.types.key
    import aws_sdk_cloudfront_keyvaluestore.types.value


class PutKeyRequestListItem(TypedDict, closed=True):
    key: "aws_sdk_cloudfront_keyvaluestore.types.key.Key"
    """<p>The key of the key value pair list item to put.</p>"""
    value: "aws_sdk_cloudfront_keyvaluestore.types.value.Value"
    """<p>The value for the key value pair to put.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutKeyRequestListItem) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PutKeyRequestListItem:
    out: PutKeyRequestListItem = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("PutKeyRequestListItem.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("PutKeyRequestListItem.value required")
    return out
