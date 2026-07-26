"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#CreateCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_name
    import capo_connectcampaigns.types.dialer_config
    import capo_connectcampaigns.types.instance_id
    import capo_connectcampaigns.types.outbound_call_config
    import capo_connectcampaigns.types.tag_map


class CreateCampaignRequest(TypedDict, closed=True):
    name: "capo_connectcampaigns.types.campaign_name.CampaignName"
    connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId"
    dialer_config: "capo_connectcampaigns.types.dialer_config.DialerConfig"
    outbound_call_config: (
        "capo_connectcampaigns.types.outbound_call_config.OutboundCallConfig"
    )
    tags: NotRequired["capo_connectcampaigns.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateCampaignRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["connectInstanceId"] = value["connect_instance_id"]
    import capo_connectcampaigns.types.dialer_config

    out["dialerConfig"] = capo_connectcampaigns.types.dialer_config.serialize_json(
        value["dialer_config"]
    )
    import capo_connectcampaigns.types.outbound_call_config

    out["outboundCallConfig"] = (
        capo_connectcampaigns.types.outbound_call_config.serialize_json(
            value["outbound_call_config"]
        )
    )
    if "tags" in value:
        import capo_connectcampaigns.types.tag_map

        out["tags"] = capo_connectcampaigns.types.tag_map.serialize_json(value["tags"])
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
    if "dialerConfig" in data:
        import capo_connectcampaigns.types.dialer_config

        out["dialer_config"] = (
            capo_connectcampaigns.types.dialer_config.deserialize_json(
                data["dialerConfig"]
            )
        )
    else:
        raise DeserializationError("CreateCampaignRequest.dialer_config required")
    if "outboundCallConfig" in data:
        import capo_connectcampaigns.types.outbound_call_config

        out["outbound_call_config"] = (
            capo_connectcampaigns.types.outbound_call_config.deserialize_json(
                data["outboundCallConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCampaignRequest.outbound_call_config required"
        )
    if "tags" in data:
        import capo_connectcampaigns.types.tag_map

        out["tags"] = capo_connectcampaigns.types.tag_map.deserialize_json(data["tags"])
    return out
