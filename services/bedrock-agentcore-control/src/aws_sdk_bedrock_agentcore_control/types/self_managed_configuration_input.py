"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SelfManagedConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.invocation_configuration_input
    import aws_sdk_bedrock_agentcore_control.types.trigger_condition_input_list


class SelfManagedConfigurationInput(TypedDict, closed=True):
    trigger_conditions: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.trigger_condition_input_list.TriggerConditionInputList"
    ]
    """<p>A list of conditions that trigger memory processing.</p>"""
    invocation_configuration: "aws_sdk_bedrock_agentcore_control.types.invocation_configuration_input.InvocationConfigurationInput"
    """<p>Configuration to invoke a self-managed memory processing pipeline with.</p>"""
    historical_context_window_size: "int"
    """<p>Number of historical messages to include in processing context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedConfigurationInput) -> dict:
    out: dict = {}
    if "trigger_conditions" in value:
        import aws_sdk_bedrock_agentcore_control.types.trigger_condition_input_list

        out["triggerConditions"] = (
            aws_sdk_bedrock_agentcore_control.types.trigger_condition_input_list.serialize_json(
                value["trigger_conditions"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types.invocation_configuration_input

    out["invocationConfiguration"] = (
        aws_sdk_bedrock_agentcore_control.types.invocation_configuration_input.serialize_json(
            value["invocation_configuration"]
        )
    )
    out["historicalContextWindowSize"] = value.get("historical_context_window_size", 4)
    return out


def deserialize_json(data: dict) -> SelfManagedConfigurationInput:
    out: SelfManagedConfigurationInput = {}  # type: ignore[typeddict-item]
    if "triggerConditions" in data:
        import aws_sdk_bedrock_agentcore_control.types.trigger_condition_input_list

        out["trigger_conditions"] = (
            aws_sdk_bedrock_agentcore_control.types.trigger_condition_input_list.deserialize_json(
                data["triggerConditions"]
            )
        )
    if "invocationConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.invocation_configuration_input

        out["invocation_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.invocation_configuration_input.deserialize_json(
                data["invocationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SelfManagedConfigurationInput.invocation_configuration required"
        )
    if "historicalContextWindowSize" in data:
        out["historical_context_window_size"] = data["historicalContextWindowSize"]
    else:
        out["historical_context_window_size"] = 4
    return out
