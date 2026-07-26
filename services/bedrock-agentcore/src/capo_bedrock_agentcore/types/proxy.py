"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Proxy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.external_proxy


class _Proxy_externalProxy(TypedDict, closed=True):
    externalProxy: "capo_bedrock_agentcore.types.external_proxy.ExternalProxy"


Proxy: TypeAlias = _Proxy_externalProxy


# --- restJson1 ser/de ---
def serialize_json(value: Proxy) -> dict:
    if "externalProxy" in value:
        import capo_bedrock_agentcore.types.external_proxy

        return {
            "externalProxy": capo_bedrock_agentcore.types.external_proxy.serialize_json(
                value["externalProxy"]
            )
        }
    else:
        raise SerializationError("Proxy: no variant present")


def deserialize_json(data: dict) -> Proxy:
    if "externalProxy" in data:
        import capo_bedrock_agentcore.types.external_proxy

        return {
            "externalProxy": capo_bedrock_agentcore.types.external_proxy.deserialize_json(
                data["externalProxy"]
            )
        }
    else:
        raise DeserializationError("Proxy: no recognized variant key")
