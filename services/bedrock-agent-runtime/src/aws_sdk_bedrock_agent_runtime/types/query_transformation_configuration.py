"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#QueryTransformationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.query_transformation_type


class QueryTransformationConfiguration(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent_runtime.types.query_transformation_type.QueryTransformationType"
    """<p>The type of transformation to apply to the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryTransformationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.query_transformation_type

    out["type"] = (
        aws_sdk_bedrock_agent_runtime.types.query_transformation_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> QueryTransformationConfiguration:
    out: QueryTransformationConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.query_transformation_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.query_transformation_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("QueryTransformationConfiguration.type required")
    return out
