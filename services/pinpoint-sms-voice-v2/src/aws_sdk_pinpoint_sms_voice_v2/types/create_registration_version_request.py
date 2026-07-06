"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateRegistrationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn


class CreateRegistrationVersionRequest(TypedDict, closed=True):
    registration_id: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRegistrationVersionRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRegistrationVersionRequest:
    out: CreateRegistrationVersionRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "CreateRegistrationVersionRequest.registration_id required"
        )
    return out
