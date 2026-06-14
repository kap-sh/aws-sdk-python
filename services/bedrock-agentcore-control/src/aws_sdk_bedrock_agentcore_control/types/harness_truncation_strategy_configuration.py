"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessTruncationStrategyConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_sliding_window_configuration
    import aws_sdk_bedrock_agentcore_control.types.harness_summarization_configuration


class _HarnessTruncationStrategyConfiguration_slidingWindow(TypedDict):
    slidingWindow: "aws_sdk_bedrock_agentcore_control.types.harness_sliding_window_configuration.HarnessSlidingWindowConfiguration"


class _HarnessTruncationStrategyConfiguration_summarization(TypedDict):
    summarization: "aws_sdk_bedrock_agentcore_control.types.harness_summarization_configuration.HarnessSummarizationConfiguration"


HarnessTruncationStrategyConfiguration: TypeAlias = (
    _HarnessTruncationStrategyConfiguration_slidingWindow
    | _HarnessTruncationStrategyConfiguration_summarization
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTruncationStrategyConfiguration) -> dict:
    if "slidingWindow" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_sliding_window_configuration

        return {
            "slidingWindow": aws_sdk_bedrock_agentcore_control.types.harness_sliding_window_configuration.serialize_json(
                value["slidingWindow"]
            )
        }
    elif "summarization" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_summarization_configuration

        return {
            "summarization": aws_sdk_bedrock_agentcore_control.types.harness_summarization_configuration.serialize_json(
                value["summarization"]
            )
        }
    else:
        raise SerializationError(
            "HarnessTruncationStrategyConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> HarnessTruncationStrategyConfiguration:
    if "slidingWindow" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_sliding_window_configuration

        return {
            "slidingWindow": aws_sdk_bedrock_agentcore_control.types.harness_sliding_window_configuration.deserialize_json(
                data["slidingWindow"]
            )
        }
    elif "summarization" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_summarization_configuration

        return {
            "summarization": aws_sdk_bedrock_agentcore_control.types.harness_summarization_configuration.deserialize_json(
                data["summarization"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessTruncationStrategyConfiguration: no recognized variant key"
        )
