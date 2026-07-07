"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_information_list


class DescribeRegistrationsResult(TypedDict, closed=True):
    registrations: "aws_sdk_pinpoint_sms_voice_v2.types.registration_information_list.RegistrationInformationList"
    """<p>An array of RegistrationInformation objects.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationsResult) -> dict:
    out: dict = {}
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_information_list

    out["Registrations"] = (
        aws_sdk_pinpoint_sms_voice_v2.types.registration_information_list.serialize_aws_json_1_0(
            value["registrations"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationsResult:
    out: DescribeRegistrationsResult = {}  # type: ignore[typeddict-item]
    if "Registrations" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_information_list

        out["registrations"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_information_list.deserialize_aws_json_1_0(
                data["Registrations"]
            )
        )
    else:
        raise DeserializationError("DescribeRegistrationsResult.registrations required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
