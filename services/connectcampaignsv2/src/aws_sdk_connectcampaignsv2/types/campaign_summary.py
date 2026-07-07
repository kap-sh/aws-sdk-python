"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CampaignSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn
    import aws_sdk_connectcampaignsv2.types.campaign_arn
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.campaign_name
    import aws_sdk_connectcampaignsv2.types.channel_subtype_list
    import aws_sdk_connectcampaignsv2.types.entry_limits_config
    import aws_sdk_connectcampaignsv2.types.external_campaign_type
    import aws_sdk_connectcampaignsv2.types.instance_id
    import aws_sdk_connectcampaignsv2.types.schedule


class CampaignSummary(TypedDict, closed=True):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    arn: "aws_sdk_connectcampaignsv2.types.campaign_arn.CampaignArn"
    name: "aws_sdk_connectcampaignsv2.types.campaign_name.CampaignName"
    connect_instance_id: "aws_sdk_connectcampaignsv2.types.instance_id.InstanceId"
    channel_subtypes: (
        "aws_sdk_connectcampaignsv2.types.channel_subtype_list.ChannelSubtypeList"
    )
    type: NotRequired[
        "aws_sdk_connectcampaignsv2.types.external_campaign_type.ExternalCampaignType"
    ]
    schedule: NotRequired["aws_sdk_connectcampaignsv2.types.schedule.Schedule"]
    entry_limits_config: NotRequired[
        "aws_sdk_connectcampaignsv2.types.entry_limits_config.EntryLimitsConfig"
    ]
    connect_campaign_flow_arn: NotRequired["aws_sdk_connectcampaignsv2.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: CampaignSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["connectInstanceId"] = value["connect_instance_id"]
    import aws_sdk_connectcampaignsv2.types.channel_subtype_list

    out["channelSubtypes"] = (
        aws_sdk_connectcampaignsv2.types.channel_subtype_list.serialize_json(
            value["channel_subtypes"]
        )
    )
    if "type" in value:
        out["type"] = value["type"]
    if "schedule" in value:
        import aws_sdk_connectcampaignsv2.types.schedule

        out["schedule"] = aws_sdk_connectcampaignsv2.types.schedule.serialize_json(
            value["schedule"]
        )
    if "entry_limits_config" in value:
        import aws_sdk_connectcampaignsv2.types.entry_limits_config

        out["entryLimitsConfig"] = (
            aws_sdk_connectcampaignsv2.types.entry_limits_config.serialize_json(
                value["entry_limits_config"]
            )
        )
    if "connect_campaign_flow_arn" in value:
        out["connectCampaignFlowArn"] = value["connect_campaign_flow_arn"]
    return out


def deserialize_json(data: dict) -> CampaignSummary:
    out: CampaignSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CampaignSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CampaignSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CampaignSummary.name required")
    if "connectInstanceId" in data:
        out["connect_instance_id"] = data["connectInstanceId"]
    else:
        raise DeserializationError("CampaignSummary.connect_instance_id required")
    if "channelSubtypes" in data:
        import aws_sdk_connectcampaignsv2.types.channel_subtype_list

        out["channel_subtypes"] = (
            aws_sdk_connectcampaignsv2.types.channel_subtype_list.deserialize_json(
                data["channelSubtypes"]
            )
        )
    else:
        raise DeserializationError("CampaignSummary.channel_subtypes required")
    if "type" in data:
        out["type"] = data["type"]
    if "schedule" in data:
        import aws_sdk_connectcampaignsv2.types.schedule

        out["schedule"] = aws_sdk_connectcampaignsv2.types.schedule.deserialize_json(
            data["schedule"]
        )
    if "entryLimitsConfig" in data:
        import aws_sdk_connectcampaignsv2.types.entry_limits_config

        out["entry_limits_config"] = (
            aws_sdk_connectcampaignsv2.types.entry_limits_config.deserialize_json(
                data["entryLimitsConfig"]
            )
        )
    if "connectCampaignFlowArn" in data:
        out["connect_campaign_flow_arn"] = data["connectCampaignFlowArn"]
    return out
