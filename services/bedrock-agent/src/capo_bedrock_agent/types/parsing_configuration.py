"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ParsingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.bedrock_data_automation_configuration
    import capo_bedrock_agent.types.bedrock_foundation_model_configuration
    import capo_bedrock_agent.types.parsing_strategy


class ParsingConfiguration(TypedDict, closed=True):
    parsing_strategy: "capo_bedrock_agent.types.parsing_strategy.ParsingStrategy"
    """<p>The parsing strategy for the data source.</p>"""
    bedrock_foundation_model_configuration: NotRequired[
        "capo_bedrock_agent.types.bedrock_foundation_model_configuration.BedrockFoundationModelConfiguration"
    ]
    """<p>If you specify <code>BEDROCK_FOUNDATION_MODEL</code> as the parsing strategy for ingesting your data source, use this object to modify configurations for using a foundation model to parse documents.</p>"""
    bedrock_data_automation_configuration: NotRequired[
        "capo_bedrock_agent.types.bedrock_data_automation_configuration.BedrockDataAutomationConfiguration"
    ]
    """<p>If you specify <code>BEDROCK_DATA_AUTOMATION</code> as the parsing strategy for ingesting your data source, use this object to modify configurations for using the Amazon Bedrock Data Automation parser.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParsingConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.parsing_strategy

    out["parsingStrategy"] = capo_bedrock_agent.types.parsing_strategy.serialize_json(
        value["parsing_strategy"]
    )
    if "bedrock_foundation_model_configuration" in value:
        import capo_bedrock_agent.types.bedrock_foundation_model_configuration

        out["bedrockFoundationModelConfiguration"] = (
            capo_bedrock_agent.types.bedrock_foundation_model_configuration.serialize_json(
                value["bedrock_foundation_model_configuration"]
            )
        )
    if "bedrock_data_automation_configuration" in value:
        import capo_bedrock_agent.types.bedrock_data_automation_configuration

        out["bedrockDataAutomationConfiguration"] = (
            capo_bedrock_agent.types.bedrock_data_automation_configuration.serialize_json(
                value["bedrock_data_automation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParsingConfiguration:
    out: ParsingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("parsingStrategy") is not None:
        import capo_bedrock_agent.types.parsing_strategy

        out["parsing_strategy"] = (
            capo_bedrock_agent.types.parsing_strategy.deserialize_json(
                data["parsingStrategy"]
            )
        )
    else:
        raise DeserializationError("ParsingConfiguration.parsing_strategy required")
    if data.get("bedrockFoundationModelConfiguration") is not None:
        import capo_bedrock_agent.types.bedrock_foundation_model_configuration

        out["bedrock_foundation_model_configuration"] = (
            capo_bedrock_agent.types.bedrock_foundation_model_configuration.deserialize_json(
                data["bedrockFoundationModelConfiguration"]
            )
        )
    if data.get("bedrockDataAutomationConfiguration") is not None:
        import capo_bedrock_agent.types.bedrock_data_automation_configuration

        out["bedrock_data_automation_configuration"] = (
            capo_bedrock_agent.types.bedrock_data_automation_configuration.deserialize_json(
                data["bedrockDataAutomationConfiguration"]
            )
        )
    return out
