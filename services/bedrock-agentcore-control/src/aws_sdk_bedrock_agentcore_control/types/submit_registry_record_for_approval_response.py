"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SubmitRegistryRecordForApprovalResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.registry_arn
    import aws_sdk_bedrock_agentcore_control.types.registry_record_arn
    import aws_sdk_bedrock_agentcore_control.types.registry_record_id
    import aws_sdk_bedrock_agentcore_control.types.registry_record_status


class SubmitRegistryRecordForApprovalResponse(TypedDict):
    registry_arn: "aws_sdk_bedrock_agentcore_control.types.registry_arn.RegistryArn"
    """<p>The Amazon Resource Name (ARN) of the registry that contains the record.</p>"""
    record_arn: (
        "aws_sdk_bedrock_agentcore_control.types.registry_record_arn.RegistryRecordArn"
    )
    """<p>The Amazon Resource Name (ARN) of the registry record.</p>"""
    record_id: (
        "aws_sdk_bedrock_agentcore_control.types.registry_record_id.RegistryRecordId"
    )
    """<p>The unique identifier of the registry record.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus"
    """<p>The resulting status of the registry record after submission.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the record was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmitRegistryRecordForApprovalResponse) -> dict:
    out: dict = {}
    out["registryArn"] = value["registry_arn"]
    out["recordArn"] = value["record_arn"]
    out["recordId"] = value["record_id"]
    import aws_sdk_bedrock_agentcore_control.types.registry_record_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.registry_record_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> SubmitRegistryRecordForApprovalResponse:
    out: SubmitRegistryRecordForApprovalResponse = {}  # type: ignore[typeddict-item]
    if "registryArn" in data:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError(
            "SubmitRegistryRecordForApprovalResponse.registry_arn required"
        )
    if "recordArn" in data:
        out["record_arn"] = data["recordArn"]
    else:
        raise DeserializationError(
            "SubmitRegistryRecordForApprovalResponse.record_arn required"
        )
    if "recordId" in data:
        out["record_id"] = data["recordId"]
    else:
        raise DeserializationError(
            "SubmitRegistryRecordForApprovalResponse.record_id required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "SubmitRegistryRecordForApprovalResponse.status required"
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "SubmitRegistryRecordForApprovalResponse.updated_at required"
        )
    return out
