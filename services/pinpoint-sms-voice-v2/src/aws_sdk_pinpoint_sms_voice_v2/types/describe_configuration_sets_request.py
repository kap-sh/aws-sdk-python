"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeConfigurationSetsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter_list
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_list
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token


class DescribeConfigurationSetsRequest(TypedDict):
    configuration_set_names: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_list.ConfigurationSetNameList"
    ]
    """<p>An array of strings. Each element can be either a ConfigurationSetName or ConfigurationSetArn.</p>"""
    filters: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter_list.ConfigurationSetFilterList"
    ]
    """<p>An array of filters to apply to the results that are returned.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeConfigurationSetsRequest) -> dict:
    out: dict = {}
    if "configuration_set_names" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_list

        out["ConfigurationSetNames"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_list.serialize_aws_json_1_0(
                value["configuration_set_names"]
            )
        )
    if "filters" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter_list

        out["Filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter_list.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeConfigurationSetsRequest:
    out: DescribeConfigurationSetsRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetNames" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_list

        out["configuration_set_names"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_name_list.deserialize_aws_json_1_0(
                data["ConfigurationSetNames"]
            )
        )
    if "Filters" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter_list

        out["filters"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_filter_list.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
