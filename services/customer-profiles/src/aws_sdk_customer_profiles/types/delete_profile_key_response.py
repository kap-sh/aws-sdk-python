"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteProfileKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.message


class DeleteProfileKeyResponse(TypedDict):
    message: NotRequired["aws_sdk_customer_profiles.types.message.message"]
    """<p>A message that indicates the delete request is done.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProfileKeyResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteProfileKeyResponse:
    out: DeleteProfileKeyResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
