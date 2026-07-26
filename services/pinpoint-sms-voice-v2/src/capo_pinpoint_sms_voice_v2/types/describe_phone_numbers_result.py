"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribePhoneNumbersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.phone_number_information_list


class DescribePhoneNumbersResult(TypedDict, closed=True):
    phone_numbers: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.phone_number_information_list.PhoneNumberInformationList"
    ]
    """<p>An array of PhoneNumberInformation objects that contain the details for the requested phone numbers.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribePhoneNumbersResult) -> dict:
    out: dict = {}
    if "phone_numbers" in value:
        import capo_pinpoint_sms_voice_v2.types.phone_number_information_list

        out["PhoneNumbers"] = (
            capo_pinpoint_sms_voice_v2.types.phone_number_information_list.serialize_aws_json_1_0(
                value["phone_numbers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribePhoneNumbersResult:
    out: DescribePhoneNumbersResult = {}  # type: ignore[typeddict-item]
    if "PhoneNumbers" in data:
        import capo_pinpoint_sms_voice_v2.types.phone_number_information_list

        out["phone_numbers"] = (
            capo_pinpoint_sms_voice_v2.types.phone_number_information_list.deserialize_aws_json_1_0(
                data["PhoneNumbers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
