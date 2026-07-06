"""Generated from Smithy shape ``com.amazonaws.bedrockagent#BedrockDataAutomationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.parsing_modality


class BedrockDataAutomationConfiguration(TypedDict, closed=True):
    parsing_modality: NotRequired[
        "aws_sdk_bedrock_agent.types.parsing_modality.ParsingModality"
    ]
    """<p>Specifies whether to enable parsing of multimodal data, including both text and/or images.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockDataAutomationConfiguration) -> dict:
    out: dict = {}
    if "parsing_modality" in value:
        import aws_sdk_bedrock_agent.types.parsing_modality

        out["parsingModality"] = (
            aws_sdk_bedrock_agent.types.parsing_modality.serialize_json(
                value["parsing_modality"]
            )
        )
    return out


def deserialize_json(data: dict) -> BedrockDataAutomationConfiguration:
    out: BedrockDataAutomationConfiguration = {}  # type: ignore[typeddict-item]
    if "parsingModality" in data:
        import aws_sdk_bedrock_agent.types.parsing_modality

        out["parsing_modality"] = (
            aws_sdk_bedrock_agent.types.parsing_modality.deserialize_json(
                data["parsingModality"]
            )
        )
    return out
