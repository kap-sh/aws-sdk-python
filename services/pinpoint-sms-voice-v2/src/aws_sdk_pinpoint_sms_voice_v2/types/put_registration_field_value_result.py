"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutRegistrationFieldValueResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.field_path
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_number
    import aws_sdk_pinpoint_sms_voice_v2.types.select_choice_list
    import aws_sdk_pinpoint_sms_voice_v2.types.text_value


class PutRegistrationFieldValueResult(TypedDict):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    version_number: "aws_sdk_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    """<p>The version number of the registration.</p>"""
    field_path: "aws_sdk_pinpoint_sms_voice_v2.types.field_path.FieldPath"
    """<p>The path to the registration form field. You can use <a>DescribeRegistrationFieldDefinitions</a> for a list of <b>FieldPaths</b>.</p>"""
    select_choices: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.select_choice_list.SelectChoiceList"
    ]
    """<p>An array of values for the form field.</p>"""
    text_value: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.text_value.TextValue"]
    """<p>The text data for a free form field.</p>"""
    registration_attachment_id: NotRequired["str"]
    """<p>The unique identifier for the registration attachment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutRegistrationFieldValueResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    out["VersionNumber"] = value["version_number"]
    out["FieldPath"] = value["field_path"]
    if "select_choices" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.select_choice_list

        out["SelectChoices"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.select_choice_list.serialize_aws_json_1_0(
                value["select_choices"]
            )
        )
    if "text_value" in value:
        out["TextValue"] = value["text_value"]
    if "registration_attachment_id" in value:
        out["RegistrationAttachmentId"] = value["registration_attachment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutRegistrationFieldValueResult:
    out: PutRegistrationFieldValueResult = {}  # type: ignore[typeddict-item]
    if "RegistrationArn" in data:
        out["registration_arn"] = data["RegistrationArn"]
    else:
        raise DeserializationError(
            "PutRegistrationFieldValueResult.registration_arn required"
        )
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "PutRegistrationFieldValueResult.registration_id required"
        )
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    else:
        raise DeserializationError(
            "PutRegistrationFieldValueResult.version_number required"
        )
    if "FieldPath" in data:
        out["field_path"] = data["FieldPath"]
    else:
        raise DeserializationError(
            "PutRegistrationFieldValueResult.field_path required"
        )
    if "SelectChoices" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.select_choice_list

        out["select_choices"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.select_choice_list.deserialize_aws_json_1_0(
                data["SelectChoices"]
            )
        )
    if "TextValue" in data:
        out["text_value"] = data["TextValue"]
    if "RegistrationAttachmentId" in data:
        out["registration_attachment_id"] = data["RegistrationAttachmentId"]
    return out
