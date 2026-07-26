"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteRecommenderFilterResponse``."""

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError


class DeleteRecommenderFilterResponse(TypedDict, closed=True):
    message: "str"
    """<p>A message that indicates the delete request is done.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecommenderFilterResponse) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteRecommenderFilterResponse:
    out: DeleteRecommenderFilterResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("DeleteRecommenderFilterResponse.message required")
    return out
