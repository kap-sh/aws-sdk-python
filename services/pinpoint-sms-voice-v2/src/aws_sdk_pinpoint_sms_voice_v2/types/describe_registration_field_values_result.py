"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationFieldValuesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information_list
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_number


class DescribeRegistrationFieldValuesResult(TypedDict):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    version_number: "aws_sdk_pinpoint_sms_voice_v2.types.registration_version_number.RegistrationVersionNumber"
    """<p>The current version of the registration.</p>"""
    registration_field_values: "aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information_list.RegistrationFieldValueInformationList"
    """<p>An array of RegistrationFieldValues objects that contain the values for the requested registration. </p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationFieldValuesResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    out["VersionNumber"] = value["version_number"]
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information_list

    out["RegistrationFieldValues"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information_list.serialize_aws_json_1_0(
            value["registration_field_values"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationFieldValuesResult:
    out: DescribeRegistrationFieldValuesResult = {}  # type: ignore[typeddict-item]
    if "RegistrationArn" in data:
        out["registration_arn"] = data["RegistrationArn"]
    else:
        raise DeserializationError(
            "DescribeRegistrationFieldValuesResult.registration_arn required"
        )
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "DescribeRegistrationFieldValuesResult.registration_id required"
        )
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    else:
        raise DeserializationError(
            "DescribeRegistrationFieldValuesResult.version_number required"
        )
    if "RegistrationFieldValues" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information_list

        out["registration_field_values"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_field_value_information_list.deserialize_aws_json_1_0(
                data["RegistrationFieldValues"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeRegistrationFieldValuesResult.registration_field_values required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
