"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetExecutionFlowSnapshotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_role_arn
    import aws_sdk_bedrock_agent_runtime.types.flow_identifier
    import aws_sdk_bedrock_agent_runtime.types.kms_key_arn
    import aws_sdk_bedrock_agent_runtime.types.version


class GetExecutionFlowSnapshotResponse(TypedDict):
    flow_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier"
    )
    """<p>The unique identifier of the flow.</p>"""
    flow_alias_identifier: (
        "aws_sdk_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the flow alias used for the flow execution.</p>"""
    flow_version: "aws_sdk_bedrock_agent_runtime.types.version.Version"
    """<p>The version of the flow used for the flow execution.</p>"""
    execution_role_arn: "aws_sdk_bedrock_agent_runtime.types.flow_execution_role_arn.FlowExecutionRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM service role that's used by the flow execution.</p>"""
    definition: "str"
    """<p>The flow definition used for the flow execution, including the nodes, connections, and configuration at the time when the execution started.</p> <p>The definition returns as a string that follows the structure of a <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_FlowDefinition.html\">FlowDefinition</a> object.</p>"""
    customer_encryption_key_arn: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the customer managed KMS key that's used to encrypt the flow snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExecutionFlowSnapshotResponse) -> dict:
    out: dict = {}
    out["flowIdentifier"] = value["flow_identifier"]
    out["flowAliasIdentifier"] = value["flow_alias_identifier"]
    out["flowVersion"] = value["flow_version"]
    out["executionRoleArn"] = value["execution_role_arn"]
    out["definition"] = value["definition"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> GetExecutionFlowSnapshotResponse:
    out: GetExecutionFlowSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "flowIdentifier" in data:
        out["flow_identifier"] = data["flowIdentifier"]
    else:
        raise DeserializationError(
            "GetExecutionFlowSnapshotResponse.flow_identifier required"
        )
    if "flowAliasIdentifier" in data:
        out["flow_alias_identifier"] = data["flowAliasIdentifier"]
    else:
        raise DeserializationError(
            "GetExecutionFlowSnapshotResponse.flow_alias_identifier required"
        )
    if "flowVersion" in data:
        out["flow_version"] = data["flowVersion"]
    else:
        raise DeserializationError(
            "GetExecutionFlowSnapshotResponse.flow_version required"
        )
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError(
            "GetExecutionFlowSnapshotResponse.execution_role_arn required"
        )
    if "definition" in data:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError(
            "GetExecutionFlowSnapshotResponse.definition required"
        )
    if "customerEncryptionKeyArn" in data:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    return out
