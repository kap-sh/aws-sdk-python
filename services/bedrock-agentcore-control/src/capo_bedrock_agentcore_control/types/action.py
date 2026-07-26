"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Action``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_action
    import capo_bedrock_agentcore_control.types.route_to_target_action


class _Action_configurationBundle(TypedDict, closed=True):
    configurationBundle: "capo_bedrock_agentcore_control.types.configuration_bundle_action.ConfigurationBundleAction"


class _Action_routeToTarget(TypedDict, closed=True):
    routeToTarget: "capo_bedrock_agentcore_control.types.route_to_target_action.RouteToTargetAction"


Action: TypeAlias = _Action_configurationBundle | _Action_routeToTarget


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    if "configurationBundle" in value:
        import capo_bedrock_agentcore_control.types.configuration_bundle_action

        return {
            "configurationBundle": capo_bedrock_agentcore_control.types.configuration_bundle_action.serialize_json(
                value["configurationBundle"]
            )
        }
    elif "routeToTarget" in value:
        import capo_bedrock_agentcore_control.types.route_to_target_action

        return {
            "routeToTarget": capo_bedrock_agentcore_control.types.route_to_target_action.serialize_json(
                value["routeToTarget"]
            )
        }
    else:
        raise SerializationError("Action: no variant present")


def deserialize_json(data: dict) -> Action:
    if "configurationBundle" in data:
        import capo_bedrock_agentcore_control.types.configuration_bundle_action

        return {
            "configurationBundle": capo_bedrock_agentcore_control.types.configuration_bundle_action.deserialize_json(
                data["configurationBundle"]
            )
        }
    elif "routeToTarget" in data:
        import capo_bedrock_agentcore_control.types.route_to_target_action

        return {
            "routeToTarget": capo_bedrock_agentcore_control.types.route_to_target_action.deserialize_json(
                data["routeToTarget"]
            )
        }
    else:
        raise DeserializationError("Action: no recognized variant key")
