"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchPutProfileObjectRequestItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.stringified_json


class BatchPutProfileObjectRequestItem(TypedDict, closed=True):
    id: "capo_customer_profiles.types.name.name"
    """<p>A unique identifier for this item in the batch request. Used to correlate items in the response.</p>"""
    object: "capo_customer_profiles.types.stringified_json.stringifiedJson"
    """<p>A string that is serialized from a JSON object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutProfileObjectRequestItem) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Object"] = value["object"]
    return out


def deserialize_json(data: dict) -> BatchPutProfileObjectRequestItem:
    out: BatchPutProfileObjectRequestItem = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("BatchPutProfileObjectRequestItem.id required")
    if "Object" in data:
        out["object"] = data["Object"]
    else:
        raise DeserializationError("BatchPutProfileObjectRequestItem.object required")
    return out
