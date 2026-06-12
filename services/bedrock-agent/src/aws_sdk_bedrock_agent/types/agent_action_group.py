"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentActionGroup``."""

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
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.function_schema
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.version


class AgentActionGroup(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent to which the action group belongs.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.version.Version"
    """<p>The version of the agent to which the action group belongs.</p>"""
    action_group_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the action group.</p>"""
    action_group_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the action group.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the action group.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the action group was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the action group was last updated.</p>"""
    parent_action_signature: NotRequired[
        "aws_sdk_bedrock_agent.types.action_group_signature.ActionGroupSignature"
    ]
    """<p>If this field is set as <code>AMAZON.UserInput</code>, the agent can request the user for additional information when trying to complete a task. The <code>description</code>, <code>apiSchema</code>, and <code>actionGroupExecutor</code> fields must be blank for this action group.</p> <p>During orchestration, if the agent determines that it needs to invoke an API in an action group, but doesn't have enough information to complete the API request, it will invoke this action group instead and return an <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Observation.html\">Observation</a> reprompting the user for more information.</p>"""
    parent_action_group_signature_params: NotRequired[
        "aws_sdk_bedrock_agent.types.action_group_signature_params.ActionGroupSignatureParams"
    ]
    """<p>The configuration settings for a computer use action.</p> <important> <p> Computer use is a new Anthropic Claude model capability (in beta) available with Claude 3.7 Sonnet and Claude 3.5 Sonnet v2 only. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html\">Configure an Amazon Bedrock Agent to complete tasks with computer use tools</a>. </p> </important>"""
    action_group_executor: NotRequired[
        "aws_sdk_bedrock_agent.types.action_group_executor.ActionGroupExecutor"
    ]
    """<p>The Amazon Resource Name (ARN) of the Lambda function containing the business logic that is carried out upon invoking the action or the custom control method for handling the information elicited from the user.</p>"""
    api_schema: NotRequired["aws_sdk_bedrock_agent.types.api_schema.APISchema"]
    """<p>Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html\">Action group OpenAPI schemas</a>.</p>"""
    function_schema: NotRequired[
        "aws_sdk_bedrock_agent.types.function_schema.FunctionSchema"
    ]
    """<p>Defines functions that each define parameters that the agent needs to invoke from the user. Each function represents an action in an action group.</p>"""
    action_group_state: (
        "aws_sdk_bedrock_agent.types.action_group_state.ActionGroupState"
    )
    """<p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html\">InvokeAgent</a> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentActionGroup) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentVersion"] = value["agent_version"]
    out["actionGroupId"] = value["action_group_id"]
    out["actionGroupName"] = value["action_group_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "parent_action_signature" in value:
        import aws_sdk_bedrock_agent.types.action_group_signature

        out["parentActionSignature"] = (
            aws_sdk_bedrock_agent.types.action_group_signature.serialize_json(
                value["parent_action_signature"]
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
    if "function_schema" in value:
        import aws_sdk_bedrock_agent.types.function_schema

        out["functionSchema"] = (
            aws_sdk_bedrock_agent.types.function_schema.serialize_json(
                value["function_schema"]
            )
        )
    import aws_sdk_bedrock_agent.types.action_group_state

    out["actionGroupState"] = (
        aws_sdk_bedrock_agent.types.action_group_state.serialize_json(
            value["action_group_state"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgentActionGroup:
    out: AgentActionGroup = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AgentActionGroup.agent_id required")
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("AgentActionGroup.agent_version required")
    if "actionGroupId" in data:
        out["action_group_id"] = data["actionGroupId"]
    else:
        raise DeserializationError("AgentActionGroup.action_group_id required")
    if "actionGroupName" in data:
        out["action_group_name"] = data["actionGroupName"]
    else:
        raise DeserializationError("AgentActionGroup.action_group_name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AgentActionGroup.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AgentActionGroup.updated_at required")
    if "parentActionSignature" in data:
        import aws_sdk_bedrock_agent.types.action_group_signature

        out["parent_action_signature"] = (
            aws_sdk_bedrock_agent.types.action_group_signature.deserialize_json(
                data["parentActionSignature"]
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
    if "functionSchema" in data:
        import aws_sdk_bedrock_agent.types.function_schema

        out["function_schema"] = (
            aws_sdk_bedrock_agent.types.function_schema.deserialize_json(
                data["functionSchema"]
            )
        )
    if "actionGroupState" in data:
        import aws_sdk_bedrock_agent.types.action_group_state

        out["action_group_state"] = (
            aws_sdk_bedrock_agent.types.action_group_state.deserialize_json(
                data["actionGroupState"]
            )
        )
    else:
        raise DeserializationError("AgentActionGroup.action_group_state required")
    return out
