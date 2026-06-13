"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TransformationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.query_transformation_mode
    import aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration


class TransformationConfiguration(TypedDict):
    mode: "aws_sdk_bedrock_agent_runtime.types.query_transformation_mode.QueryTransformationMode"
    """<p>The mode of the transformation.</p>"""
    text_to_sql_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration.TextToSqlConfiguration"
    ]
    """<p>Specifies configurations for transforming text to SQL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransformationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.query_transformation_mode

    out["mode"] = (
        aws_sdk_bedrock_agent_runtime.types.query_transformation_mode.serialize_json(
            value["mode"]
        )
    )
    if "text_to_sql_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration

        out["textToSqlConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration.serialize_json(
                value["text_to_sql_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransformationConfiguration:
    out: TransformationConfiguration = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_bedrock_agent_runtime.types.query_transformation_mode

        out["mode"] = (
            aws_sdk_bedrock_agent_runtime.types.query_transformation_mode.deserialize_json(
                data["mode"]
            )
        )
    else:
        raise DeserializationError("TransformationConfiguration.mode required")
    if "textToSqlConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration

        out["text_to_sql_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.text_to_sql_configuration.deserialize_json(
                data["textToSqlConfiguration"]
            )
        )
    return out
