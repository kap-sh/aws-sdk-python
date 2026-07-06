"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationTypeDefinitionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition_list


class DescribeRegistrationTypeDefinitionsResult(TypedDict, closed=True):
    registration_type_definitions: "aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition_list.RegistrationTypeDefinitionList"
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationTypeDefinitionsResult) -> dict:
    out: dict = {}
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition_list

    out["RegistrationTypeDefinitions"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition_list.serialize_aws_json_1_0(
            value["registration_type_definitions"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationTypeDefinitionsResult:
    out: DescribeRegistrationTypeDefinitionsResult = {}  # type: ignore[typeddict-item]
    if "RegistrationTypeDefinitions" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition_list

        out["registration_type_definitions"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_type_definition_list.deserialize_aws_json_1_0(
                data["RegistrationTypeDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeRegistrationTypeDefinitionsResult.registration_type_definitions required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
