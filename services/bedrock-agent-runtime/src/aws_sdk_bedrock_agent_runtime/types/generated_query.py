"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GeneratedQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.generated_query_type


class GeneratedQuery(TypedDict):
    type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.generated_query_type.GeneratedQueryType"
    ]
    """<p>The type of transformed query.</p>"""
    sql: NotRequired["str"]
    """<p>An SQL query that corresponds to the natural language query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeneratedQuery) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_bedrock_agent_runtime.types.generated_query_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.generated_query_type.serialize_json(
                value["type"]
            )
        )
    if "sql" in value:
        out["sql"] = value["sql"]
    return out


def deserialize_json(data: dict) -> GeneratedQuery:
    out: GeneratedQuery = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.generated_query_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.generated_query_type.deserialize_json(
                data["type"]
            )
        )
    if "sql" in data:
        out["sql"] = data["sql"]
    return out
