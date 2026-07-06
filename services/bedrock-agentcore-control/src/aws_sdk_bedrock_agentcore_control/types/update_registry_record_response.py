"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateRegistryRecordResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description
    import aws_sdk_bedrock_agentcore_control.types.descriptor_type
    import aws_sdk_bedrock_agentcore_control.types.descriptors
    import aws_sdk_bedrock_agentcore_control.types.registry_arn
    import aws_sdk_bedrock_agentcore_control.types.registry_record_arn
    import aws_sdk_bedrock_agentcore_control.types.registry_record_id
    import aws_sdk_bedrock_agentcore_control.types.registry_record_name
    import aws_sdk_bedrock_agentcore_control.types.registry_record_status
    import aws_sdk_bedrock_agentcore_control.types.registry_record_version
    import aws_sdk_bedrock_agentcore_control.types.synchronization_configuration
    import aws_sdk_bedrock_agentcore_control.types.synchronization_type


class UpdateRegistryRecordResponse(TypedDict, closed=True):
    registry_arn: "aws_sdk_bedrock_agentcore_control.types.registry_arn.RegistryArn"
    """<p>The Amazon Resource Name (ARN) of the registry that contains the updated record.</p>"""
    record_arn: (
        "aws_sdk_bedrock_agentcore_control.types.registry_record_arn.RegistryRecordArn"
    )
    """<p>The Amazon Resource Name (ARN) of the updated registry record.</p>"""
    record_id: (
        "aws_sdk_bedrock_agentcore_control.types.registry_record_id.RegistryRecordId"
    )
    """<p>The unique identifier of the updated registry record.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
    """<p>The name of the updated registry record.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the updated registry record.</p>"""
    descriptor_type: (
        "aws_sdk_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
    )
    """<p>The descriptor type of the updated registry record. Possible values are <code>MCP</code>, <code>A2A</code>, <code>CUSTOM</code>, and <code>AGENT_SKILLS</code>.</p>"""
    descriptors: "aws_sdk_bedrock_agentcore_control.types.descriptors.Descriptors"
    """<p>The descriptor-type-specific configuration of the updated registry record. For details, see the <code>Descriptors</code> data type.</p>"""
    record_version: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
    ]
    """<p>The version of the updated registry record.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus"
    """<p>The current status of the updated registry record. Possible values include <code>CREATING</code>, <code>DRAFT</code>, <code>APPROVED</code>, <code>PENDING_APPROVAL</code>, <code>REJECTED</code>, <code>DEPRECATED</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, and <code>UPDATE_FAILED</code>.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry record was created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry record was last updated.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the updated registry record.</p>"""
    synchronization_type: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.synchronization_type.SynchronizationType"
    ]
    """<p>The synchronization type of the updated registry record.</p>"""
    synchronization_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.synchronization_configuration.SynchronizationConfiguration"
    ]
    """<p>The synchronization configuration of the updated registry record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryRecordResponse) -> dict:
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
    import aws_sdk_bedrock_agentcore_control.types.descriptors

    out["descriptors"] = (
        aws_sdk_bedrock_agentcore_control.types.descriptors.serialize_json(
            value["descriptors"]
        )
    )
    if "record_version" in value:
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
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "synchronization_type" in value:
        import aws_sdk_bedrock_agentcore_control.types.synchronization_type

        out["synchronizationType"] = (
            aws_sdk_bedrock_agentcore_control.types.synchronization_type.serialize_json(
                value["synchronization_type"]
            )
        )
    if "synchronization_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.synchronization_configuration

        out["synchronizationConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.synchronization_configuration.serialize_json(
                value["synchronization_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRegistryRecordResponse:
    out: UpdateRegistryRecordResponse = {}  # type: ignore[typeddict-item]
    if "registryArn" in data:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.registry_arn required")
    if "recordArn" in data:
        out["record_arn"] = data["recordArn"]
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.record_arn required")
    if "recordId" in data:
        out["record_id"] = data["recordId"]
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.record_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.name required")
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
        raise DeserializationError(
            "UpdateRegistryRecordResponse.descriptor_type required"
        )
    if "descriptors" in data:
        import aws_sdk_bedrock_agentcore_control.types.descriptors

        out["descriptors"] = (
            aws_sdk_bedrock_agentcore_control.types.descriptors.deserialize_json(
                data["descriptors"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.descriptors required")
    if "recordVersion" in data:
        out["record_version"] = data["recordVersion"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.updated_at required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "synchronizationType" in data:
        import aws_sdk_bedrock_agentcore_control.types.synchronization_type

        out["synchronization_type"] = (
            aws_sdk_bedrock_agentcore_control.types.synchronization_type.deserialize_json(
                data["synchronizationType"]
            )
        )
    if "synchronizationConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.synchronization_configuration

        out["synchronization_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.synchronization_configuration.deserialize_json(
                data["synchronizationConfiguration"]
            )
        )
    return out
