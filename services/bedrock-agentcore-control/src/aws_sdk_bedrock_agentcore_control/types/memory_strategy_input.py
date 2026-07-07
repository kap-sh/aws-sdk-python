"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.custom_memory_strategy_input
    import aws_sdk_bedrock_agentcore_control.types.episodic_memory_strategy_input
    import aws_sdk_bedrock_agentcore_control.types.semantic_memory_strategy_input
    import aws_sdk_bedrock_agentcore_control.types.summary_memory_strategy_input
    import aws_sdk_bedrock_agentcore_control.types.user_preference_memory_strategy_input


class _MemoryStrategyInput_semanticMemoryStrategy(TypedDict, closed=True):
    semanticMemoryStrategy: "aws_sdk_bedrock_agentcore_control.types.semantic_memory_strategy_input.SemanticMemoryStrategyInput"


class _MemoryStrategyInput_summaryMemoryStrategy(TypedDict, closed=True):
    summaryMemoryStrategy: "aws_sdk_bedrock_agentcore_control.types.summary_memory_strategy_input.SummaryMemoryStrategyInput"


class _MemoryStrategyInput_userPreferenceMemoryStrategy(TypedDict, closed=True):
    userPreferenceMemoryStrategy: "aws_sdk_bedrock_agentcore_control.types.user_preference_memory_strategy_input.UserPreferenceMemoryStrategyInput"


class _MemoryStrategyInput_customMemoryStrategy(TypedDict, closed=True):
    customMemoryStrategy: "aws_sdk_bedrock_agentcore_control.types.custom_memory_strategy_input.CustomMemoryStrategyInput"


class _MemoryStrategyInput_episodicMemoryStrategy(TypedDict, closed=True):
    episodicMemoryStrategy: "aws_sdk_bedrock_agentcore_control.types.episodic_memory_strategy_input.EpisodicMemoryStrategyInput"


MemoryStrategyInput: TypeAlias = (
    _MemoryStrategyInput_semanticMemoryStrategy
    | _MemoryStrategyInput_summaryMemoryStrategy
    | _MemoryStrategyInput_userPreferenceMemoryStrategy
    | _MemoryStrategyInput_customMemoryStrategy
    | _MemoryStrategyInput_episodicMemoryStrategy
)


# --- restJson1 ser/de ---
def serialize_json(value: MemoryStrategyInput) -> dict:
    if "semanticMemoryStrategy" in value:
        import aws_sdk_bedrock_agentcore_control.types.semantic_memory_strategy_input

        return {
            "semanticMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.semantic_memory_strategy_input.serialize_json(
                value["semanticMemoryStrategy"]
            )
        }
    elif "summaryMemoryStrategy" in value:
        import aws_sdk_bedrock_agentcore_control.types.summary_memory_strategy_input

        return {
            "summaryMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.summary_memory_strategy_input.serialize_json(
                value["summaryMemoryStrategy"]
            )
        }
    elif "userPreferenceMemoryStrategy" in value:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_memory_strategy_input

        return {
            "userPreferenceMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.user_preference_memory_strategy_input.serialize_json(
                value["userPreferenceMemoryStrategy"]
            )
        }
    elif "customMemoryStrategy" in value:
        import aws_sdk_bedrock_agentcore_control.types.custom_memory_strategy_input

        return {
            "customMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.custom_memory_strategy_input.serialize_json(
                value["customMemoryStrategy"]
            )
        }
    elif "episodicMemoryStrategy" in value:
        import aws_sdk_bedrock_agentcore_control.types.episodic_memory_strategy_input

        return {
            "episodicMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.episodic_memory_strategy_input.serialize_json(
                value["episodicMemoryStrategy"]
            )
        }
    else:
        raise SerializationError("MemoryStrategyInput: no variant present")


def deserialize_json(data: dict) -> MemoryStrategyInput:
    if "semanticMemoryStrategy" in data:
        import aws_sdk_bedrock_agentcore_control.types.semantic_memory_strategy_input

        return {
            "semanticMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.semantic_memory_strategy_input.deserialize_json(
                data["semanticMemoryStrategy"]
            )
        }
    elif "summaryMemoryStrategy" in data:
        import aws_sdk_bedrock_agentcore_control.types.summary_memory_strategy_input

        return {
            "summaryMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.summary_memory_strategy_input.deserialize_json(
                data["summaryMemoryStrategy"]
            )
        }
    elif "userPreferenceMemoryStrategy" in data:
        import aws_sdk_bedrock_agentcore_control.types.user_preference_memory_strategy_input

        return {
            "userPreferenceMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.user_preference_memory_strategy_input.deserialize_json(
                data["userPreferenceMemoryStrategy"]
            )
        }
    elif "customMemoryStrategy" in data:
        import aws_sdk_bedrock_agentcore_control.types.custom_memory_strategy_input

        return {
            "customMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.custom_memory_strategy_input.deserialize_json(
                data["customMemoryStrategy"]
            )
        }
    elif "episodicMemoryStrategy" in data:
        import aws_sdk_bedrock_agentcore_control.types.episodic_memory_strategy_input

        return {
            "episodicMemoryStrategy": aws_sdk_bedrock_agentcore_control.types.episodic_memory_strategy_input.deserialize_json(
                data["episodicMemoryStrategy"]
            )
        }
    else:
        raise DeserializationError("MemoryStrategyInput: no recognized variant key")
