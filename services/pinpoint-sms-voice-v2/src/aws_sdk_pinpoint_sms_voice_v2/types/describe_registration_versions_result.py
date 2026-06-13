"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationVersionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information_list


class DescribeRegistrationVersionsResult(TypedDict):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    registration_versions: "aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information_list.RegistrationVersionInformationList"
    """<p>An array of RegistrationVersions objects.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationVersionsResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information_list

    out["RegistrationVersions"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information_list.serialize_aws_json_1_0(
            value["registration_versions"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationVersionsResult:
    out: DescribeRegistrationVersionsResult = {}  # type: ignore[typeddict-item]
    if "RegistrationArn" in data:
        out["registration_arn"] = data["RegistrationArn"]
    else:
        raise DeserializationError(
            "DescribeRegistrationVersionsResult.registration_arn required"
        )
    if "RegistrationId" in data:
        out["registration_id"] = data["RegistrationId"]
    else:
        raise DeserializationError(
            "DescribeRegistrationVersionsResult.registration_id required"
        )
    if "RegistrationVersions" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information_list

        out["registration_versions"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_version_information_list.deserialize_aws_json_1_0(
                data["RegistrationVersions"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeRegistrationVersionsResult.registration_versions required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
