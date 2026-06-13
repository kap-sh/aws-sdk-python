"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteRegistrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn


class DeleteRegistrationRequest(TypedDict):
    registration_id: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRegistrationRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRegistrationRequest:
    out: DeleteRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError("DeleteRegistrationRequest.registration_id required")
    return out
