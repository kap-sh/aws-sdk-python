"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SmsOutboundMode``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.agentless_config


class _SmsOutboundMode_agentless(TypedDict):
    agentless: "aws_sdk_connectcampaignsv2.types.agentless_config.AgentlessConfig"


SmsOutboundMode: TypeAlias = _SmsOutboundMode_agentless


# --- restJson1 ser/de ---
def serialize_json(value: SmsOutboundMode) -> dict:
    if "agentless" in value:
        import aws_sdk_connectcampaignsv2.types.agentless_config

        return {
            "agentless": aws_sdk_connectcampaignsv2.types.agentless_config.serialize_json(
                value["agentless"]
            )
        }
    else:
        raise SerializationError("SmsOutboundMode: no variant present")


def deserialize_json(data: dict) -> SmsOutboundMode:
    if "agentless" in data:
        import aws_sdk_connectcampaignsv2.types.agentless_config

        return {
            "agentless": aws_sdk_connectcampaignsv2.types.agentless_config.deserialize_json(
                data["agentless"]
            )
        }
    else:
        raise DeserializationError("SmsOutboundMode: no recognized variant key")
