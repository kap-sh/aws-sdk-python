"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SmsChannelSubtypeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.capacity
    import capo_connectcampaignsv2.types.sms_outbound_config
    import capo_connectcampaignsv2.types.sms_outbound_mode


class SmsChannelSubtypeConfig(TypedDict, closed=True):
    capacity: NotRequired["capo_connectcampaignsv2.types.capacity.Capacity"]
    outbound_mode: "capo_connectcampaignsv2.types.sms_outbound_mode.SmsOutboundMode"
    default_outbound_config: (
        "capo_connectcampaignsv2.types.sms_outbound_config.SmsOutboundConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: SmsChannelSubtypeConfig) -> dict:
    out: dict = {}
    if "capacity" in value:
        out["capacity"] = value["capacity"]
    import capo_connectcampaignsv2.types.sms_outbound_mode

    out["outboundMode"] = (
        capo_connectcampaignsv2.types.sms_outbound_mode.serialize_json(
            value["outbound_mode"]
        )
    )
    import capo_connectcampaignsv2.types.sms_outbound_config

    out["defaultOutboundConfig"] = (
        capo_connectcampaignsv2.types.sms_outbound_config.serialize_json(
            value["default_outbound_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> SmsChannelSubtypeConfig:
    out: SmsChannelSubtypeConfig = {}  # type: ignore[typeddict-item]
    if "capacity" in data:
        out["capacity"] = data["capacity"]
    if "outboundMode" in data:
        import capo_connectcampaignsv2.types.sms_outbound_mode

        out["outbound_mode"] = (
            capo_connectcampaignsv2.types.sms_outbound_mode.deserialize_json(
                data["outboundMode"]
            )
        )
    else:
        raise DeserializationError("SmsChannelSubtypeConfig.outbound_mode required")
    if "defaultOutboundConfig" in data:
        import capo_connectcampaignsv2.types.sms_outbound_config

        out["default_outbound_config"] = (
            capo_connectcampaignsv2.types.sms_outbound_config.deserialize_json(
                data["defaultOutboundConfig"]
            )
        )
    else:
        raise DeserializationError(
            "SmsChannelSubtypeConfig.default_outbound_config required"
        )
    return out
