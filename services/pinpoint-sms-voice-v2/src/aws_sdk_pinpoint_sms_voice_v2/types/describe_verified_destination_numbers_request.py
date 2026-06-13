"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeVerifiedDestinationNumbersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.destination_phone_number_list
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list
    import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_list


class DescribeVerifiedDestinationNumbersRequest(TypedDict):
    verified_destination_number_ids: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_list.VerifiedDestinationNumberIdList"
    ]
    """<p>An array of VerifiedDestinationNumberid to retrieve.</p>"""
    destination_phone_numbers: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.destination_phone_number_list.DestinationPhoneNumberList"
    ]
    """<p>An array of verified destination phone number, in E.164 format.</p>"""
    filters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list.VerifiedDestinationNumberFilterList"
    ]
    """<p>An array of VerifiedDestinationNumberFilter objects to filter the results.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeVerifiedDestinationNumbersRequest) -> dict:
    out: dict = {}
    if "verified_destination_number_ids" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_list

        out["VerifiedDestinationNumberIds"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_list.serialize_aws_json_1_0(
                value["verified_destination_number_ids"]
            )
        )
    if "destination_phone_numbers" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.destination_phone_number_list

        out["DestinationPhoneNumbers"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.destination_phone_number_list.serialize_aws_json_1_0(
                value["destination_phone_numbers"]
            )
        )
    if "filters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list

        out["Filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeVerifiedDestinationNumbersRequest:
    out: DescribeVerifiedDestinationNumbersRequest = {}  # type: ignore[typeddict-item]
    if "VerifiedDestinationNumberIds" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_list

        out["verified_destination_number_ids"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_list.deserialize_aws_json_1_0(
                data["VerifiedDestinationNumberIds"]
            )
        )
    if "DestinationPhoneNumbers" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.destination_phone_number_list

        out["destination_phone_numbers"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.destination_phone_number_list.deserialize_aws_json_1_0(
                data["DestinationPhoneNumbers"]
            )
        )
    if "Filters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list

        out["filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
