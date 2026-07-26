"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeVerifiedDestinationNumbersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.destination_phone_number_list
    import capo_pinpoint_sms_voice_v2.types.max_results
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_list


class DescribeVerifiedDestinationNumbersRequest(TypedDict, closed=True):
    verified_destination_number_ids: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_list.VerifiedDestinationNumberIdList"
    ]
    """<p>An array of VerifiedDestinationNumberid to retrieve.</p>"""
    destination_phone_numbers: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.destination_phone_number_list.DestinationPhoneNumberList"
    ]
    """<p>An array of verified destination phone number, in E.164 format.</p>"""
    filters: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list.VerifiedDestinationNumberFilterList"
    ]
    """<p>An array of VerifiedDestinationNumberFilter objects to filter the results.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired["capo_pinpoint_sms_voice_v2.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeVerifiedDestinationNumbersRequest) -> dict:
    out: dict = {}
    if "verified_destination_number_ids" in value:
        import capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_list

        out["VerifiedDestinationNumberIds"] = (
            capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_list.serialize_aws_json_1_0(
                value["verified_destination_number_ids"]
            )
        )
    if "destination_phone_numbers" in value:
        import capo_pinpoint_sms_voice_v2.types.destination_phone_number_list

        out["DestinationPhoneNumbers"] = (
            capo_pinpoint_sms_voice_v2.types.destination_phone_number_list.serialize_aws_json_1_0(
                value["destination_phone_numbers"]
            )
        )
    if "filters" in value:
        import capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list

        out["Filters"] = (
            capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list.serialize_aws_json_1_0(
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
        import capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_list

        out["verified_destination_number_ids"] = (
            capo_pinpoint_sms_voice_v2.types.verified_destination_number_id_list.deserialize_aws_json_1_0(
                data["VerifiedDestinationNumberIds"]
            )
        )
    if "DestinationPhoneNumbers" in data:
        import capo_pinpoint_sms_voice_v2.types.destination_phone_number_list

        out["destination_phone_numbers"] = (
            capo_pinpoint_sms_voice_v2.types.destination_phone_number_list.deserialize_aws_json_1_0(
                data["DestinationPhoneNumbers"]
            )
        )
    if "Filters" in data:
        import capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list

        out["filters"] = (
            capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
