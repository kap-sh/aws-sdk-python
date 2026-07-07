"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DescribeConfigurationSetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information_list
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token


class DescribeConfigurationSetsResult(TypedDict, closed=True):
    configuration_sets: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information_list.ConfigurationSetInformationList"
    ]
    """<p>An array of ConfigurationSets objects.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. If this field is empty then there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeConfigurationSetsResult) -> dict:
    out: dict = {}
    if "configuration_sets" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information_list

        out["ConfigurationSets"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information_list.serialize_aws_json_1_0(
                value["configuration_sets"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeConfigurationSetsResult:
    out: DescribeConfigurationSetsResult = {}  # type: ignore[typeddict-item]
    if "ConfigurationSets" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information_list

        out["configuration_sets"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.configuration_set_information_list.deserialize_aws_json_1_0(
                data["ConfigurationSets"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
