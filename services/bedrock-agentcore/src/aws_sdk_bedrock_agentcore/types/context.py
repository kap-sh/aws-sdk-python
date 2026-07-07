"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Context``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.span_context


class _Context_spanContext(TypedDict, closed=True):
    spanContext: "aws_sdk_bedrock_agentcore.types.span_context.SpanContext"


Context: TypeAlias = _Context_spanContext


# --- restJson1 ser/de ---
def serialize_json(value: Context) -> dict:
    if "spanContext" in value:
        import aws_sdk_bedrock_agentcore.types.span_context

        return {
            "spanContext": aws_sdk_bedrock_agentcore.types.span_context.serialize_json(
                value["spanContext"]
            )
        }
    else:
        raise SerializationError("Context: no variant present")


def deserialize_json(data: dict) -> Context:
    if "spanContext" in data:
        import aws_sdk_bedrock_agentcore.types.span_context

        return {
            "spanContext": aws_sdk_bedrock_agentcore.types.span_context.deserialize_json(
                data["spanContext"]
            )
        }
    else:
        raise DeserializationError("Context: no recognized variant key")
