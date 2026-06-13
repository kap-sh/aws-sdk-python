"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRegistrationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_filter_list
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_id_list


class DescribeRegistrationsRequest(TypedDict):
    registration_ids: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_id_list.RegistrationIdList"
    ]
    """<p>An array of unique identifiers for each registration.</p>"""
    filters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.registration_filter_list.RegistrationFilterList"
    ]
    """<p>An array of RegistrationFilter objects to filter the results.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRegistrationsRequest) -> dict:
    out: dict = {}
    if "registration_ids" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_id_list

        out["RegistrationIds"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_id_list.serialize_aws_json_1_0(
                value["registration_ids"]
            )
        )
    if "filters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_filter_list

        out["Filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRegistrationsRequest:
    out: DescribeRegistrationsRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationIds" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_id_list

        out["registration_ids"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_id_list.deserialize_aws_json_1_0(
                data["RegistrationIds"]
            )
        )
    if "Filters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.registration_filter_list

        out["filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.registration_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
