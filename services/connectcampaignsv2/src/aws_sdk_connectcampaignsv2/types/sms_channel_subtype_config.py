"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SmsChannelSubtypeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.capacity
    import aws_sdk_connectcampaignsv2.types.sms_outbound_config
    import aws_sdk_connectcampaignsv2.types.sms_outbound_mode


class SmsChannelSubtypeConfig(TypedDict):
    capacity: NotRequired["aws_sdk_connectcampaignsv2.types.capacity.Capacity"]
    outbound_mode: "aws_sdk_connectcampaignsv2.types.sms_outbound_mode.SmsOutboundMode"
    default_outbound_config: (
        "aws_sdk_connectcampaignsv2.types.sms_outbound_config.SmsOutboundConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: SmsChannelSubtypeConfig) -> dict:
    out: dict = {}
    if "capacity" in value:
        out["capacity"] = value["capacity"]
    import aws_sdk_connectcampaignsv2.types.sms_outbound_mode

    out["outboundMode"] = (
        aws_sdk_connectcampaignsv2.types.sms_outbound_mode.serialize_json(
            value["outbound_mode"]
        )
    )
    import aws_sdk_connectcampaignsv2.types.sms_outbound_config

    out["defaultOutboundConfig"] = (
        aws_sdk_connectcampaignsv2.types.sms_outbound_config.serialize_json(
            value["default_outbound_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> SmsChannelSubtypeConfig:
    out: SmsChannelSubtypeConfig = {}  # type: ignore[typeddict-item]
    if "capacity" in data:
        out["capacity"] = data["capacity"]
    if "outboundMode" in data:
        import aws_sdk_connectcampaignsv2.types.sms_outbound_mode

        out["outbound_mode"] = (
            aws_sdk_connectcampaignsv2.types.sms_outbound_mode.deserialize_json(
                data["outboundMode"]
            )
        )
    else:
        raise DeserializationError("SmsChannelSubtypeConfig.outbound_mode required")
    if "defaultOutboundConfig" in data:
        import aws_sdk_connectcampaignsv2.types.sms_outbound_config

        out["default_outbound_config"] = (
            aws_sdk_connectcampaignsv2.types.sms_outbound_config.deserialize_json(
                data["defaultOutboundConfig"]
            )
        )
    else:
        raise DeserializationError(
            "SmsChannelSubtypeConfig.default_outbound_config required"
        )
    return out
