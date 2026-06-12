"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionEvent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_input_event
    import aws_sdk_bedrock_agent_runtime.types.node_input_event
    import aws_sdk_bedrock_agent_runtime.types.flow_failure_event
    import aws_sdk_bedrock_agent_runtime.types.condition_result_event
    import aws_sdk_bedrock_agent_runtime.types.node_action_event
    import aws_sdk_bedrock_agent_runtime.types.node_failure_event
    import aws_sdk_bedrock_agent_runtime.types.node_dependency_event
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_output_event
    import aws_sdk_bedrock_agent_runtime.types.node_output_event

class _FlowExecutionEvent_flowInputEvent(TypedDict):
    flowInputEvent: "aws_sdk_bedrock_agent_runtime.types.flow_execution_input_event.FlowExecutionInputEvent"


class _FlowExecutionEvent_flowOutputEvent(TypedDict):
    flowOutputEvent: "aws_sdk_bedrock_agent_runtime.types.flow_execution_output_event.FlowExecutionOutputEvent"


class _FlowExecutionEvent_nodeInputEvent(TypedDict):
    nodeInputEvent: "aws_sdk_bedrock_agent_runtime.types.node_input_event.NodeInputEvent"


class _FlowExecutionEvent_nodeOutputEvent(TypedDict):
    nodeOutputEvent: "aws_sdk_bedrock_agent_runtime.types.node_output_event.NodeOutputEvent"


class _FlowExecutionEvent_conditionResultEvent(TypedDict):
    conditionResultEvent: "aws_sdk_bedrock_agent_runtime.types.condition_result_event.ConditionResultEvent"


class _FlowExecutionEvent_nodeFailureEvent(TypedDict):
    nodeFailureEvent: "aws_sdk_bedrock_agent_runtime.types.node_failure_event.NodeFailureEvent"


class _FlowExecutionEvent_flowFailureEvent(TypedDict):
    flowFailureEvent: "aws_sdk_bedrock_agent_runtime.types.flow_failure_event.FlowFailureEvent"


class _FlowExecutionEvent_nodeActionEvent(TypedDict):
    nodeActionEvent: "aws_sdk_bedrock_agent_runtime.types.node_action_event.NodeActionEvent"


class _FlowExecutionEvent_nodeDependencyEvent(TypedDict):
    nodeDependencyEvent: "aws_sdk_bedrock_agent_runtime.types.node_dependency_event.NodeDependencyEvent"

FlowExecutionEvent: TypeAlias = _FlowExecutionEvent_flowInputEvent | _FlowExecutionEvent_flowOutputEvent | _FlowExecutionEvent_nodeInputEvent | _FlowExecutionEvent_nodeOutputEvent | _FlowExecutionEvent_conditionResultEvent | _FlowExecutionEvent_nodeFailureEvent | _FlowExecutionEvent_flowFailureEvent | _FlowExecutionEvent_nodeActionEvent | _FlowExecutionEvent_nodeDependencyEvent

# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionEvent) -> dict:
    if "flowInputEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_input_event
        return {"flowInputEvent": aws_sdk_bedrock_agent_runtime.types.flow_execution_input_event.serialize_json(value["flowInputEvent"])}
    elif "flowOutputEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_output_event
        return {"flowOutputEvent": aws_sdk_bedrock_agent_runtime.types.flow_execution_output_event.serialize_json(value["flowOutputEvent"])}
    elif "nodeInputEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.node_input_event
        return {"nodeInputEvent": aws_sdk_bedrock_agent_runtime.types.node_input_event.serialize_json(value["nodeInputEvent"])}
    elif "nodeOutputEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.node_output_event
        return {"nodeOutputEvent": aws_sdk_bedrock_agent_runtime.types.node_output_event.serialize_json(value["nodeOutputEvent"])}
    elif "conditionResultEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.condition_result_event
        return {"conditionResultEvent": aws_sdk_bedrock_agent_runtime.types.condition_result_event.serialize_json(value["conditionResultEvent"])}
    elif "nodeFailureEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.node_failure_event
        return {"nodeFailureEvent": aws_sdk_bedrock_agent_runtime.types.node_failure_event.serialize_json(value["nodeFailureEvent"])}
    elif "flowFailureEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_failure_event
        return {"flowFailureEvent": aws_sdk_bedrock_agent_runtime.types.flow_failure_event.serialize_json(value["flowFailureEvent"])}
    elif "nodeActionEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.node_action_event
        return {"nodeActionEvent": aws_sdk_bedrock_agent_runtime.types.node_action_event.serialize_json(value["nodeActionEvent"])}
    elif "nodeDependencyEvent" in value:
        import aws_sdk_bedrock_agent_runtime.types.node_dependency_event
        return {"nodeDependencyEvent": aws_sdk_bedrock_agent_runtime.types.node_dependency_event.serialize_json(value["nodeDependencyEvent"])}
    else:
        raise SerializationError("FlowExecutionEvent: no variant present")


def deserialize_json(data: dict) -> FlowExecutionEvent:
    if "flowInputEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_input_event
        return {"flowInputEvent": aws_sdk_bedrock_agent_runtime.types.flow_execution_input_event.deserialize_json(data["flowInputEvent"])}
    elif "flowOutputEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_output_event
        return {"flowOutputEvent": aws_sdk_bedrock_agent_runtime.types.flow_execution_output_event.deserialize_json(data["flowOutputEvent"])}
    elif "nodeInputEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_input_event
        return {"nodeInputEvent": aws_sdk_bedrock_agent_runtime.types.node_input_event.deserialize_json(data["nodeInputEvent"])}
    elif "nodeOutputEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_output_event
        return {"nodeOutputEvent": aws_sdk_bedrock_agent_runtime.types.node_output_event.deserialize_json(data["nodeOutputEvent"])}
    elif "conditionResultEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.condition_result_event
        return {"conditionResultEvent": aws_sdk_bedrock_agent_runtime.types.condition_result_event.deserialize_json(data["conditionResultEvent"])}
    elif "nodeFailureEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_failure_event
        return {"nodeFailureEvent": aws_sdk_bedrock_agent_runtime.types.node_failure_event.deserialize_json(data["nodeFailureEvent"])}
    elif "flowFailureEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_failure_event
        return {"flowFailureEvent": aws_sdk_bedrock_agent_runtime.types.flow_failure_event.deserialize_json(data["flowFailureEvent"])}
    elif "nodeActionEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_action_event
        return {"nodeActionEvent": aws_sdk_bedrock_agent_runtime.types.node_action_event.deserialize_json(data["nodeActionEvent"])}
    elif "nodeDependencyEvent" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_dependency_event
        return {"nodeDependencyEvent": aws_sdk_bedrock_agent_runtime.types.node_dependency_event.deserialize_json(data["nodeDependencyEvent"])}
    else:
        raise DeserializationError("FlowExecutionEvent: no recognized variant key")