"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TelephonyChannelSubtypeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.capacity
    import aws_sdk_connectcampaignsv2.types.queue_id
    import aws_sdk_connectcampaignsv2.types.telephony_outbound_config
    import aws_sdk_connectcampaignsv2.types.telephony_outbound_mode


class TelephonyChannelSubtypeConfig(TypedDict, closed=True):
    capacity: NotRequired["aws_sdk_connectcampaignsv2.types.capacity.Capacity"]
    connect_queue_id: NotRequired["aws_sdk_connectcampaignsv2.types.queue_id.QueueId"]
    outbound_mode: (
        "aws_sdk_connectcampaignsv2.types.telephony_outbound_mode.TelephonyOutboundMode"
    )
    default_outbound_config: "aws_sdk_connectcampaignsv2.types.telephony_outbound_config.TelephonyOutboundConfig"


# --- restJson1 ser/de ---
def serialize_json(value: TelephonyChannelSubtypeConfig) -> dict:
    out: dict = {}
    if "capacity" in value:
        out["capacity"] = value["capacity"]
    if "connect_queue_id" in value:
        out["connectQueueId"] = value["connect_queue_id"]
    import aws_sdk_connectcampaignsv2.types.telephony_outbound_mode

    out["outboundMode"] = (
        aws_sdk_connectcampaignsv2.types.telephony_outbound_mode.serialize_json(
            value["outbound_mode"]
        )
    )
    import aws_sdk_connectcampaignsv2.types.telephony_outbound_config

    out["defaultOutboundConfig"] = (
        aws_sdk_connectcampaignsv2.types.telephony_outbound_config.serialize_json(
            value["default_outbound_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> TelephonyChannelSubtypeConfig:
    out: TelephonyChannelSubtypeConfig = {}  # type: ignore[typeddict-item]
    if "capacity" in data:
        out["capacity"] = data["capacity"]
    if "connectQueueId" in data:
        out["connect_queue_id"] = data["connectQueueId"]
    if "outboundMode" in data:
        import aws_sdk_connectcampaignsv2.types.telephony_outbound_mode

        out["outbound_mode"] = (
            aws_sdk_connectcampaignsv2.types.telephony_outbound_mode.deserialize_json(
                data["outboundMode"]
            )
        )
    else:
        raise DeserializationError(
            "TelephonyChannelSubtypeConfig.outbound_mode required"
        )
    if "defaultOutboundConfig" in data:
        import aws_sdk_connectcampaignsv2.types.telephony_outbound_config

        out["default_outbound_config"] = (
            aws_sdk_connectcampaignsv2.types.telephony_outbound_config.deserialize_json(
                data["defaultOutboundConfig"]
            )
        )
    else:
        raise DeserializationError(
            "TelephonyChannelSubtypeConfig.default_outbound_config required"
        )
    return out
