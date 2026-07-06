"""Generated from Smithy shape ``com.amazonaws.bedrockagent#BedrockFoundationModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.bedrock_model_arn
    import aws_sdk_bedrock_agent.types.parsing_modality
    import aws_sdk_bedrock_agent.types.parsing_prompt


class BedrockFoundationModelConfiguration(TypedDict, closed=True):
    model_arn: "aws_sdk_bedrock_agent.types.bedrock_model_arn.BedrockModelArn"
    """<p>The ARN of the foundation model to use for parsing.</p>"""
    parsing_prompt: NotRequired[
        "aws_sdk_bedrock_agent.types.parsing_prompt.ParsingPrompt"
    ]
    """<p>Instructions for interpreting the contents of a document.</p>"""
    parsing_modality: NotRequired[
        "aws_sdk_bedrock_agent.types.parsing_modality.ParsingModality"
    ]
    """<p>Specifies whether to enable parsing of multimodal data, including both text and/or images.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockFoundationModelConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "parsing_prompt" in value:
        import aws_sdk_bedrock_agent.types.parsing_prompt

        out["parsingPrompt"] = (
            aws_sdk_bedrock_agent.types.parsing_prompt.serialize_json(
                value["parsing_prompt"]
            )
        )
    if "parsing_modality" in value:
        import aws_sdk_bedrock_agent.types.parsing_modality

        out["parsingModality"] = (
            aws_sdk_bedrock_agent.types.parsing_modality.serialize_json(
                value["parsing_modality"]
            )
        )
    return out


def deserialize_json(data: dict) -> BedrockFoundationModelConfiguration:
    out: BedrockFoundationModelConfiguration = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "BedrockFoundationModelConfiguration.model_arn required"
        )
    if "parsingPrompt" in data:
        import aws_sdk_bedrock_agent.types.parsing_prompt

        out["parsing_prompt"] = (
            aws_sdk_bedrock_agent.types.parsing_prompt.deserialize_json(
                data["parsingPrompt"]
            )
        )
    if "parsingModality" in data:
        import aws_sdk_bedrock_agent.types.parsing_modality

        out["parsing_modality"] = (
            aws_sdk_bedrock_agent.types.parsing_modality.deserialize_json(
                data["parsingModality"]
            )
        )
    return out
