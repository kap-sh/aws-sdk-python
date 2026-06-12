"""Generated from Smithy shape ``com.amazonaws.bedrock#ImplicitFilterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.bedrock_model_arn
    import aws_sdk_bedrock.types.metadata_attribute_schema_list


class ImplicitFilterConfiguration(TypedDict):
    metadata_attributes: "aws_sdk_bedrock.types.metadata_attribute_schema_list.MetadataAttributeSchemaList"
    """<p>A list of metadata attribute schemas that define the structure and properties of metadata fields used for implicit filtering. Each attribute defines a key, type, and optional description.</p>"""
    model_arn: "aws_sdk_bedrock.types.bedrock_model_arn.BedrockModelArn"
    """<p>The Amazon Resource Name (ARN) of the foundation model used for implicit filtering. This model processes the query to extract relevant filtering criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImplicitFilterConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.metadata_attribute_schema_list

    out["metadataAttributes"] = (
        aws_sdk_bedrock.types.metadata_attribute_schema_list.serialize_json(
            value["metadata_attributes"]
        )
    )
    out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(data: dict) -> ImplicitFilterConfiguration:
    out: ImplicitFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "metadataAttributes" in data:
        import aws_sdk_bedrock.types.metadata_attribute_schema_list

        out["metadata_attributes"] = (
            aws_sdk_bedrock.types.metadata_attribute_schema_list.deserialize_json(
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
