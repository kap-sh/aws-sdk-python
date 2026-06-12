"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ChannelHandshakePayload``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_partnercentral_channel.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.revoke_service_period_payload
    import aws_sdk_partnercentral_channel.types.start_service_period_payload


class _ChannelHandshakePayload_startServicePeriodPayload(TypedDict):
    startServicePeriodPayload: "aws_sdk_partnercentral_channel.types.start_service_period_payload.StartServicePeriodPayload"


class _ChannelHandshakePayload_revokeServicePeriodPayload(TypedDict):
    revokeServicePeriodPayload: "aws_sdk_partnercentral_channel.types.revoke_service_period_payload.RevokeServicePeriodPayload"


ChannelHandshakePayload: TypeAlias = (
    _ChannelHandshakePayload_startServicePeriodPayload
    | _ChannelHandshakePayload_revokeServicePeriodPayload
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChannelHandshakePayload) -> dict:
    if "startServicePeriodPayload" in value:
        import aws_sdk_partnercentral_channel.types.start_service_period_payload

        return {
            "startServicePeriodPayload": aws_sdk_partnercentral_channel.types.start_service_period_payload.serialize_aws_json_1_0(
                value["startServicePeriodPayload"]
            )
        }
    elif "revokeServicePeriodPayload" in value:
        import aws_sdk_partnercentral_channel.types.revoke_service_period_payload

        return {
            "revokeServicePeriodPayload": aws_sdk_partnercentral_channel.types.revoke_service_period_payload.serialize_aws_json_1_0(
                value["revokeServicePeriodPayload"]
            )
        }
    else:
        raise SerializationError("ChannelHandshakePayload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ChannelHandshakePayload:
    if "startServicePeriodPayload" in data:
        import aws_sdk_partnercentral_channel.types.start_service_period_payload

        return {
            "startServicePeriodPayload": aws_sdk_partnercentral_channel.types.start_service_period_payload.deserialize_aws_json_1_0(
                data["startServicePeriodPayload"]
            )
        }
    elif "revokeServicePeriodPayload" in data:
        import aws_sdk_partnercentral_channel.types.revoke_service_period_payload

        return {
            "revokeServicePeriodPayload": aws_sdk_partnercentral_channel.types.revoke_service_period_payload.deserialize_aws_json_1_0(
                data["revokeServicePeriodPayload"]
            )
        }
    else:
        raise DeserializationError("ChannelHandshakePayload: no recognized variant key")
