"""Generated from Smithy shape ``com.amazonaws.qconnect#ParsingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.bedrock_foundation_model_configuration_for_parsing
    import aws_sdk_qconnect.types.parsing_strategy


class ParsingConfiguration(TypedDict):
    parsing_strategy: "aws_sdk_qconnect.types.parsing_strategy.ParsingStrategy"
    """<p>The parsing strategy for the data source.</p>"""
    bedrock_foundation_model_configuration: NotRequired[
        "aws_sdk_qconnect.types.bedrock_foundation_model_configuration_for_parsing.BedrockFoundationModelConfigurationForParsing"
    ]
    """<p>Settings for a foundation model used to parse documents for a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParsingConfiguration) -> dict:
    out: dict = {}
    out["parsingStrategy"] = value["parsing_strategy"]
    if "bedrock_foundation_model_configuration" in value:
        import aws_sdk_qconnect.types.bedrock_foundation_model_configuration_for_parsing

        out["bedrockFoundationModelConfiguration"] = (
            aws_sdk_qconnect.types.bedrock_foundation_model_configuration_for_parsing.serialize_json(
                value["bedrock_foundation_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParsingConfiguration:
    out: ParsingConfiguration = {}  # type: ignore[typeddict-item]
    if "parsingStrategy" in data:
        out["parsing_strategy"] = data["parsingStrategy"]
    else:
        raise DeserializationError("ParsingConfiguration.parsing_strategy required")
    if "bedrockFoundationModelConfiguration" in data:
        import aws_sdk_qconnect.types.bedrock_foundation_model_configuration_for_parsing

        out["bedrock_foundation_model_configuration"] = (
            aws_sdk_qconnect.types.bedrock_foundation_model_configuration_for_parsing.deserialize_json(
                data["bedrockFoundationModelConfiguration"]
            )
        )
    return out
