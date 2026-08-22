"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Caller``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_alias_arn


class _Caller_agentAliasArn(TypedDict, closed=True):
    agentAliasArn: "capo_bedrock_agent_runtime.types.agent_alias_arn.AgentAliasArn"


Caller: TypeAlias = _Caller_agentAliasArn


# --- restJson1 ser/de ---
def serialize_json(value: Caller) -> dict:
    if "agentAliasArn" in value:
        return {"agentAliasArn": value["agentAliasArn"]}
    else:
        raise SerializationError("Caller: no variant present")


def deserialize_json(data: dict) -> Caller:
    if data.get("agentAliasArn") is not None:
        return {"agentAliasArn": data["agentAliasArn"]}
    else:
        raise DeserializationError("Caller: no recognized variant key")
