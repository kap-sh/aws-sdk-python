"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Observation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.action_group_invocation_output
    import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_output
    import aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_output
    import aws_sdk_bedrock_agent_runtime.types.final_response
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_output
    import aws_sdk_bedrock_agent_runtime.types.reprompt_response
    import aws_sdk_bedrock_agent_runtime.types.trace_id
    import aws_sdk_bedrock_agent_runtime.types.type


class Observation(TypedDict, closed=True):
    trace_id: NotRequired["aws_sdk_bedrock_agent_runtime.types.trace_id.TraceId"]
    """<p>The unique identifier of the trace.</p>"""
    type: NotRequired["aws_sdk_bedrock_agent_runtime.types.type.Type"]
    """<p>Specifies what kind of information the agent returns in the observation. The following values are possible.</p> <ul> <li> <p> <code>ACTION_GROUP</code> – The agent returns the result of an action group.</p> </li> <li> <p> <code>KNOWLEDGE_BASE</code> – The agent returns information from a knowledge base.</p> </li> <li> <p> <code>FINISH</code> – The agent returns a final response to the user with no follow-up.</p> </li> <li> <p> <code>ASK_USER</code> – The agent asks the user a question.</p> </li> <li> <p> <code>REPROMPT</code> – The agent prompts the user again for the same information.</p> </li> </ul>"""
    action_group_invocation_output: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.action_group_invocation_output.ActionGroupInvocationOutput"
    ]
    """<p>Contains the JSON-formatted string returned by the API invoked by the action group.</p>"""
    agent_collaborator_invocation_output: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_output.AgentCollaboratorInvocationOutput"
    ]
    """<p>A collaborator's invocation output.</p>"""
    knowledge_base_lookup_output: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_output.KnowledgeBaseLookupOutput"
    ]
    """<p>Contains details about the results from looking up the knowledge base.</p>"""
    final_response: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.final_response.FinalResponse"
    ]
    """<p>Contains details about the response to the user.</p>"""
    reprompt_response: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.reprompt_response.RepromptResponse"
    ]
    """<p>Contains details about the response to reprompt the input.</p>"""
    code_interpreter_invocation_output: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_output.CodeInterpreterInvocationOutput"
    ]
    """<p>Contains the JSON-formatted string returned by the API invoked by the code interpreter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Observation) -> dict:
    out: dict = {}
    if "trace_id" in value:
        out["traceId"] = value["trace_id"]
    if "type" in value:
        import aws_sdk_bedrock_agent_runtime.types.type

        out["type"] = aws_sdk_bedrock_agent_runtime.types.type.serialize_json(
            value["type"]
        )
    if "action_group_invocation_output" in value:
        import aws_sdk_bedrock_agent_runtime.types.action_group_invocation_output

        out["actionGroupInvocationOutput"] = (
            aws_sdk_bedrock_agent_runtime.types.action_group_invocation_output.serialize_json(
                value["action_group_invocation_output"]
            )
        )
    if "agent_collaborator_invocation_output" in value:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_output

        out["agentCollaboratorInvocationOutput"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_output.serialize_json(
                value["agent_collaborator_invocation_output"]
            )
        )
    if "knowledge_base_lookup_output" in value:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_output

        out["knowledgeBaseLookupOutput"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_output.serialize_json(
                value["knowledge_base_lookup_output"]
            )
        )
    if "final_response" in value:
        import aws_sdk_bedrock_agent_runtime.types.final_response

        out["finalResponse"] = (
            aws_sdk_bedrock_agent_runtime.types.final_response.serialize_json(
                value["final_response"]
            )
        )
    if "reprompt_response" in value:
        import aws_sdk_bedrock_agent_runtime.types.reprompt_response

        out["repromptResponse"] = (
            aws_sdk_bedrock_agent_runtime.types.reprompt_response.serialize_json(
                value["reprompt_response"]
            )
        )
    if "code_interpreter_invocation_output" in value:
        import aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_output

        out["codeInterpreterInvocationOutput"] = (
            aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_output.serialize_json(
                value["code_interpreter_invocation_output"]
            )
        )
    return out


def deserialize_json(data: dict) -> Observation:
    out: Observation = {}  # type: ignore[typeddict-item]
    if "traceId" in data:
        out["trace_id"] = data["traceId"]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.type

        out["type"] = aws_sdk_bedrock_agent_runtime.types.type.deserialize_json(
            data["type"]
        )
    if "actionGroupInvocationOutput" in data:
        import aws_sdk_bedrock_agent_runtime.types.action_group_invocation_output

        out["action_group_invocation_output"] = (
            aws_sdk_bedrock_agent_runtime.types.action_group_invocation_output.deserialize_json(
                data["actionGroupInvocationOutput"]
            )
        )
    if "agentCollaboratorInvocationOutput" in data:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_output

        out["agent_collaborator_invocation_output"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaborator_invocation_output.deserialize_json(
                data["agentCollaboratorInvocationOutput"]
            )
        )
    if "knowledgeBaseLookupOutput" in data:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_output

        out["knowledge_base_lookup_output"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_base_lookup_output.deserialize_json(
                data["knowledgeBaseLookupOutput"]
            )
        )
    if "finalResponse" in data:
        import aws_sdk_bedrock_agent_runtime.types.final_response

        out["final_response"] = (
            aws_sdk_bedrock_agent_runtime.types.final_response.deserialize_json(
                data["finalResponse"]
            )
        )
    if "repromptResponse" in data:
        import aws_sdk_bedrock_agent_runtime.types.reprompt_response

        out["reprompt_response"] = (
            aws_sdk_bedrock_agent_runtime.types.reprompt_response.deserialize_json(
                data["repromptResponse"]
            )
        )
    if "codeInterpreterInvocationOutput" in data:
        import aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_output

        out["code_interpreter_invocation_output"] = (
            aws_sdk_bedrock_agent_runtime.types.code_interpreter_invocation_output.deserialize_json(
                data["codeInterpreterInvocationOutput"]
            )
        )
    return out
