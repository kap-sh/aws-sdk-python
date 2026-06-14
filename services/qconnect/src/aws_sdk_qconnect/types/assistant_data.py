"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_agent_configuration_map
    import aws_sdk_qconnect.types.arn
    import aws_sdk_qconnect.types.assistant_capability_configuration
    import aws_sdk_qconnect.types.assistant_integration_configuration
    import aws_sdk_qconnect.types.assistant_status
    import aws_sdk_qconnect.types.assistant_type
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.orchestrator_configuration_list
    import aws_sdk_qconnect.types.server_side_encryption_configuration
    import aws_sdk_qconnect.types.tags
    import aws_sdk_qconnect.types.uuid


class AssistantData(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    assistant_arn: "aws_sdk_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    name: "aws_sdk_qconnect.types.name.Name"
    """<p>The name.</p>"""
    type: "aws_sdk_qconnect.types.assistant_type.AssistantType"
    """<p>The type of assistant.</p>"""
    status: "aws_sdk_qconnect.types.assistant_status.AssistantStatus"
    """<p>The status of the assistant.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description.</p>"""
    tags: NotRequired["aws_sdk_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    server_side_encryption_configuration: NotRequired[
        "aws_sdk_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    ]
    r"""<p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect. To use Amazon Q in Connect with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html\">Enable Amazon Q in Connect for your instance</a>.</p>"""
    integration_configuration: NotRequired[
        "aws_sdk_qconnect.types.assistant_integration_configuration.AssistantIntegrationConfiguration"
    ]
    """<p>The configuration information for the Amazon Q in Connect assistant integration.</p>"""
    capability_configuration: NotRequired[
        "aws_sdk_qconnect.types.assistant_capability_configuration.AssistantCapabilityConfiguration"
    ]
    """<p>The configuration information for the Amazon Q in Connect assistant capability. </p>"""
    ai_agent_configuration: NotRequired[
        "aws_sdk_qconnect.types.ai_agent_configuration_map.AIAgentConfigurationMap"
    ]
    """<p>The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that is set on the Amazon Q in Connect Assistant.</p>"""
    orchestrator_configuration_list: NotRequired[
        "aws_sdk_qconnect.types.orchestrator_configuration_list.OrchestratorConfigurationList"
    ]
    """<p>The list of orchestrator configurations for the assistant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantData) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["status"] = value["status"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.serialize_json(value["tags"])
    if "server_side_encryption_configuration" in value:
        import aws_sdk_qconnect.types.server_side_encryption_configuration

        out["serverSideEncryptionConfiguration"] = (
            aws_sdk_qconnect.types.server_side_encryption_configuration.serialize_json(
                value["server_side_encryption_configuration"]
            )
        )
    if "integration_configuration" in value:
        import aws_sdk_qconnect.types.assistant_integration_configuration

        out["integrationConfiguration"] = (
            aws_sdk_qconnect.types.assistant_integration_configuration.serialize_json(
                value["integration_configuration"]
            )
        )
    if "capability_configuration" in value:
        import aws_sdk_qconnect.types.assistant_capability_configuration

        out["capabilityConfiguration"] = (
            aws_sdk_qconnect.types.assistant_capability_configuration.serialize_json(
                value["capability_configuration"]
            )
        )
    if "ai_agent_configuration" in value:
        import aws_sdk_qconnect.types.ai_agent_configuration_map

        out["aiAgentConfiguration"] = (
            aws_sdk_qconnect.types.ai_agent_configuration_map.serialize_json(
                value["ai_agent_configuration"]
            )
        )
    if "orchestrator_configuration_list" in value:
        import aws_sdk_qconnect.types.orchestrator_configuration_list

        out["orchestratorConfigurationList"] = (
            aws_sdk_qconnect.types.orchestrator_configuration_list.serialize_json(
                value["orchestrator_configuration_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssistantData:
    out: AssistantData = {}  # type: ignore[typeddict-item]
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("AssistantData.assistant_id required")
    if "assistantArn" in data:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("AssistantData.assistant_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssistantData.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("AssistantData.type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("AssistantData.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_qconnect.types.tags

        out["tags"] = aws_sdk_qconnect.types.tags.deserialize_json(data["tags"])
    if "serverSideEncryptionConfiguration" in data:
        import aws_sdk_qconnect.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            aws_sdk_qconnect.types.server_side_encryption_configuration.deserialize_json(
                data["serverSideEncryptionConfiguration"]
            )
        )
    if "integrationConfiguration" in data:
        import aws_sdk_qconnect.types.assistant_integration_configuration

        out["integration_configuration"] = (
            aws_sdk_qconnect.types.assistant_integration_configuration.deserialize_json(
                data["integrationConfiguration"]
            )
        )
    if "capabilityConfiguration" in data:
        import aws_sdk_qconnect.types.assistant_capability_configuration

        out["capability_configuration"] = (
            aws_sdk_qconnect.types.assistant_capability_configuration.deserialize_json(
                data["capabilityConfiguration"]
            )
        )
    if "aiAgentConfiguration" in data:
        import aws_sdk_qconnect.types.ai_agent_configuration_map

        out["ai_agent_configuration"] = (
            aws_sdk_qconnect.types.ai_agent_configuration_map.deserialize_json(
                data["aiAgentConfiguration"]
            )
        )
    if "orchestratorConfigurationList" in data:
        import aws_sdk_qconnect.types.orchestrator_configuration_list

        out["orchestrator_configuration_list"] = (
            aws_sdk_qconnect.types.orchestrator_configuration_list.deserialize_json(
                data["orchestratorConfigurationList"]
            )
        )
    return out
