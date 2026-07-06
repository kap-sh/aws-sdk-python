"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.action_group_invocation_input
    import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_input
    import aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_input
    import aws_sdk_bedrock_agent_runtime.types.invocation_type
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_input
    import aws_sdk_bedrock_agent_runtime.types.trace_id


class InvocationInput(TypedDict, closed=True):
    trace_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p>The unique identifier of the trace.</p>"""
    invocation_type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.invocation_type.InvocationType"
    ]
    """<p>Specifies whether the agent is invoking an action group or a knowledge base.</p>"""
    action_group_invocation_input: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.action_group_invocation_input.ActionGroupInvocationInput"
    ]
    """<p>Contains information about the action group to be invoked.</p>"""
    knowledge_base_lookup_input: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_input.KnowledgeBaseLookupInput"
    ]
    """<p>Contains details about the knowledge base to look up and the query to be made.</p>"""
    code_interpreter_invocation_input: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_input.CodeInterpreterInvocationInput"
    ]
    """<p>Contains information about the code interpreter to be invoked.</p>"""
    agent_collaborator_invocation_input: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_input.AgentCollaboratorInvocationInput"
    ]
    """<p>The collaborator's invocation input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationInput) -> dict:
    out: dict = {}
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "invocation_type" in value:
        import aws_sdk_bedrock_agent_runtime.types.invocation_type

        out["invocationType"] = (
            aws_sdk_bedrock_agent_runtime.types.invocation_type.serialize_json(
                value["invocation_type"]
            )
        )
    if "action_group_invocation_input" in value:
        import aws_sdk_bedrock_agent_runtime.types.action_group_invocation_input

        out["actionGroupInvocationInput"] = (
            aws_sdk_bedrock_agent_runtime.types.action_group_invocation_input.serialize_json(
                value["action_group_invocation_input"]
            )
        )
    if "knowledge_base_lookup_input" in value:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_input

        out["knowledgeBaseLookupInput"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_input.serialize_json(
                value["knowledge_base_lookup_input"]
            )
        )
    if "code_interpreter_invocation_input" in value:
        import aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_input

        out["codeInterpreterInvocationInput"] = (
            aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_input.serialize_json(
                value["code_interpreter_invocation_input"]
            )
        )
    if "agent_collaborator_invocation_input" in value:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_input

        out["agentCollaboratorInvocationInput"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_input.serialize_json(
                value["agent_collaborator_invocation_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvocationInput:
    out: InvocationInput = {}  # type: ignore[typeddict-item]
    if "traceId" in data:
        out["trace_id"] = data["traceId"]
    if "invocationType" in data:
        import aws_sdk_bedrock_agent_runtime.types.invocation_type

        out["invocation_type"] = (
            aws_sdk_bedrock_agent_runtime.types.invocation_type.deserialize_json(
                data["invocationType"]
            )
        )
    if "actionGroupInvocationInput" in data:
        import aws_sdk_bedrock_agent_runtime.types.action_group_invocation_input

        out["action_group_invocation_input"] = (
            aws_sdk_bedrock_agent_runtime.types.action_group_invocation_input.deserialize_json(
                data["actionGroupInvocationInput"]
            )
        )
    if "knowledgeBaseLookupInput" in data:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_input

        out["knowledge_base_lookup_input"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_input.deserialize_json(
                data["knowledgeBaseLookupInput"]
            )
        )
    if "codeInterpreterInvocationInput" in data:
        import aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_input

        out["code_interpreter_invocation_input"] = (
            aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_input.deserialize_json(
                data["codeInterpreterInvocationInput"]
            )
        )
    if "agentCollaboratorInvocationInput" in data:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_input

        out["agent_collaborator_invocation_input"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_input.deserialize_json(
                data["agentCollaboratorInvocationInput"]
            )
        )
    return out
