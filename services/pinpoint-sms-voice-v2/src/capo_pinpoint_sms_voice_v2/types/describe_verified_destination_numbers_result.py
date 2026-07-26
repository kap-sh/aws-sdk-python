"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeVerifiedDestinationNumbersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_information_list


class DescribeVerifiedDestinationNumbersResult(TypedDict, closed=True):
    verified_destination_numbers: "capo_pinpoint_sms_voice_v2.types.verified_destination_number_information_list.VerifiedDestinationNumberInformationList"
    """<p>An array of VerifiedDestinationNumberInformation objects</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeVerifiedDestinationNumbersResult) -> dict:
    out: dict = {}
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_information_list

    out["VerifiedDestinationNumbers"] = (
        capo_pinpoint_sms_voice_v2.types.verified_destination_number_information_list.serialize_aws_json_1_0(
            value["verified_destination_numbers"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeVerifiedDestinationNumbersResult:
    out: DescribeVerifiedDestinationNumbersResult = {}  # type: ignore[typeddict-item]
    if "VerifiedDestinationNumbers" in data:
        import capo_pinpoint_sms_voice_v2.types.verified_destination_number_information_list

        out["verified_destination_numbers"] = (
            capo_pinpoint_sms_voice_v2.types.verified_destination_number_information_list.deserialize_aws_json_1_0(
                data["VerifiedDestinationNumbers"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeVerifiedDestinationNumbersResult.verified_destination_numbers required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
