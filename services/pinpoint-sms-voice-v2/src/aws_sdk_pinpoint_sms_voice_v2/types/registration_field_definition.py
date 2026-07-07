"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationFieldDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.field_path
    import aws_sdk_pinpoint_sms_voice_v2.types.field_requirement
    import aws_sdk_pinpoint_sms_voice_v2.types.field_type
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_field_display_hints
    import aws_sdk_pinpoint_sms_voice_v2.types.section_path
    import aws_sdk_pinpoint_sms_voice_v2.types.select_validation
    import aws_sdk_pinpoint_sms_voice_v2.types.text_validation


class RegistrationFieldDefinition(TypedDict, closed=True):
    section_path: "aws_sdk_pinpoint_sms_voice_v2.types.section_path.SectionPath"
    """<p>The section path of the field.</p>"""
    field_path: "aws_sdk_pinpoint_sms_voice_v2.types.field_path.FieldPath"
    """<p>The path to the registration form field. You can use <a>DescribeRegistrationFieldDefinitions</a> for a list of <b>FieldPaths</b>.</p>"""
    field_type: "aws_sdk_pinpoint_sms_voice_v2.types.field_type.FieldType"
    """<p>The type of field.</p>"""
    field_requirement: (
        "aws_sdk_pinpoint_sms_voice_v2.types.field_requirement.FieldRequirement"
    )
    """<p>Specifies if the field for the registration form is required, conditional or optional.</p>"""
    select_validation: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.select_validation.SelectValidation"
    ]
    """<p>The validation rules for a select field.</p>"""
    text_validation: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.text_validation.TextValidation"
    ]
    """<p>The validation rules for a text field.</p>"""
    display_hints: "aws_sdk_pinpoint_sms_voice_v2.types.registration_field_display_hints.RegistrationFieldDisplayHints"
    """<p>An array of RegistrationFieldDisplayHints objects for the field.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationFieldDefinition) -> dict:
    out: dict = {}
    out["SectionPath"] = value["section_path"]
    out["FieldPath"] = value["field_path"]
    out["FieldType"] = value["field_type"]
    out["FieldRequirement"] = value["field_requirement"]
    if "select_validation" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.select_validation

        out["SelectValidation"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.select_validation.serialize_aws_json_1_0(
                value["select_validation"]
            )
        )
    if "text_validation" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.text_validation

        out["TextValidation"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.text_validation.serialize_aws_json_1_0(
                value["text_validation"]
            )
        )
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_field_display_hints

    out["DisplayHints"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.registration_field_display_hints.serialize_aws_json_1_0(
            value["display_hints"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationFieldDefinition:
    out: RegistrationFieldDefinition = {}  # type: ignore[typeddict-item]
    if "SectionPath" in data:
        out["section_path"] = data["SectionPath"]
    else:
        raise DeserializationError("RegistrationFieldDefinition.section_path required")
    if "FieldPath" in data:
        out["field_path"] = data["FieldPath"]
    else:
        raise DeserializationError("RegistrationFieldDefinition.field_path required")
    if "FieldType" in data:
        out["field_type"] = data["FieldType"]
    else:
        raise DeserializationError("RegistrationFieldDefinition.field_type required")
    if "FieldRequirement" in data:
        out["field_requirement"] = data["FieldRequirement"]
    else:
        raise DeserializationError(
            "RegistrationFieldDefinition.field_requirement required"
        )
    if "SelectValidation" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.select_validation

        out["select_validation"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.select_validation.deserialize_aws_json_1_0(
                data["SelectValidation"]
            )
        )
    if "TextValidation" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.text_validation

        out["text_validation"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.text_validation.deserialize_aws_json_1_0(
                data["TextValidation"]
            )
        )
    if "DisplayHints" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_field_display_hints

        out["display_hints"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_field_display_hints.deserialize_aws_json_1_0(
                data["DisplayHints"]
            )
        )
    else:
        raise DeserializationError("RegistrationFieldDefinition.display_hints required")
    return out
