"""Generated from Smithy shape ``com.amazonaws.bedrock#VectorSearchBedrockRerankingModelConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.additional_model_request_fields
    import aws_sdk_bedrock.types.bedrock_reranking_model_arn


class VectorSearchBedrockRerankingModelConfiguration(TypedDict):
    model_arn: (
        "aws_sdk_bedrock.types.bedrock_reranking_model_arn.BedrockRerankingModelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the foundation model to use for reranking. This model processes the query and search results to determine a more relevant ordering.</p>"""
    additional_model_request_fields: NotRequired[
        "aws_sdk_bedrock.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p>A list of additional fields to include in the model request during reranking. These fields provide extra context or configuration options specific to the selected foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchBedrockRerankingModelConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "additional_model_request_fields" in value:
        import aws_sdk_bedrock.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            aws_sdk_bedrock.types.additional_model_request_fields.serialize_json(
                value["additional_model_request_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorSearchBedrockRerankingModelConfiguration:
    out: VectorSearchBedrockRerankingModelConfiguration = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "VectorSearchBedrockRerankingModelConfiguration.model_arn required"
        )
    if "additionalModelRequestFields" in data:
        import aws_sdk_bedrock.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            aws_sdk_bedrock.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    return out
