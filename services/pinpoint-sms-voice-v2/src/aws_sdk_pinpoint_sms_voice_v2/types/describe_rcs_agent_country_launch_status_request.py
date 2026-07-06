"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeRcsAgentCountryLaunchStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.country_launch_status_filter_list
    import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn


class DescribeRcsAgentCountryLaunchStatusRequest(TypedDict, closed=True):
    rcs_agent_id: (
        "aws_sdk_pinpoint_sms_voice_v2.types.rcs_agent_id_or_arn.RcsAgentIdOrArn"
    )
    """<p>The unique identifier of the RCS agent. You can use either the RcsAgentId or RcsAgentArn.</p>"""
    iso_country_codes: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.IsoCountryCodeList"
    ]
    """<p>An array of two-character ISO country codes, in ISO 3166-1 alpha-2 format, to filter the results.</p>"""
    filters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.country_launch_status_filter_list.CountryLaunchStatusFilterList"
    ]
    """<p>An array of CountryLaunchStatusFilter objects to filter the results.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRcsAgentCountryLaunchStatusRequest) -> dict:
    out: dict = {}
    out["RcsAgentId"] = value["rcs_agent_id"]
    if "iso_country_codes" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["IsoCountryCodes"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.serialize_aws_json_1_0(
                value["iso_country_codes"]
            )
        )
    if "filters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.country_launch_status_filter_list

        out["Filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.country_launch_status_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRcsAgentCountryLaunchStatusRequest:
    out: DescribeRcsAgentCountryLaunchStatusRequest = {}  # type: ignore[typeddict-item]
    if "RcsAgentId" in data:
        out["rcs_agent_id"] = data["RcsAgentId"]
    else:
        raise DeserializationError(
            "DescribeRcsAgentCountryLaunchStatusRequest.rcs_agent_id required"
        )
    if "IsoCountryCodes" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list

        out["iso_country_codes"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.iso_country_code_list.deserialize_aws_json_1_0(
                data["IsoCountryCodes"]
            )
        )
    if "Filters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.country_launch_status_filter_list

        out["filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.country_launch_status_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
