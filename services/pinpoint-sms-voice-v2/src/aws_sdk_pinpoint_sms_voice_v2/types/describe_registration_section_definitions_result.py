"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationSectionDefinitionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_section_definition_list
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type


class DescribeRegistrationSectionDefinitionsResult(TypedDict):
    registration_type: (
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    registration_section_definitions: "aws_sdk_pinpoint_sms_voice_v2.types.registration_section_definition_list.RegistrationSectionDefinitionList"
    """<p>An array of RegistrationSectionDefinition objects.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationSectionDefinitionsResult) -> dict:
    out: dict = {}
    out["RegistrationType"] = value["registration_type"]
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_section_definition_list

    out["RegistrationSectionDefinitions"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.registration_section_definition_list.serialize_aws_json_1_0(
            value["registration_section_definitions"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DescribeRegistrationSectionDefinitionsResult:
    out: DescribeRegistrationSectionDefinitionsResult = {}  # type: ignore[typeddict-item]
    if "RegistrationType" in data:
        out["registration_type"] = data["RegistrationType"]
    else:
        raise DeserializationError(
            "DescribeRegistrationSectionDefinitionsResult.registration_type required"
        )
    if "RegistrationSectionDefinitions" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_section_definition_list

        out["registration_section_definitions"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_section_definition_list.deserialize_aws_json_1_0(
                data["RegistrationSectionDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeRegistrationSectionDefinitionsResult.registration_section_definitions required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
