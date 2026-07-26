"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SmsOutboundMode``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.agentless_config


class _SmsOutboundMode_agentless(TypedDict, closed=True):
    agentless: "capo_connectcampaignsv2.types.agentless_config.AgentlessConfig"


SmsOutboundMode: TypeAlias = _SmsOutboundMode_agentless


# --- restJson1 ser/de ---
def serialize_json(value: SmsOutboundMode) -> dict:
    if "agentless" in value:
        import capo_connectcampaignsv2.types.agentless_config

        return {
            "agentless": capo_connectcampaignsv2.types.agentless_config.serialize_json(
                value["agentless"]
            )
        }
    else:
        raise SerializationError("SmsOutboundMode: no variant present")


def deserialize_json(data: dict) -> SmsOutboundMode:
    if "agentless" in data:
        import capo_connectcampaignsv2.types.agentless_config

        return {
            "agentless": capo_connectcampaignsv2.types.agentless_config.deserialize_json(
                data["agentless"]
            )
        }
    else:
        raise DeserializationError("SmsOutboundMode: no recognized variant key")
