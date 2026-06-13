"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMapperSegment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.checksum
    import aws_sdk_mgn.types.logical_id
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.network_migration_job_id
    import aws_sdk_mgn.types.network_migration_mapper_segment_type
    import aws_sdk_mgn.types.referenced_segments_list
    import aws_sdk_mgn.types.s3_configuration
    import aws_sdk_mgn.types.scope_tags_map
    import aws_sdk_mgn.types.segment_description
    import aws_sdk_mgn.types.segment_id
    import aws_sdk_mgn.types.segment_name


class NetworkMigrationMapperSegment(TypedDict):
    job_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_job_id.NetworkMigrationJobID"
    ]
    """<p>The unique identifier of the job that created this segment.</p>"""
    network_migration_execution_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    ]
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition.</p>"""
    segment_id: NotRequired["aws_sdk_mgn.types.segment_id.SegmentID"]
    """<p>The unique identifier of the segment.</p>"""
    segment_type: NotRequired[
        "aws_sdk_mgn.types.network_migration_mapper_segment_type.NetworkMigrationMapperSegmentType"
    ]
    """<p>The type of the segment, such as VPC, subnet, or security group.</p>"""
    name: NotRequired["aws_sdk_mgn.types.segment_name.SegmentName"]
    """<p>The name of the segment.</p>"""
    description: NotRequired["aws_sdk_mgn.types.segment_description.SegmentDescription"]
    """<p>A description of the segment.</p>"""
    logical_id: NotRequired["aws_sdk_mgn.types.logical_id.LogicalID"]
    """<p>The logical identifier for the segment in the infrastructure code.</p>"""
    checksum: NotRequired["aws_sdk_mgn.types.checksum.Checksum"]
    """<p>The checksum of the segment data for integrity verification.</p>"""
    output_s3_configuration: NotRequired[
        "aws_sdk_mgn.types.s3_configuration.S3Configuration"
    ]
    """<p>The S3 location where segment artifacts are stored.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the segment was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the segment was last updated.</p>"""
    scope_tags: NotRequired["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>Scope tags for the segment.</p>"""
    target_account: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>The target AWS account where this segment will be deployed.</p>"""
    referenced_segments: NotRequired[
        "aws_sdk_mgn.types.referenced_segments_list.referencedSegmentsList"
    ]
    """<p>A list of other segments that this segment depends on or references.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMapperSegment) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "network_migration_execution_id" in value:
        out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "segment_id" in value:
        out["segmentID"] = value["segment_id"]
    if "segment_type" in value:
        out["segmentType"] = value["segment_type"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "logical_id" in value:
        out["logicalID"] = value["logical_id"]
    if "checksum" in value:
        import aws_sdk_mgn.types.checksum

        out["checksum"] = aws_sdk_mgn.types.checksum.serialize_json(value["checksum"])
    if "output_s3_configuration" in value:
        import aws_sdk_mgn.types.s3_configuration

        out["outputS3Configuration"] = (
            aws_sdk_mgn.types.s3_configuration.serialize_json(
                value["output_s3_configuration"]
            )
        )
    if "created_at" in value:
        import aws_sdk_mgn.types._prelude.timestamp

        out["createdAt"] = aws_sdk_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_mgn.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_mgn.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "scope_tags" in value:
        import aws_sdk_mgn.types.scope_tags_map

        out["scopeTags"] = aws_sdk_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    if "target_account" in value:
        out["targetAccount"] = value["target_account"]
    if "referenced_segments" in value:
        import aws_sdk_mgn.types.referenced_segments_list

        out["referencedSegments"] = (
            aws_sdk_mgn.types.referenced_segments_list.serialize_json(
                value["referenced_segments"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationMapperSegment:
    out: NetworkMigrationMapperSegment = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if "segmentID" in data:
        out["segment_id"] = data["segmentID"]
    if "segmentType" in data:
        out["segment_type"] = data["segmentType"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "logicalID" in data:
        out["logical_id"] = data["logicalID"]
    if "checksum" in data:
        import aws_sdk_mgn.types.checksum

        out["checksum"] = aws_sdk_mgn.types.checksum.deserialize_json(data["checksum"])
    if "outputS3Configuration" in data:
        import aws_sdk_mgn.types.s3_configuration

        out["output_s3_configuration"] = (
            aws_sdk_mgn.types.s3_configuration.deserialize_json(
                data["outputS3Configuration"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_mgn.types._prelude.timestamp

        out["created_at"] = aws_sdk_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_mgn.types._prelude.timestamp

        out["updated_at"] = aws_sdk_mgn.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "scopeTags" in data:
        import aws_sdk_mgn.types.scope_tags_map

        out["scope_tags"] = aws_sdk_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    if "targetAccount" in data:
        out["target_account"] = data["targetAccount"]
    if "referencedSegments" in data:
        import aws_sdk_mgn.types.referenced_segments_list

        out["referenced_segments"] = (
            aws_sdk_mgn.types.referenced_segments_list.deserialize_json(
                data["referencedSegments"]
            )
        )
    return out
