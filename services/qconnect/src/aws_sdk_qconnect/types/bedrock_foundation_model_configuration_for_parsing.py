"""Generated from Smithy shape ``com.amazonaws.qconnect#BedrockFoundationModelConfigurationForParsing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.bedrock_model_arn_for_parsing
    import aws_sdk_qconnect.types.parsing_prompt


class BedrockFoundationModelConfigurationForParsing(TypedDict, closed=True):
    model_arn: (
        "aws_sdk_qconnect.types.bedrock_model_arn_for_parsing.BedrockModelArnForParsing"
    )
    """<p>The ARN of the foundation model.</p>"""
    parsing_prompt: NotRequired["aws_sdk_qconnect.types.parsing_prompt.ParsingPrompt"]
    """<p>Instructions for interpreting the contents of a document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockFoundationModelConfigurationForParsing) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    if "parsing_prompt" in value:
        import aws_sdk_qconnect.types.parsing_prompt

        out["parsingPrompt"] = aws_sdk_qconnect.types.parsing_prompt.serialize_json(
            value["parsing_prompt"]
        )
    return out


def deserialize_json(data: dict) -> BedrockFoundationModelConfigurationForParsing:
    out: BedrockFoundationModelConfigurationForParsing = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    else:
        raise DeserializationError(
            "BedrockFoundationModelConfigurationForParsing.model_arn required"
        )
    if "parsingPrompt" in data:
        import aws_sdk_qconnect.types.parsing_prompt

        out["parsing_prompt"] = aws_sdk_qconnect.types.parsing_prompt.deserialize_json(
            data["parsingPrompt"]
        )
    return out
