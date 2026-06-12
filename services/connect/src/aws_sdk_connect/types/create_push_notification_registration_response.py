"""Generated from Smithy shape ``com.amazonaws.connect#CreatePushNotificationRegistrationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.registration_id


class CreatePushNotificationRegistrationResponse(TypedDict):
    registration_id: "aws_sdk_connect.types.registration_id.RegistrationId"
    """<p>The identifier for the registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePushNotificationRegistrationResponse) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    return out


def deserialize_json(data: dict) -> CreatePushNotificationRegistrationResponse:
    out: CreatePushNotificationRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "CreatePushNotificationRegistrationResponse.registration_id required"
        )
    return out
