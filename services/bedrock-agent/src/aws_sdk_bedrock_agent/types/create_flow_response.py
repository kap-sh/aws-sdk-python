"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateFlowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.draft_version
    import aws_sdk_bedrock_agent.types.flow_arn
    import aws_sdk_bedrock_agent.types.flow_definition
    import aws_sdk_bedrock_agent.types.flow_description
    import aws_sdk_bedrock_agent.types.flow_execution_role_arn
    import aws_sdk_bedrock_agent.types.flow_id
    import aws_sdk_bedrock_agent.types.flow_name
    import aws_sdk_bedrock_agent.types.flow_status
    import aws_sdk_bedrock_agent.types.kms_key_arn


class CreateFlowResponse(TypedDict):
    name: "aws_sdk_bedrock_agent.types.flow_name.FlowName"
    """<p>The name of the flow.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_description.FlowDescription"
    ]
    """<p>The description of the flow.</p>"""
    execution_role_arn: (
        "aws_sdk_bedrock_agent.types.flow_execution_role_arn.FlowExecutionRoleArn"
    )
    r"""<p>The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html\">Create a service role for flows in Amazon Bedrock</a> in the Amazon Bedrock User Guide.</p>"""
    customer_encryption_key_arn: NotRequired[
        "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key that you encrypted the flow with.</p>"""
    id: "aws_sdk_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    arn: "aws_sdk_bedrock_agent.types.flow_arn.FlowArn"
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    status: "aws_sdk_bedrock_agent.types.flow_status.FlowStatus"
    """<p>The status of the flow. When you submit this request, the status will be <code>NotPrepared</code>. If creation fails, the status becomes <code>Failed</code>.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the flow was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the flow was last updated.</p>"""
    version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the flow. When you create a flow, the version created is the <code>DRAFT</code> version.</p>"""
    definition: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_definition.FlowDefinition"
    ]
    """<p>A definition of the nodes and connections between nodes in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_bedrock_agent.types.flow_status

    out["status"] = aws_sdk_bedrock_agent.types.flow_status.serialize_json(
        value["status"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    out["version"] = value["version"]
    if "definition" in value:
        import aws_sdk_bedrock_agent.types.flow_definition

        out["definition"] = aws_sdk_bedrock_agent.types.flow_definition.serialize_json(
            value["definition"]
        )
    return out


def deserialize_json(data: dict) -> CreateFlowResponse:
    out: CreateFlowResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFlowResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("CreateFlowResponse.execution_role_arn required")
    if "customerEncryptionKeyArn" in data:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateFlowResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateFlowResponse.arn required")
    if "status" in data:
        import aws_sdk_bedrock_agent.types.flow_status

        out["status"] = aws_sdk_bedrock_agent.types.flow_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateFlowResponse.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateFlowResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("CreateFlowResponse.updated_at required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreateFlowResponse.version required")
    if "definition" in data:
        import aws_sdk_bedrock_agent.types.flow_definition

        out["definition"] = (
            aws_sdk_bedrock_agent.types.flow_definition.deserialize_json(
                data["definition"]
            )
        )
    return out
