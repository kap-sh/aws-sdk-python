"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListNotifyCountriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.max_results
    import aws_sdk_pinpoint_sms_voice_v2.types.next_token
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list


class ListNotifyCountriesRequest(TypedDict, closed=True):
    channels: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.NotifyEnabledChannelsList"
    ]
    """<p>An array of channels to filter the results by.</p>"""
    use_cases: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list.NotifyUseCaseList"
    ]
    """<p>An array of use cases to filter the results by.</p>"""
    tier: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.notify_configuration_tier.NotifyConfigurationTier"
    ]
    """<p>The tier to filter the results by.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""
    max_results: NotRequired[
        "aws_sdk_pinpoint_sms_voice_v2.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return per each request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListNotifyCountriesRequest) -> dict:
    out: dict = {}
    if "channels" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

        out["Channels"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.serialize_aws_json_1_0(
                value["channels"]
            )
        )
    if "use_cases" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list

        out["UseCases"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list.serialize_aws_json_1_0(
                value["use_cases"]
            )
        )
    if "tier" in value:
        out["Tier"] = value["tier"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListNotifyCountriesRequest:
    out: ListNotifyCountriesRequest = {}  # type: ignore[typeddict-item]
    if "Channels" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list

        out["channels"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_enabled_channels_list.deserialize_aws_json_1_0(
                data["Channels"]
            )
        )
    if "UseCases" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list

        out["use_cases"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.notify_use_case_list.deserialize_aws_json_1_0(
                data["UseCases"]
            )
        )
    if "Tier" in data:
        out["tier"] = data["Tier"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
