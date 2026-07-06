"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteProfileObjectTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.message


class DeleteProfileObjectTypeResponse(TypedDict, closed=True):
    message: "aws_sdk_customer_profiles.types.message.message"
    """<p>A message that indicates the delete request is done.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileObjectTypeResponse) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteProfileObjectTypeResponse:
    out: DeleteProfileObjectTypeResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("DeleteProfileObjectTypeResponse.message required")
    return out
