"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#WhatsAppOutboundMode``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.agentless_config


class _WhatsAppOutboundMode_agentless(TypedDict, closed=True):
    agentless: "capo_connectcampaignsv2.types.agentless_config.AgentlessConfig"


WhatsAppOutboundMode: TypeAlias = _WhatsAppOutboundMode_agentless


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppOutboundMode) -> dict:
    if "agentless" in value:
        import capo_connectcampaignsv2.types.agentless_config

        return {
            "agentless": capo_connectcampaignsv2.types.agentless_config.serialize_json(
                value["agentless"]
            )
        }
    else:
        raise SerializationError("WhatsAppOutboundMode: no variant present")


def deserialize_json(data: dict) -> WhatsAppOutboundMode:
    if "agentless" in data:
        import capo_connectcampaignsv2.types.agentless_config

        return {
            "agentless": capo_connectcampaignsv2.types.agentless_config.deserialize_json(
                data["agentless"]
            )
        }
    else:
        raise DeserializationError("WhatsAppOutboundMode: no recognized variant key")
