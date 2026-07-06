"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockRerankingModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields
    import aws_sdk_bedrock_agent_runtime.types.bedrock_model_arn


class BedrockRerankingModelConfiguration(TypedDict, closed=True):
    model_arn: "aws_sdk_bedrock_agent_runtime.types.bedrock_model_arn.BedrockModelArn"
    """<p>The ARN of the reranker model.</p>"""
    additional_model_request_fields: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields.AdditionalModelRequestFields"
    ]
    """<p>A JSON object whose keys are request fields for the model and whose values are values for those fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockRerankingModelConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "additional_model_request_fields" in value:
        import aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields

        out["additionalModelRequestFields"] = (
            aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields.serialize_json(
                value["additional_model_request_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> BedrockRerankingModelConfiguration:
    out: BedrockRerankingModelConfiguration = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "BedrockRerankingModelConfiguration.model_arn required"
        )
    if "additionalModelRequestFields" in data:
        import aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields

        out["additional_model_request_fields"] = (
            aws_sdk_bedrock_agent_runtime.types.additional_model_request_fields.deserialize_json(
                data["additionalModelRequestFields"]
            )
        )
    return out
