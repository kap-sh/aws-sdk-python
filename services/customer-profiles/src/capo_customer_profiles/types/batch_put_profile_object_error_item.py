"""Generated from Smithy shape ``com.amazonaws.customerprofiles#BatchPutProfileObjectErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.response_code
    import capo_customer_profiles.types.text


class BatchPutProfileObjectErrorItem(TypedDict, closed=True):
    id: "capo_customer_profiles.types.name.name"
    """<p>The unique identifier of the item in the batch request that failed.</p>"""
    code: "capo_customer_profiles.types.response_code.responseCode"
    """<p>The HTTP status code for the error.</p>"""
    message: NotRequired["capo_customer_profiles.types.text.text"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutProfileObjectErrorItem) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchPutProfileObjectErrorItem:
    out: BatchPutProfileObjectErrorItem = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("BatchPutProfileObjectErrorItem.id required")
    if "Code" in data:
        out["code"] = data["Code"]
    else:
        raise DeserializationError("BatchPutProfileObjectErrorItem.code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out
