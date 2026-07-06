"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryGenerationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.query_execution_timeout_seconds
    import aws_sdk_bedrock_agent.types.query_generation_context


class QueryGenerationConfiguration(TypedDict, closed=True):
    execution_timeout_seconds: NotRequired[
        "aws_sdk_bedrock_agent.types.query_execution_timeout_seconds.QueryExecutionTimeoutSeconds"
    ]
    """<p>The time after which query generation will time out.</p>"""
    generation_context: NotRequired[
        "aws_sdk_bedrock_agent.types.query_generation_context.QueryGenerationContext"
    ]
    """<p>Specifies configurations for context to use during query generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryGenerationConfiguration) -> dict:
    out: dict = {}
    if "execution_timeout_seconds" in value:
        out["executionTimeoutSeconds"] = value["execution_timeout_seconds"]
    if "generation_context" in value:
        import aws_sdk_bedrock_agent.types.query_generation_context

        out["generationContext"] = (
            aws_sdk_bedrock_agent.types.query_generation_context.serialize_json(
                value["generation_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> QueryGenerationConfiguration:
    out: QueryGenerationConfiguration = {}  # type: ignore[typeddict-item]
    if "executionTimeoutSeconds" in data:
        out["execution_timeout_seconds"] = data["executionTimeoutSeconds"]
    if "generationContext" in data:
        import aws_sdk_bedrock_agent.types.query_generation_context

        out["generation_context"] = (
            aws_sdk_bedrock_agent.types.query_generation_context.deserialize_json(
                data["generationContext"]
            )
        )
    return out
