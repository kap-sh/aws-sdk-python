"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTrace``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agent_runtime.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_event
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_action_event
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_event
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_condition_node_result_event
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_dependency_event

class _FlowTrace_nodeInputTrace(TypedDict):
    nodeInputTrace: "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_event.FlowTraceNodeInputEvent"


class _FlowTrace_nodeOutputTrace(TypedDict):
    nodeOutputTrace: "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_event.FlowTraceNodeOutputEvent"


class _FlowTrace_conditionNodeResultTrace(TypedDict):
    conditionNodeResultTrace: "aws_sdk_bedrock_agent_runtime.types.flow_trace_condition_node_result_event.FlowTraceConditionNodeResultEvent"


class _FlowTrace_nodeActionTrace(TypedDict):
    nodeActionTrace: "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_action_event.FlowTraceNodeActionEvent"


class _FlowTrace_nodeDependencyTrace(TypedDict):
    nodeDependencyTrace: "aws_sdk_bedrock_agent_runtime.types.flow_trace_dependency_event.FlowTraceDependencyEvent"

FlowTrace: TypeAlias = _FlowTrace_nodeInputTrace | _FlowTrace_nodeOutputTrace | _FlowTrace_conditionNodeResultTrace | _FlowTrace_nodeActionTrace | _FlowTrace_nodeDependencyTrace

# --- restJson1 ser/de ---
def serialize_json(value: FlowTrace) -> dict:
    if "nodeInputTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_event
        return {"nodeInputTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_event.serialize_json(value["nodeInputTrace"])}
    elif "nodeOutputTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_event
        return {"nodeOutputTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_event.serialize_json(value["nodeOutputTrace"])}
    elif "conditionNodeResultTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_condition_node_result_event
        return {"conditionNodeResultTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_condition_node_result_event.serialize_json(value["conditionNodeResultTrace"])}
    elif "nodeActionTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_action_event
        return {"nodeActionTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_node_action_event.serialize_json(value["nodeActionTrace"])}
    elif "nodeDependencyTrace" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_dependency_event
        return {"nodeDependencyTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_dependency_event.serialize_json(value["nodeDependencyTrace"])}
    else:
        raise SerializationError("FlowTrace: no variant present")


def deserialize_json(data: dict) -> FlowTrace:
    if "nodeInputTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_event
        return {"nodeInputTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_event.deserialize_json(data["nodeInputTrace"])}
    elif "nodeOutputTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_event
        return {"nodeOutputTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_event.deserialize_json(data["nodeOutputTrace"])}
    elif "conditionNodeResultTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_condition_node_result_event
        return {"conditionNodeResultTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_condition_node_result_event.deserialize_json(data["conditionNodeResultTrace"])}
    elif "nodeActionTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_action_event
        return {"nodeActionTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_node_action_event.deserialize_json(data["nodeActionTrace"])}
    elif "nodeDependencyTrace" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_dependency_event
        return {"nodeDependencyTrace": aws_sdk_bedrock_agent_runtime.types.flow_trace_dependency_event.deserialize_json(data["nodeDependencyTrace"])}
    else:
        raise DeserializationError("FlowTrace: no recognized variant key")