"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BedrockModelSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bedrock_guardrail_configuration
    import aws_sdk_lex_models_v2.types.bedrock_model_arn
    import aws_sdk_lex_models_v2.types.bedrock_model_custom_prompt
    import aws_sdk_lex_models_v2.types.bedrock_trace_status


class BedrockModelSpecification(TypedDict):
    model_arn: "aws_sdk_lex_models_v2.types.bedrock_model_arn.BedrockModelArn"
    """<p>The ARN of the foundation model used in descriptive bot building.</p>"""
    guardrail: NotRequired[
        "aws_sdk_lex_models_v2.types.bedrock_guardrail_configuration.BedrockGuardrailConfiguration"
    ]
    """<p>The guardrail configuration in the Bedrock model specification details.</p>"""
    trace_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bedrock_trace_status.BedrockTraceStatus"
    ]
    """<p>The Bedrock trace status in the Bedrock model specification details.</p>"""
    custom_prompt: NotRequired[
        "aws_sdk_lex_models_v2.types.bedrock_model_custom_prompt.BedrockModelCustomPrompt"
    ]
    """<p>The custom prompt used in the Bedrock model specification details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockModelSpecification) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "guardrail" in value:
        import aws_sdk_lex_models_v2.types.bedrock_guardrail_configuration

        out["guardrail"] = (
            aws_sdk_lex_models_v2.types.bedrock_guardrail_configuration.serialize_json(
                value["guardrail"]
            )
        )
    if "trace_status" in value:
        import aws_sdk_lex_models_v2.types.bedrock_trace_status

        out["traceStatus"] = (
            aws_sdk_lex_models_v2.types.bedrock_trace_status.serialize_json(
                value["trace_status"]
            )
        )
    if "custom_prompt" in value:
        out["customPrompt"] = value["custom_prompt"]
    return out


def deserialize_json(data: dict) -> BedrockModelSpecification:
    out: BedrockModelSpecification = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError("BedrockModelSpecification.model_arn required")
    if "guardrail" in data:
        import aws_sdk_lex_models_v2.types.bedrock_guardrail_configuration

        out["guardrail"] = (
            aws_sdk_lex_models_v2.types.bedrock_guardrail_configuration.deserialize_json(
                data["guardrail"]
            )
        )
    if "traceStatus" in data:
        import aws_sdk_lex_models_v2.types.bedrock_trace_status

        out["trace_status"] = (
            aws_sdk_lex_models_v2.types.bedrock_trace_status.deserialize_json(
                data["traceStatus"]
            )
        )
    if "customPrompt" in data:
        out["custom_prompt"] = data["customPrompt"]
    return out
