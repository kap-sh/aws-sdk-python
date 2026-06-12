"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteDomainLayoutResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.message


class DeleteDomainLayoutResponse(TypedDict):
    message: "aws_sdk_customer_profiles.types.message.message"
    """<p>A message that indicates the delete request is done.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainLayoutResponse) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteDomainLayoutResponse:
    out: DeleteDomainLayoutResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("DeleteDomainLayoutResponse.message required")
    return out
