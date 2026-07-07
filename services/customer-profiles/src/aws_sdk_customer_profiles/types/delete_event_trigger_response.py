"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DeleteEventTriggerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.message


class DeleteEventTriggerResponse(TypedDict, closed=True):
    message: "aws_sdk_customer_profiles.types.message.message"
    """<p>A message that indicates the delete request is done.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventTriggerResponse) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteEventTriggerResponse:
    out: DeleteEventTriggerResponse = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("DeleteEventTriggerResponse.message required")
    return out
