"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#WhatsAppChannelSubtypeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.capacity
    import capo_connectcampaignsv2.types.whats_app_outbound_config
    import capo_connectcampaignsv2.types.whats_app_outbound_mode


class WhatsAppChannelSubtypeConfig(TypedDict, closed=True):
    capacity: NotRequired["capo_connectcampaignsv2.types.capacity.Capacity"]
    outbound_mode: (
        "capo_connectcampaignsv2.types.whats_app_outbound_mode.WhatsAppOutboundMode"
    )
    default_outbound_config: (
        "capo_connectcampaignsv2.types.whats_app_outbound_config.WhatsAppOutboundConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppChannelSubtypeConfig) -> dict:
    out: dict = {}
    if "capacity" in value:
        out["capacity"] = value["capacity"]
    import capo_connectcampaignsv2.types.whats_app_outbound_mode

    out["outboundMode"] = (
        capo_connectcampaignsv2.types.whats_app_outbound_mode.serialize_json(
            value["outbound_mode"]
        )
    )
    import capo_connectcampaignsv2.types.whats_app_outbound_config

    out["defaultOutboundConfig"] = (
        capo_connectcampaignsv2.types.whats_app_outbound_config.serialize_json(
            value["default_outbound_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> WhatsAppChannelSubtypeConfig:
    out: WhatsAppChannelSubtypeConfig = {}  # type: ignore[typeddict-item]
    if "capacity" in data:
        out["capacity"] = data["capacity"]
    if "outboundMode" in data:
        import capo_connectcampaignsv2.types.whats_app_outbound_mode

        out["outbound_mode"] = (
            capo_connectcampaignsv2.types.whats_app_outbound_mode.deserialize_json(
                data["outboundMode"]
            )
        )
    else:
        raise DeserializationError(
            "WhatsAppChannelSubtypeConfig.outbound_mode required"
        )
    if "defaultOutboundConfig" in data:
        import capo_connectcampaignsv2.types.whats_app_outbound_config

        out["default_outbound_config"] = (
            capo_connectcampaignsv2.types.whats_app_outbound_config.deserialize_json(
                data["defaultOutboundConfig"]
            )
        )
    else:
        raise DeserializationError(
            "WhatsAppChannelSubtypeConfig.default_outbound_config required"
        )
    return out
