"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#DeleteKeyRequestListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront_keyvaluestore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.key


class DeleteKeyRequestListItem(TypedDict, closed=True):
    key: "capo_cloudfront_keyvaluestore.types.key.Key"
    """<p>The key of the key value pair to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKeyRequestListItem) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    return out


def deserialize_json(data: dict) -> DeleteKeyRequestListItem:
    out: DeleteKeyRequestListItem = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("DeleteKeyRequestListItem.key required")
    return out
