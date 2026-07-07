"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VectorSearchBedrockRerankingModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.additional_model_request_fields
    import aws_sdk_bedrock_agent.types.bedrock_reranking_model_arn


class VectorSearchBedrockRerankingModelConfiguration(TypedDict, closed=True):
    model_arn: "aws_sdk_bedrock_agent.types.bedrock_reranking_model_arn.BedrockRerankingModelArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Bedrock reranker model.</p>"""
    additional_model_request_fields: NotRequired[
        "aws_sdk_bedrock_agent.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p>Specifies additional model-specific request parameters as key-value pairs that are included in the request to the Amazon Bedrock reranker model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorSearchBedrockRerankingModelConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "additional_model_request_fields" in value:
        import aws_sdk_bedrock_agent.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            aws_sdk_bedrock_agent.types.additional_model_request_fields.serialize_json(
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
        import aws_sdk_bedrock_agent.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            aws_sdk_bedrock_agent.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    return out
