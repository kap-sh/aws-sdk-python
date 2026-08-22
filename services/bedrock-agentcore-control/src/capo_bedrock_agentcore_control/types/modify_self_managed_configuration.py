"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifySelfManagedConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.modify_invocation_configuration_input
    import capo_bedrock_agentcore_control.types.trigger_condition_input_list


class ModifySelfManagedConfiguration(TypedDict, closed=True):
    trigger_conditions: NotRequired[
        "capo_bedrock_agentcore_control.types.trigger_condition_input_list.TriggerConditionInputList"
    ]
    """<p>The updated list of conditions that trigger memory processing.</p>"""
    invocation_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.modify_invocation_configuration_input.ModifyInvocationConfigurationInput"
    ]
    """<p>The updated configuration to invoke self-managed memory processing pipeline.</p>"""
    historical_context_window_size: NotRequired["int"]
    """<p>The updated number of historical messages to include in processing context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifySelfManagedConfiguration) -> dict:
    out: dict = {}
    if "trigger_conditions" in value:
        import capo_bedrock_agentcore_control.types.trigger_condition_input_list

        out["triggerConditions"] = (
            capo_bedrock_agentcore_control.types.trigger_condition_input_list.serialize_json(
                value["trigger_conditions"]
            )
        )
    if "invocation_configuration" in value:
        import capo_bedrock_agentcore_control.types.modify_invocation_configuration_input

        out["invocationConfiguration"] = (
            capo_bedrock_agentcore_control.types.modify_invocation_configuration_input.serialize_json(
                value["invocation_configuration"]
            )
        )
    if "historical_context_window_size" in value:
        out["historicalContextWindowSize"] = value["historical_context_window_size"]
    return out


def deserialize_json(data: dict) -> ModifySelfManagedConfiguration:
    out: ModifySelfManagedConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("triggerConditions") is not None:
        import capo_bedrock_agentcore_control.types.trigger_condition_input_list

        out["trigger_conditions"] = (
            capo_bedrock_agentcore_control.types.trigger_condition_input_list.deserialize_json(
                data["triggerConditions"]
            )
        )
    if data.get("invocationConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.modify_invocation_configuration_input

        out["invocation_configuration"] = (
            capo_bedrock_agentcore_control.types.modify_invocation_configuration_input.deserialize_json(
                data["invocationConfiguration"]
            )
        )
    if data.get("historicalContextWindowSize") is not None:
        out["historical_context_window_size"] = data["historicalContextWindowSize"]
    return out
