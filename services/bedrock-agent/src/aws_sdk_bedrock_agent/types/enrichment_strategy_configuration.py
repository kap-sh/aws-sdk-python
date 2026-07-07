"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EnrichmentStrategyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.enrichment_strategy_method


class EnrichmentStrategyConfiguration(TypedDict, closed=True):
    method: "aws_sdk_bedrock_agent.types.enrichment_strategy_method.EnrichmentStrategyMethod"
    """<p>The method used for the context enrichment strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentStrategyConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.enrichment_strategy_method

    out["method"] = (
        aws_sdk_bedrock_agent.types.enrichment_strategy_method.serialize_json(
            value["method"]
        )
    )
    return out


def deserialize_json(data: dict) -> EnrichmentStrategyConfiguration:
    out: EnrichmentStrategyConfiguration = {}  # type: ignore[typeddict-item]
    if "method" in data:
        import aws_sdk_bedrock_agent.types.enrichment_strategy_method

        out["method"] = (
            aws_sdk_bedrock_agent.types.enrichment_strategy_method.deserialize_json(
                data["method"]
            )
        )
    else:
        raise DeserializationError("EnrichmentStrategyConfiguration.method required")
    return out
