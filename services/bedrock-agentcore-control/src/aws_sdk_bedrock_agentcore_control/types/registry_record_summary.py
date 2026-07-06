"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.descriptor_type
    import aws_sdk_bedrock_agentcore_control.types.registry_arn
    import aws_sdk_bedrock_agentcore_control.types.registry_record_arn
    import aws_sdk_bedrock_agentcore_control.types.registry_record_id
    import aws_sdk_bedrock_agentcore_control.types.registry_record_name
    import aws_sdk_bedrock_agentcore_control.types.registry_record_status
    import aws_sdk_bedrock_agentcore_control.types.registry_record_version


class RegistryRecordSummary(TypedDict, closed=True):
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
    name: "aws_sdk_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
    """<p>The name of the registry record.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the registry record.</p>"""
    descriptor_type: (
        "aws_sdk_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
    )
    """<p>The descriptor type of the registry record. Possible values are <code>MCP</code>, <code>A2A</code>, <code>CUSTOM</code>, and <code>AGENT_SKILLS</code>.</p>"""
    record_version: "aws_sdk_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
    """<p>The version of the registry record.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus"
    """<p>The current status of the registry record. Possible values include <code>CREATING</code>, <code>DRAFT</code>, <code>APPROVED</code>, <code>PENDING_APPROVAL</code>, <code>REJECTED</code>, <code>DEPRECATED</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, and <code>UPDATE_FAILED</code>.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry record was created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry record was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordSummary) -> dict:
    out: dict = {}
    out["registryArn"] = value["registry_arn"]
    out["recordArn"] = value["record_arn"]
    out["recordId"] = value["record_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.descriptor_type

    out["descriptorType"] = (
        aws_sdk_bedrock_agentcore_control.types.descriptor_type.serialize_json(
            value["descriptor_type"]
        )
    )
    out["recordVersion"] = value["record_version"]
    import aws_sdk_bedrock_agentcore_control.types.registry_record_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.registry_record_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegistryRecordSummary:
    out: RegistryRecordSummary = {}  # type: ignore[typeddict-item]
    if "registryArn" in data:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError("RegistryRecordSummary.registry_arn required")
    if "recordArn" in data:
        out["record_arn"] = data["recordArn"]
    else:
        raise DeserializationError("RegistryRecordSummary.record_arn required")
    if "recordId" in data:
        out["record_id"] = data["recordId"]
    else:
        raise DeserializationError("RegistryRecordSummary.record_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegistryRecordSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "descriptorType" in data:
        import aws_sdk_bedrock_agentcore_control.types.descriptor_type

        out["descriptor_type"] = (
            aws_sdk_bedrock_agentcore_control.types.descriptor_type.deserialize_json(
                data["descriptorType"]
            )
        )
    else:
        raise DeserializationError("RegistryRecordSummary.descriptor_type required")
    if "recordVersion" in data:
        out["record_version"] = data["recordVersion"]
    else:
        raise DeserializationError("RegistryRecordSummary.record_version required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("RegistryRecordSummary.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("RegistryRecordSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("RegistryRecordSummary.updated_at required")
    return out
