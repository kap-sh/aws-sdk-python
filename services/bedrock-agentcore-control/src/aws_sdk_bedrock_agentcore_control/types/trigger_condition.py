"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TriggerCondition``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.message_based_trigger
    import aws_sdk_bedrock_agentcore_control.types.time_based_trigger
    import aws_sdk_bedrock_agentcore_control.types.token_based_trigger


class _TriggerCondition_messageBasedTrigger(TypedDict):
    messageBasedTrigger: "aws_sdk_bedrock_agentcore_control.types.message_based_trigger.MessageBasedTrigger"


class _TriggerCondition_tokenBasedTrigger(TypedDict):
    tokenBasedTrigger: (
        "aws_sdk_bedrock_agentcore_control.types.token_based_trigger.TokenBasedTrigger"
    )


class _TriggerCondition_timeBasedTrigger(TypedDict):
    timeBasedTrigger: (
        "aws_sdk_bedrock_agentcore_control.types.time_based_trigger.TimeBasedTrigger"
    )


TriggerCondition: TypeAlias = (
    _TriggerCondition_messageBasedTrigger
    | _TriggerCondition_tokenBasedTrigger
    | _TriggerCondition_timeBasedTrigger
)


# --- restJson1 ser/de ---
def serialize_json(value: TriggerCondition) -> dict:
    if "messageBasedTrigger" in value:
        import aws_sdk_bedrock_agentcore_control.types.message_based_trigger

        return {
            "messageBasedTrigger": aws_sdk_bedrock_agentcore_control.types.message_based_trigger.serialize_json(
                value["messageBasedTrigger"]
            )
        }
    elif "tokenBasedTrigger" in value:
        import aws_sdk_bedrock_agentcore_control.types.token_based_trigger

        return {
            "tokenBasedTrigger": aws_sdk_bedrock_agentcore_control.types.token_based_trigger.serialize_json(
                value["tokenBasedTrigger"]
            )
        }
    elif "timeBasedTrigger" in value:
        import aws_sdk_bedrock_agentcore_control.types.time_based_trigger

        return {
            "timeBasedTrigger": aws_sdk_bedrock_agentcore_control.types.time_based_trigger.serialize_json(
                value["timeBasedTrigger"]
            )
        }
    else:
        raise SerializationError("TriggerCondition: no variant present")


def deserialize_json(data: dict) -> TriggerCondition:
    if "messageBasedTrigger" in data:
        import aws_sdk_bedrock_agentcore_control.types.message_based_trigger

        return {
            "messageBasedTrigger": aws_sdk_bedrock_agentcore_control.types.message_based_trigger.deserialize_json(
                data["messageBasedTrigger"]
            )
        }
    elif "tokenBasedTrigger" in data:
        import aws_sdk_bedrock_agentcore_control.types.token_based_trigger

        return {
            "tokenBasedTrigger": aws_sdk_bedrock_agentcore_control.types.token_based_trigger.deserialize_json(
                data["tokenBasedTrigger"]
            )
        }
    elif "timeBasedTrigger" in data:
        import aws_sdk_bedrock_agentcore_control.types.time_based_trigger

        return {
            "timeBasedTrigger": aws_sdk_bedrock_agentcore_control.types.time_based_trigger.deserialize_json(
                data["timeBasedTrigger"]
            )
        }
    else:
        raise DeserializationError("TriggerCondition: no recognized variant key")
