"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#QueryGenerationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.input_query_type


class QueryGenerationInput(TypedDict):
    type: "aws_sdk_bedrock_agent_runtime.types.input_query_type.InputQueryType"
    """<p>The type of the query.</p>"""
    text: "str"
    """<p>The text of the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationInput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.input_query_type

    out["type"] = aws_sdk_bedrock_agent_runtime.types.input_query_type.serialize_json(
        value["type"]
    )
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> QueryGenerationInput:
    out: QueryGenerationInput = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.input_query_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.input_query_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("QueryGenerationInput.type required")
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("QueryGenerationInput.text required")
    return out
