"""Generated from Smithy shape ``com.amazonaws.ivs#ListChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.channel_ad_configuration_arn
    import aws_sdk_ivs.types.channel_name
    import aws_sdk_ivs.types.channel_playback_restriction_policy_arn
    import aws_sdk_ivs.types.channel_recording_configuration_arn
    import aws_sdk_ivs.types.max_channel_results
    import aws_sdk_ivs.types.pagination_token


class ListChannelsRequest(TypedDict, closed=True):
    filter_by_name: NotRequired["aws_sdk_ivs.types.channel_name.ChannelName"]
    """<p>Filters the channel list to match the specified name.</p>"""
    filter_by_recording_configuration_arn: NotRequired[
        "aws_sdk_ivs.types.channel_recording_configuration_arn.ChannelRecordingConfigurationArn"
    ]
    """<p>Filters the channel list to match the specified recording-configuration ARN.</p>"""
    filter_by_playback_restriction_policy_arn: NotRequired[
        "aws_sdk_ivs.types.channel_playback_restriction_policy_arn.ChannelPlaybackRestrictionPolicyArn"
    ]
    """<p>Filters the channel list to match the specified policy.</p>"""
    filter_by_ad_configuration_arn: NotRequired[
        "aws_sdk_ivs.types.channel_ad_configuration_arn.ChannelAdConfigurationArn"
    ]
    """<p>Filters the channel list to match the specified ad configuration ARN.</p>"""
    next_token: NotRequired["aws_sdk_ivs.types.pagination_token.PaginationToken"]
    """<p>The first channel to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired["aws_sdk_ivs.types.max_channel_results.MaxChannelResults"]
    """<p>Maximum number of channels to return. Default: 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsRequest) -> dict:
    out: dict = {}
    if "filter_by_name" in value:
        out["filterByName"] = value["filter_by_name"]
    if "filter_by_recording_configuration_arn" in value:
        out["filterByRecordingConfigurationArn"] = value[
            "filter_by_recording_configuration_arn"
        ]
    if "filter_by_playback_restriction_policy_arn" in value:
        out["filterByPlaybackRestrictionPolicyArn"] = value[
            "filter_by_playback_restriction_policy_arn"
        ]
    if "filter_by_ad_configuration_arn" in value:
        out["filterByAdConfigurationArn"] = value["filter_by_ad_configuration_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListChannelsRequest:
    out: ListChannelsRequest = {}  # type: ignore[typeddict-item]
    if "filterByName" in data:
        out["filter_by_name"] = data["filterByName"]
    if "filterByRecordingConfigurationArn" in data:
        out["filter_by_recording_configuration_arn"] = data[
            "filterByRecordingConfigurationArn"
        ]
    if "filterByPlaybackRestrictionPolicyArn" in data:
        out["filter_by_playback_restriction_policy_arn"] = data[
            "filterByPlaybackRestrictionPolicyArn"
        ]
    if "filterByAdConfigurationArn" in data:
        out["filter_by_ad_configuration_arn"] = data["filterByAdConfigurationArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
