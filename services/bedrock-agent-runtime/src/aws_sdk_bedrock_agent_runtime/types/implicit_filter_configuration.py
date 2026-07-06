"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImplicitFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.bedrock_model_arn
    import aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema_list


class ImplicitFilterConfiguration(TypedDict, closed=True):
    metadata_attributes: "aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema_list.MetadataAttributeSchemaList"
    """<p>Metadata that can be used in a filter.</p>"""
    model_arn: "aws_sdk_bedrock_agent_runtime.types.bedrock_model_arn.BedrockModelArn"
    """<p>The model that generates the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImplicitFilterConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema_list

    out["metadataAttributes"] = (
        aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema_list.serialize_json(
            value["metadata_attributes"]
        )
    )
    out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(data: dict) -> ImplicitFilterConfiguration:
    out: ImplicitFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "metadataAttributes" in data:
        import aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema_list

        out["metadata_attributes"] = (
            aws_sdk_bedrock_agent_runtime.types.metadata_attribute_schema_list.deserialize_json(
                data["metadataAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "ImplicitFilterConfiguration.metadata_attributes required"
        )
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("ImplicitFilterConfiguration.model_arn required")
    return out
