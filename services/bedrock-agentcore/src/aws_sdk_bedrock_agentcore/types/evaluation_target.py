"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationTarget``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.span_ids
    import aws_sdk_bedrock_agentcore.types.trace_ids


class _EvaluationTarget_spanIds(TypedDict):
    spanIds: "aws_sdk_bedrock_agentcore.types.span_ids.SpanIds"


class _EvaluationTarget_traceIds(TypedDict):
    traceIds: "aws_sdk_bedrock_agentcore.types.trace_ids.TraceIds"


EvaluationTarget: TypeAlias = _EvaluationTarget_spanIds | _EvaluationTarget_traceIds


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationTarget) -> dict:
    if "spanIds" in value:
        import aws_sdk_bedrock_agentcore.types.span_ids

        return {
            "spanIds": aws_sdk_bedrock_agentcore.types.span_ids.serialize_json(
                value["spanIds"]
            )
        }
    elif "traceIds" in value:
        import aws_sdk_bedrock_agentcore.types.trace_ids

        return {
            "traceIds": aws_sdk_bedrock_agentcore.types.trace_ids.serialize_json(
                value["traceIds"]
            )
        }
    else:
        raise SerializationError("EvaluationTarget: no variant present")


def deserialize_json(data: dict) -> EvaluationTarget:
    if "spanIds" in data:
        import aws_sdk_bedrock_agentcore.types.span_ids

        return {
            "spanIds": aws_sdk_bedrock_agentcore.types.span_ids.deserialize_json(
                data["spanIds"]
            )
        }
    elif "traceIds" in data:
        import aws_sdk_bedrock_agentcore.types.trace_ids

        return {
            "traceIds": aws_sdk_bedrock_agentcore.types.trace_ids.deserialize_json(
                data["traceIds"]
            )
        }
    else:
        raise DeserializationError("EvaluationTarget: no recognized variant key")
