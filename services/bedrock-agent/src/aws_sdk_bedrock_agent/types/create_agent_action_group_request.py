"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateAgentActionGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.action_group_executor
    import aws_sdk_bedrock_agent.types.action_group_signature
    import aws_sdk_bedrock_agent.types.action_group_signature_params
    import aws_sdk_bedrock_agent.types.action_group_state
    import aws_sdk_bedrock_agent.types.api_schema
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.draft_version
    import aws_sdk_bedrock_agent.types.function_schema
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name


class CreateAgentActionGroupRequest(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent for which to create the action group.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the agent for which to create the action group.</p>"""
    action_group_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name to give the action group.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>A description of the action group.</p>"""
    parent_action_group_signature: NotRequired[
        "aws_sdk_bedrock_agent.types.action_group_signature.ActionGroupSignature"
    ]
    """<p>Specify a built-in or computer use action for this action group. If you specify a value, you must leave the <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields empty for this action group. </p> <ul> <li> <p>To allow your agent to request the user for additional information when trying to complete a task, set this field to <code>AMAZON.UserInput</code>. </p> </li> <li> <p>To allow your agent to generate, run, and troubleshoot code when trying to complete a task, set this field to <code>AMAZON.CodeInterpreter</code>.</p> </li> <li> <p>To allow your agent to use an Anthropic computer use tool, specify one of the following values. </p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. When operating computer use functionality, we recommend taking additional security precautions, such as executing computer actions in virtual environments with restricted data access and limited internet connectivity. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html\">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important> <ul> <li> <p> <code>ANTHROPIC.Computer</code> - Gives the agent permission to use the mouse and keyboard and take screenshots.</p> </li> <li> <p> <code>ANTHROPIC.TextEditor</code> - Gives the agent permission to view, create and edit files.</p> </li> <li> <p> <code>ANTHROPIC.Bash</code> - Gives the agent permission to run commands in a bash shell.</p> </li> </ul> </li> </ul>"""
    parent_action_group_signature_params: NotRequired[
        "aws_sdk_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
    ]
    """<p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Anthropic Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html\">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>"""
    action_group_executor: NotRequired[
        "aws_sdk_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
    ]
    """<p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.</p>"""
    api_schema: NotRequired["aws_sdk_bedrock_agent.types.api_schema.APISchema"]
    """<p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html\">Action group OpenAPI schemas</a>.</p>"""
    action_group_state: NotRequired[
        "aws_sdk_bedrock_agent.types.action_group_state.ActionGroupState"
    ]
    """<p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html\">InvokeAgent</a> request.</p>"""
    function_schema: NotRequired[
        "aws_sdk_bedrock_agent.types.function_schema.FunctionSchema"
    ]
    """<p>Contains details about the function schema for the action group or the JSON or YAML-formatted payload defining the schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentActionGroupRequest) -> dict:
    out: dict = {}
    out["actionGroupName"] = value["action_group_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "parent_action_group_signature" in value:
        import aws_sdk_bedrock_agent.types.action_group_signature

        out["parentActionGroupSignature"] = (
            aws_sdk_bedrock_agent.types.action_group_signature.serialize_json(
                value["parent_action_group_signature"]
            )
        )
    if "parent_action_group_signature_params" in value:
        import aws_sdk_bedrock_agent.types.action_group_signature_params

        out["parentActionGroupSignatureParams"] = (
            aws_sdk_bedrock_agent.types.action_group_signature_params.serialize_json(
                value["parent_action_group_signature_params"]
            )
        )
    if "action_group_executor" in value:
        import aws_sdk_bedrock_agent.types.action_group_executor

        out["actionGroupExecutor"] = (
            aws_sdk_bedrock_agent.types.action_group_executor.serialize_json(
                value["action_group_executor"]
            )
        )
    if "api_schema" in value:
        import aws_sdk_bedrock_agent.types.api_schema

        out["apiSchema"] = aws_sdk_bedrock_agent.types.api_schema.serialize_json(
            value["api_schema"]
        )
    if "action_group_state" in value:
        import aws_sdk_bedrock_agent.types.action_group_state

        out["actionGroupState"] = (
            aws_sdk_bedrock_agent.types.action_group_state.serialize_json(
                value["action_group_state"]
            )
        )
    if "function_schema" in value:
        import aws_sdk_bedrock_agent.types.function_schema

        out["functionSchema"] = (
            aws_sdk_bedrock_agent.types.function_schema.serialize_json(
                value["function_schema"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAgentActionGroupRequest:
    out: CreateAgentActionGroupRequest = {}  # type: ignore[typeddict-item]
    if "actionGroupName" in data:
        out["action_group_name"] = data["actionGroupName"]
    else:
        raise DeserializationError(
            "CreateAgentActionGroupRequest.action_group_name required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "parentActionGroupSignature" in data:
        import aws_sdk_bedrock_agent.types.action_group_signature

        out["parent_action_group_signature"] = (
            aws_sdk_bedrock_agent.types.action_group_signature.deserialize_json(
                data["parentActionGroupSignature"]
            )
        )
    if "parentActionGroupSignatureParams" in data:
        import aws_sdk_bedrock_agent.types.action_group_signature_params

        out["parent_action_group_signature_params"] = (
            aws_sdk_bedrock_agent.types.action_group_signature_params.deserialize_json(
                data["parentActionGroupSignatureParams"]
            )
        )
    if "actionGroupExecutor" in data:
        import aws_sdk_bedrock_agent.types.action_group_executor

        out["action_group_executor"] = (
            aws_sdk_bedrock_agent.types.action_group_executor.deserialize_json(
                data["actionGroupExecutor"]
            )
        )
    if "apiSchema" in data:
        import aws_sdk_bedrock_agent.types.api_schema

        out["api_schema"] = aws_sdk_bedrock_agent.types.api_schema.deserialize_json(
            data["apiSchema"]
        )
    if "actionGroupState" in data:
        import aws_sdk_bedrock_agent.types.action_group_state

        out["action_group_state"] = (
            aws_sdk_bedrock_agent.types.action_group_state.deserialize_json(
                data["actionGroupState"]
            )
        )
    if "functionSchema" in data:
        import aws_sdk_bedrock_agent.types.function_schema

        out["function_schema"] = (
            aws_sdk_bedrock_agent.types.function_schema.deserialize_json(
                data["functionSchema"]
            )
        )
    return out
