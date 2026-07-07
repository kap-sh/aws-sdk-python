"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessTruncationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy
    import aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy_configuration


class HarnessTruncationConfiguration(TypedDict, closed=True):
    strategy: "aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy.HarnessTruncationStrategy"
    """<p>The truncation strategy to use.</p>"""
    config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy_configuration.HarnessTruncationStrategyConfiguration"
    ]
    """<p>The strategy-specific configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTruncationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy

    out["strategy"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy.serialize_json(
            value["strategy"]
        )
    )
    if "config" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy_configuration

        out["config"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy_configuration.serialize_json(
                value["config"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessTruncationConfiguration:
    out: HarnessTruncationConfiguration = {}  # type: ignore[typeddict-item]
    if "strategy" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy

        out["strategy"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy.deserialize_json(
                data["strategy"]
            )
        )
    else:
        raise DeserializationError("HarnessTruncationConfiguration.strategy required")
    if "config" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy_configuration

        out["config"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_truncation_strategy_configuration.deserialize_json(
                data["config"]
            )
        )
    return out
