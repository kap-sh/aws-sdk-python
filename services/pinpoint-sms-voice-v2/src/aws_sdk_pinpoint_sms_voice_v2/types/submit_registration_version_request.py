"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SubmitRegistrationVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn


class SubmitRegistrationVersionRequest(TypedDict):
    registration_id: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""
    aws_review: "bool"
    """<p>Set to true to request AWS review of the registration. When enabled, AWS will perform additional validation and review of the registration submission before processing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubmitRegistrationVersionRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    out["AwsReview"] = value.get("aws_review", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> SubmitRegistrationVersionRequest:
    out: SubmitRegistrationVersionRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "SubmitRegistrationVersionRequest.registration_id required"
        )
    if "AwsReview" in data:
        out["aws_review"] = data["AwsReview"]
    else:
        out["aws_review"] = False
    return out
