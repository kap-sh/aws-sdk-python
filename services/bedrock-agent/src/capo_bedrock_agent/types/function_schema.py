"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FunctionSchema``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.functions


class _FunctionSchema_functions(TypedDict, closed=True):
    functions: "capo_bedrock_agent.types.functions.Functions"


FunctionSchema: TypeAlias = _FunctionSchema_functions


# --- restJson1 ser/de ---
def serialize_json(value: FunctionSchema) -> dict:
    if "functions" in value:
        import capo_bedrock_agent.types.functions

        return {
            "functions": capo_bedrock_agent.types.functions.serialize_json(
                value["functions"]
            )
        }
    else:
        raise SerializationError("FunctionSchema: no variant present")


def deserialize_json(data: dict) -> FunctionSchema:
    if data.get("functions") is not None:
        import capo_bedrock_agent.types.functions

        return {
            "functions": capo_bedrock_agent.types.functions.deserialize_json(
                data["functions"]
            )
        }
    else:
        raise DeserializationError("FunctionSchema: no recognized variant key")
