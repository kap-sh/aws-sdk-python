"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#Campaign``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign_arn
    import aws_sdk_connectcampaigns.types.campaign_id
    import aws_sdk_connectcampaigns.types.campaign_name
    import aws_sdk_connectcampaigns.types.dialer_config
    import aws_sdk_connectcampaigns.types.instance_id
    import aws_sdk_connectcampaigns.types.outbound_call_config
    import aws_sdk_connectcampaigns.types.tag_map


class Campaign(TypedDict, closed=True):
    id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId"
    arn: "aws_sdk_connectcampaigns.types.campaign_arn.CampaignArn"
    name: "aws_sdk_connectcampaigns.types.campaign_name.CampaignName"
    connect_instance_id: "aws_sdk_connectcampaigns.types.instance_id.InstanceId"
    dialer_config: "aws_sdk_connectcampaigns.types.dialer_config.DialerConfig"
    outbound_call_config: (
        "aws_sdk_connectcampaigns.types.outbound_call_config.OutboundCallConfig"
    )
    tags: NotRequired["aws_sdk_connectcampaigns.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: Campaign) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["connectInstanceId"] = value["connect_instance_id"]
    import aws_sdk_connectcampaigns.types.dialer_config

    out["dialerConfig"] = aws_sdk_connectcampaigns.types.dialer_config.serialize_json(
        value["dialer_config"]
    )
    import aws_sdk_connectcampaigns.types.outbound_call_config

    out["outboundCallConfig"] = (
        aws_sdk_connectcampaigns.types.outbound_call_config.serialize_json(
            value["outbound_call_config"]
        )
    )
    if "tags" in value:
        import aws_sdk_connectcampaigns.types.tag_map

        out["tags"] = aws_sdk_connectcampaigns.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> Campaign:
    out: Campaign = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Campaign.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Campaign.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Campaign.name required")
    if "connectInstanceId" in data:
        out["connect_instance_id"] = data["connectInstanceId"]
    else:
        raise DeserializationError("Campaign.connect_instance_id required")
    if "dialerConfig" in data:
        import aws_sdk_connectcampaigns.types.dialer_config

        out["dialer_config"] = (
            aws_sdk_connectcampaigns.types.dialer_config.deserialize_json(
                data["dialerConfig"]
            )
        )
    else:
        raise DeserializationError("Campaign.dialer_config required")
    if "outboundCallConfig" in data:
        import aws_sdk_connectcampaigns.types.outbound_call_config

        out["outbound_call_config"] = (
            aws_sdk_connectcampaigns.types.outbound_call_config.deserialize_json(
                data["outboundCallConfig"]
            )
        )
    else:
        raise DeserializationError("Campaign.outbound_call_config required")
    if "tags" in data:
        import aws_sdk_connectcampaigns.types.tag_map

        out["tags"] = aws_sdk_connectcampaigns.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
