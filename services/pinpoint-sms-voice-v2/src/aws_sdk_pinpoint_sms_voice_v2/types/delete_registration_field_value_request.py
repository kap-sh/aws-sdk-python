"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteRegistrationFieldValueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.field_path
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn


class DeleteRegistrationFieldValueRequest(TypedDict):
    registration_id: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_id_or_arn.RegistrationIdOrArn"
    )
    """<p>The unique identifier for the registration.</p>"""
    field_path: "aws_sdk_pinpoint_sms_voice_v2.types.field_path.FieldPath"
    """<p>The path to the registration form field. You can use <a>DescribeRegistrationFieldDefinitions</a> for a list of <b>FieldPaths</b>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRegistrationFieldValueRequest) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    out["FieldPath"] = value["field_path"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRegistrationFieldValueRequest:
    out: DeleteRegistrationFieldValueRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "DeleteRegistrationFieldValueRequest.registration_id required"
        )
    if "FieldPath" in data:
        out["field_path"] = data["FieldPath"]
    else:
        raise DeserializationError(
            "DeleteRegistrationFieldValueRequest.field_path required"
        )
    return out
