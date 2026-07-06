"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMappingUpdateJobDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mgn.types.large_bounded_string
    import aws_sdk_mgn.types.network_migration_definition_id
    import aws_sdk_mgn.types.network_migration_execution_id
    import aws_sdk_mgn.types.network_migration_job_id
    import aws_sdk_mgn.types.network_migration_job_status


class NetworkMigrationMappingUpdateJobDetails(TypedDict, closed=True):
    job_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_job_id.NetworkMigrationJobID"
    ]
    """<p>The unique identifier of the mapping update job.</p>"""
    network_migration_execution_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    ]
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: NotRequired[
        "aws_sdk_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the job was created.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the job completed or failed.</p>"""
    status: NotRequired[
        "aws_sdk_mgn.types.network_migration_job_status.NetworkMigrationJobStatus"
    ]
    """<p>The current status of the mapping update job.</p>"""
    status_details: NotRequired[
        "aws_sdk_mgn.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>Detailed status information about the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMappingUpdateJobDetails) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "network_migration_execution_id" in value:
        out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "created_at" in value:
        import aws_sdk_mgn.types._prelude.timestamp

        out["createdAt"] = aws_sdk_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "ended_at" in value:
        import aws_sdk_mgn.types._prelude.timestamp

        out["endedAt"] = aws_sdk_mgn.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "status_details" in value:
        out["statusDetails"] = value["status_details"]
    return out


def deserialize_json(data: dict) -> NetworkMigrationMappingUpdateJobDetails:
    out: NetworkMigrationMappingUpdateJobDetails = {}  # type: ignore[typeddict-item]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    if "networkMigrationExecutionID" in data:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    if "networkMigrationDefinitionID" in data:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if "createdAt" in data:
        import aws_sdk_mgn.types._prelude.timestamp

        out["created_at"] = aws_sdk_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "endedAt" in data:
        import aws_sdk_mgn.types._prelude.timestamp

        out["ended_at"] = aws_sdk_mgn.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    if "status" in data:
        out["status"] = data["status"]
    if "statusDetails" in data:
        out["status_details"] = data["statusDetails"]
    return out
