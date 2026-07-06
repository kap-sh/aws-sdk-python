"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TriggerConditionInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.message_based_trigger_input
    import aws_sdk_bedrock_agentcore_control.types.time_based_trigger_input
    import aws_sdk_bedrock_agentcore_control.types.token_based_trigger_input


class _TriggerConditionInput_messageBasedTrigger(TypedDict, closed=True):
    messageBasedTrigger: "aws_sdk_bedrock_agentcore_control.types.message_based_trigger_input.MessageBasedTriggerInput"


class _TriggerConditionInput_tokenBasedTrigger(TypedDict, closed=True):
    tokenBasedTrigger: "aws_sdk_bedrock_agentcore_control.types.token_based_trigger_input.TokenBasedTriggerInput"


class _TriggerConditionInput_timeBasedTrigger(TypedDict, closed=True):
    timeBasedTrigger: "aws_sdk_bedrock_agentcore_control.types.time_based_trigger_input.TimeBasedTriggerInput"


TriggerConditionInput: TypeAlias = (
    _TriggerConditionInput_messageBasedTrigger
    | _TriggerConditionInput_tokenBasedTrigger
    | _TriggerConditionInput_timeBasedTrigger
)


# --- restJson1 ser/de ---
def serialize_json(value: TriggerConditionInput) -> dict:
    if "messageBasedTrigger" in value:
        import aws_sdk_bedrock_agentcore_control.types.message_based_trigger_input

        return {
            "messageBasedTrigger": aws_sdk_bedrock_agentcore_control.types.message_based_trigger_input.serialize_json(
                value["messageBasedTrigger"]
            )
        }
    elif "tokenBasedTrigger" in value:
        import aws_sdk_bedrock_agentcore_control.types.token_based_trigger_input

        return {
            "tokenBasedTrigger": aws_sdk_bedrock_agentcore_control.types.token_based_trigger_input.serialize_json(
                value["tokenBasedTrigger"]
            )
        }
    elif "timeBasedTrigger" in value:
        import aws_sdk_bedrock_agentcore_control.types.time_based_trigger_input

        return {
            "timeBasedTrigger": aws_sdk_bedrock_agentcore_control.types.time_based_trigger_input.serialize_json(
                value["timeBasedTrigger"]
            )
        }
    else:
        raise SerializationError("TriggerConditionInput: no variant present")


def deserialize_json(data: dict) -> TriggerConditionInput:
    if "messageBasedTrigger" in data:
        import aws_sdk_bedrock_agentcore_control.types.message_based_trigger_input

        return {
            "messageBasedTrigger": aws_sdk_bedrock_agentcore_control.types.message_based_trigger_input.deserialize_json(
                data["messageBasedTrigger"]
            )
        }
    elif "tokenBasedTrigger" in data:
        import aws_sdk_bedrock_agentcore_control.types.token_based_trigger_input

        return {
            "tokenBasedTrigger": aws_sdk_bedrock_agentcore_control.types.token_based_trigger_input.deserialize_json(
                data["tokenBasedTrigger"]
            )
        }
    elif "timeBasedTrigger" in data:
        import aws_sdk_bedrock_agentcore_control.types.time_based_trigger_input

        return {
            "timeBasedTrigger": aws_sdk_bedrock_agentcore_control.types.time_based_trigger_input.deserialize_json(
                data["timeBasedTrigger"]
            )
        }
    else:
        raise DeserializationError("TriggerConditionInput: no recognized variant key")
