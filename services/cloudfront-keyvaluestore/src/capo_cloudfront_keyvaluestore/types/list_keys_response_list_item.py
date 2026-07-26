"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#ListKeysResponseListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront_keyvaluestore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.key
    import capo_cloudfront_keyvaluestore.types.value


class ListKeysResponseListItem(TypedDict, closed=True):
    key: "capo_cloudfront_keyvaluestore.types.key.Key"
    """<p>The key of the key value pair.</p>"""
    value: "capo_cloudfront_keyvaluestore.types.value.Value"
    """<p>The value of the key value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKeysResponseListItem) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ListKeysResponseListItem:
    out: ListKeysResponseListItem = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("ListKeysResponseListItem.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("ListKeysResponseListItem.value required")
    return out
