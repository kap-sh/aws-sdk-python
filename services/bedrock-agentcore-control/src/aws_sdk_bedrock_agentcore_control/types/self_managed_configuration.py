"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SelfManagedConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.invocation_configuration
    import aws_sdk_bedrock_agentcore_control.types.trigger_conditions_list


class SelfManagedConfiguration(TypedDict, closed=True):
    trigger_conditions: "aws_sdk_bedrock_agentcore_control.types.trigger_conditions_list.TriggerConditionsList"
    """<p>A list of conditions that trigger memory processing.</p>"""
    invocation_configuration: "aws_sdk_bedrock_agentcore_control.types.invocation_configuration.InvocationConfiguration"
    """<p>The configuration to use when invoking memory processing.</p>"""
    historical_context_window_size: "int"
    """<p>The number of historical messages to include in processing context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.trigger_conditions_list

    out["triggerConditions"] = (
        aws_sdk_bedrock_agentcore_control.types.trigger_conditions_list.serialize_json(
            value["trigger_conditions"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.invocation_configuration

    out["invocationConfiguration"] = (
        aws_sdk_bedrock_agentcore_control.types.invocation_configuration.serialize_json(
            value["invocation_configuration"]
        )
    )
    out["historicalContextWindowSize"] = value["historical_context_window_size"]
    return out


def deserialize_json(data: dict) -> SelfManagedConfiguration:
    out: SelfManagedConfiguration = {}  # type: ignore[typeddict-item]
    if "triggerConditions" in data:
        import aws_sdk_bedrock_agentcore_control.types.trigger_conditions_list

        out["trigger_conditions"] = (
            aws_sdk_bedrock_agentcore_control.types.trigger_conditions_list.deserialize_json(
                data["triggerConditions"]
            )
        )
    else:
        raise DeserializationError(
            "SelfManagedConfiguration.trigger_conditions required"
        )
    if "invocationConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.invocation_configuration

        out["invocation_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.invocation_configuration.deserialize_json(
                data["invocationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SelfManagedConfiguration.invocation_configuration required"
        )
    if "historicalContextWindowSize" in data:
        out["historical_context_window_size"] = data["historicalContextWindowSize"]
    else:
        raise DeserializationError(
            "SelfManagedConfiguration.historical_context_window_size required"
        )
    return out
