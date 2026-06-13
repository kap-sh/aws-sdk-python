"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationCodeGenerationSegment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mgn.types.logical_id
    import aws_sdk_mgn.types.network_migration_code_generation_artifacts
    import aws_sdk_mgn.types.network_migration_code_generation_segment_type
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.network_migration_job_id
    import aws_sdk_mgn.types.referenced_segments_list
    import aws_sdk_mgn.types.segment_id


class NetworkMigrationCodeGenerationSegment(TypedDict):
    job_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_job_id.NetworkMigrationJobID"
    ]
    """<p>The unique identifier of the code generation job.</p>"""
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
        "aws_sdk_mgn.types.network_migration_code_generation_segment_type.NetworkMigrationCodeGenerationSegmentType"
    ]
    """<p>The type of the segment.</p>"""
    logical_id: NotRequired["aws_sdk_mgn.types.logical_id.LogicalID"]
    """<p>The logical identifier for the segment.</p>"""
    mapper_segment_id: NotRequired["aws_sdk_mgn.types.segment_id.SegmentID"]
    """<p>The ID of the mapper segment that this code generation segment was created from.</p>"""
    artifacts: NotRequired[
        "aws_sdk_mgn.types.network_migration_code_generation_artifacts.NetworkMigrationCodeGenerationArtifacts"
    ]
    """<p>A list of artifacts generated for this segment.</p>"""
    referenced_segments: NotRequired[
        "aws_sdk_mgn.types.referenced_segments_list.referencedSegmentsList"
    ]
    """<p>A list of other segments that this segment depends on or references.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the segment was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationCodeGenerationSegment) -> dict:
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
    if "logical_id" in value:
        out["logicalID"] = value["logical_id"]
    if "mapper_segment_id" in value:
        out["mapperSegmentID"] = value["mapper_segment_id"]
    if "artifacts" in value:
        import aws_sdk_mgn.types.network_migration_code_generation_artifacts

        out["artifacts"] = (
            aws_sdk_mgn.types.network_migration_code_generation_artifacts.serialize_json(
                value["artifacts"]
            )
        )
    if "referenced_segments" in value:
        import aws_sdk_mgn.types.referenced_segments_list

        out["referencedSegments"] = (
            aws_sdk_mgn.types.referenced_segments_list.serialize_json(
                value["referenced_segments"]
            )
        )
    if "created_at" in value:
        import aws_sdk_mgn.types._prelude.timestamp

        out["createdAt"] = aws_sdk_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationCodeGenerationSegment:
    out: NetworkMigrationCodeGenerationSegment = {}  # type: ignore[typeddict-item]
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
    if "logicalID" in data:
        out["logical_id"] = data["logicalID"]
    if "mapperSegmentID" in data:
        out["mapper_segment_id"] = data["mapperSegmentID"]
    if "artifacts" in data:
        import aws_sdk_mgn.types.network_migration_code_generation_artifacts

        out["artifacts"] = (
            aws_sdk_mgn.types.network_migration_code_generation_artifacts.deserialize_json(
                data["artifacts"]
            )
        )
    if "referencedSegments" in data:
        import aws_sdk_mgn.types.referenced_segments_list

        out["referenced_segments"] = (
            aws_sdk_mgn.types.referenced_segments_list.deserialize_json(
                data["referencedSegments"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_mgn.types._prelude.timestamp

        out["created_at"] = aws_sdk_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    return out
