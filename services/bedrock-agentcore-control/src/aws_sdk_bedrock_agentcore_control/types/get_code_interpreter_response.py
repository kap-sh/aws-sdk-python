"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetCodeInterpreterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.certificates
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_arn
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_id
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_network_configuration
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_status
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.sandbox_name


class GetCodeInterpreterResponse(TypedDict):
    code_interpreter_id: (
        "aws_sdk_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId"
    )
    """<p>The unique identifier of the code interpreter.</p>"""
    code_interpreter_arn: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_arn.CodeInterpreterArn"
    """<p>The Amazon Resource Name (ARN) of the code interpreter.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.sandbox_name.SandboxName"
    """<p>The name of the code interpreter.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the code interpreter.</p>"""
    execution_role_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    ]
    """<p>The IAM role ARN that provides permissions for the code interpreter.</p>"""
    network_configuration: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_network_configuration.CodeInterpreterNetworkConfiguration"
    status: "aws_sdk_bedrock_agentcore_control.types.code_interpreter_status.CodeInterpreterStatus"
    """<p>The current status of the code interpreter.</p>"""
    certificates: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.certificates.Certificates"
    ]
    """<p>The list of certificates configured for the code interpreter.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the code interpreter is in a failed state.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the code interpreter was created.</p>"""
    last_updated_at: (
        "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp when the code interpreter was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeInterpreterResponse) -> dict:
    out: dict = {}
    out["codeInterpreterId"] = value["code_interpreter_id"]
    out["codeInterpreterArn"] = value["code_interpreter_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_network_configuration

    out["networkConfiguration"] = (
        aws_sdk_bedrock_agentcore_control.types.code_interpreter_network_configuration.serialize_json(
            value["network_configuration"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.code_interpreter_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.code_interpreter_status.serialize_json(
            value["status"]
        )
    )
    if "certificates" in value:
        import aws_sdk_bedrock_agentcore_control.types.certificates

        out["certificates"] = (
            aws_sdk_bedrock_agentcore_control.types.certificates.serialize_json(
                value["certificates"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetCodeInterpreterResponse:
    out: GetCodeInterpreterResponse = {}  # type: ignore[typeddict-item]
    if "codeInterpreterId" in data:
        out["code_interpreter_id"] = data["codeInterpreterId"]
    else:
        raise DeserializationError(
            "GetCodeInterpreterResponse.code_interpreter_id required"
        )
    if "codeInterpreterArn" in data:
        out["code_interpreter_arn"] = data["codeInterpreterArn"]
    else:
        raise DeserializationError(
            "GetCodeInterpreterResponse.code_interpreter_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetCodeInterpreterResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "networkConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.code_interpreter_network_configuration

        out["network_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.code_interpreter_network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetCodeInterpreterResponse.network_configuration required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.code_interpreter_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.code_interpreter_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetCodeInterpreterResponse.status required")
    if "certificates" in data:
        import aws_sdk_bedrock_agentcore_control.types.certificates

        out["certificates"] = (
            aws_sdk_bedrock_agentcore_control.types.certificates.deserialize_json(
                data["certificates"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetCodeInterpreterResponse.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetCodeInterpreterResponse.last_updated_at required"
        )
    return out
