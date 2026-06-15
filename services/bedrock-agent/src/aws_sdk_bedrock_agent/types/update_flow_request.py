"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_definition
    import aws_sdk_bedrock_agent.types.flow_description
    import aws_sdk_bedrock_agent.types.flow_execution_role_arn
    import aws_sdk_bedrock_agent.types.flow_identifier
    import aws_sdk_bedrock_agent.types.flow_name
    import aws_sdk_bedrock_agent.types.kms_key_arn


class UpdateFlowRequest(TypedDict):
    name: "aws_sdk_bedrock_agent.types.flow_name.FlowName"
    """<p>A name for the flow.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_description.FlowDescription"
    ]
    """<p>A description for the flow.</p>"""
    execution_role_arn: (
        "aws_sdk_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn"
    )
    r"""<p>The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html\">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>"""
    customer_encryption_key_arn: NotRequired[
        "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.</p>"""
    definition: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_definition.FlowDefinition"
    ]
    """<p>A definition of the nodes and the connections between the nodes in the flow.</p>"""
    flow_identifier: "aws_sdk_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    if "definition" in value:
        import aws_sdk_bedrock_agent.types.flow_definition

        out["definition"] = aws_sdk_bedrock_agent.types.flow_definition.serialize_json(
            value["definition"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowRequest:
    out: UpdateFlowRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateFlowRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("UpdateFlowRequest.execution_role_arn required")
    if "customerEncryptionKeyArn" in data:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if "definition" in data:
        import aws_sdk_bedrock_agent.types.flow_definition

        out["definition"] = (
            aws_sdk_bedrock_agent.types.flow_definition.deserialize_json(
                data["definition"]
            )
        )
    return out
