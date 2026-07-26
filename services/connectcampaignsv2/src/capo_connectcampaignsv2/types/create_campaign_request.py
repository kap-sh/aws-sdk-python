"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CreateCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.campaign_name
    import capo_connectcampaignsv2.types.channel_subtype_config
    import capo_connectcampaignsv2.types.communication_limits_config
    import capo_connectcampaignsv2.types.communication_time_config
    import capo_connectcampaignsv2.types.entry_limits_config
    import capo_connectcampaignsv2.types.external_campaign_type
    import capo_connectcampaignsv2.types.instance_id
    import capo_connectcampaignsv2.types.schedule
    import capo_connectcampaignsv2.types.source
    import capo_connectcampaignsv2.types.tag_map


class CreateCampaignRequest(TypedDict, closed=True):
    name: "capo_connectcampaignsv2.types.campaign_name.CampaignName"
    connect_instance_id: "capo_connectcampaignsv2.types.instance_id.InstanceId"
    channel_subtype_config: NotRequired[
        "capo_connectcampaignsv2.types.channel_subtype_config.ChannelSubtypeConfig"
    ]
    type: NotRequired[
        "capo_connectcampaignsv2.types.external_campaign_type.ExternalCampaignType"
    ]
    source: NotRequired["capo_connectcampaignsv2.types.source.Source"]
    connect_campaign_flow_arn: NotRequired["capo_connectcampaignsv2.types.arn.Arn"]
    schedule: NotRequired["capo_connectcampaignsv2.types.schedule.Schedule"]
    entry_limits_config: NotRequired[
        "capo_connectcampaignsv2.types.entry_limits_config.EntryLimitsConfig"
    ]
    communication_time_config: NotRequired[
        "capo_connectcampaignsv2.types.communication_time_config.CommunicationTimeConfig"
    ]
    communication_limits_override: NotRequired[
        "capo_connectcampaignsv2.types.communication_limits_config.CommunicationLimitsConfig"
    ]
    tags: NotRequired["capo_connectcampaignsv2.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateCampaignRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["connectInstanceId"] = value["connect_instance_id"]
    if "channel_subtype_config" in value:
        import capo_connectcampaignsv2.types.channel_subtype_config

        out["channelSubtypeConfig"] = (
            capo_connectcampaignsv2.types.channel_subtype_config.serialize_json(
                value["channel_subtype_config"]
            )
        )
    if "type" in value:
        out["type"] = value["type"]
    if "source" in value:
        import capo_connectcampaignsv2.types.source

        out["source"] = capo_connectcampaignsv2.types.source.serialize_json(
            value["source"]
        )
    if "connect_campaign_flow_arn" in value:
        out["connectCampaignFlowArn"] = value["connect_campaign_flow_arn"]
    if "schedule" in value:
        import capo_connectcampaignsv2.types.schedule

        out["schedule"] = capo_connectcampaignsv2.types.schedule.serialize_json(
            value["schedule"]
        )
    if "entry_limits_config" in value:
        import capo_connectcampaignsv2.types.entry_limits_config

        out["entryLimitsConfig"] = (
            capo_connectcampaignsv2.types.entry_limits_config.serialize_json(
                value["entry_limits_config"]
            )
        )
    if "communication_time_config" in value:
        import capo_connectcampaignsv2.types.communication_time_config

        out["communicationTimeConfig"] = (
            capo_connectcampaignsv2.types.communication_time_config.serialize_json(
                value["communication_time_config"]
            )
        )
    if "communication_limits_override" in value:
        import capo_connectcampaignsv2.types.communication_limits_config

        out["communicationLimitsOverride"] = (
            capo_connectcampaignsv2.types.communication_limits_config.serialize_json(
                value["communication_limits_override"]
            )
        )
    if "tags" in value:
        import capo_connectcampaignsv2.types.tag_map

        out["tags"] = capo_connectcampaignsv2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCampaignRequest:
    out: CreateCampaignRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCampaignRequest.name required")
    if "connectInstanceId" in data:
        out["connect_instance_id"] = data["connectInstanceId"]
    else:
        raise DeserializationError("CreateCampaignRequest.connect_instance_id required")
    if "channelSubtypeConfig" in data:
        import capo_connectcampaignsv2.types.channel_subtype_config

        out["channel_subtype_config"] = (
            capo_connectcampaignsv2.types.channel_subtype_config.deserialize_json(
                data["channelSubtypeConfig"]
            )
        )
    if "type" in data:
        out["type"] = data["type"]
    if "source" in data:
        import capo_connectcampaignsv2.types.source

        out["source"] = capo_connectcampaignsv2.types.source.deserialize_json(
            data["source"]
        )
    if "connectCampaignFlowArn" in data:
        out["connect_campaign_flow_arn"] = data["connectCampaignFlowArn"]
    if "schedule" in data:
        import capo_connectcampaignsv2.types.schedule

        out["schedule"] = capo_connectcampaignsv2.types.schedule.deserialize_json(
            data["schedule"]
        )
    if "entryLimitsConfig" in data:
        import capo_connectcampaignsv2.types.entry_limits_config

        out["entry_limits_config"] = (
            capo_connectcampaignsv2.types.entry_limits_config.deserialize_json(
                data["entryLimitsConfig"]
            )
        )
    if "communicationTimeConfig" in data:
        import capo_connectcampaignsv2.types.communication_time_config

        out["communication_time_config"] = (
            capo_connectcampaignsv2.types.communication_time_config.deserialize_json(
                data["communicationTimeConfig"]
            )
        )
    if "communicationLimitsOverride" in data:
        import capo_connectcampaignsv2.types.communication_limits_config

        out["communication_limits_override"] = (
            capo_connectcampaignsv2.types.communication_limits_config.deserialize_json(
                data["communicationLimitsOverride"]
            )
        )
    if "tags" in data:
        import capo_connectcampaignsv2.types.tag_map

        out["tags"] = capo_connectcampaignsv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
