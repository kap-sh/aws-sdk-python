"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationTaskAssessmentRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_task_assessment_run_list
    import aws_sdk_database_migration_service.types.string


class DescribeReplicationTaskAssessmentRunsResponse(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A pagination token returned for you to pass to a subsequent request. If you pass this token as the <code>Marker</code> value in a subsequent request, the response includes only records beyond the marker, up to the value specified in the request by <code>MaxRecords</code>.</p>"""
    replication_task_assessment_runs: NotRequired[
        "aws_sdk_database_migration_service.types.replication_task_assessment_run_list.ReplicationTaskAssessmentRunList"
    ]
    """<p>One or more premigration assessment runs as specified by <code>Filters</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeReplicationTaskAssessmentRunsResponse,
) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "replication_task_assessment_runs" in value:
        import aws_sdk_database_migration_service.types.replication_task_assessment_run_list

        out["ReplicationTaskAssessmentRuns"] = (
            aws_sdk_database_migration_service.types.replication_task_assessment_run_list.serialize_aws_json_1_1(
                value["replication_task_assessment_runs"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeReplicationTaskAssessmentRunsResponse:
    out: DescribeReplicationTaskAssessmentRunsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "ReplicationTaskAssessmentRuns" in data:
        import aws_sdk_database_migration_service.types.replication_task_assessment_run_list

        out["replication_task_assessment_runs"] = (
            aws_sdk_database_migration_service.types.replication_task_assessment_run_list.deserialize_aws_json_1_1(
                data["ReplicationTaskAssessmentRuns"]
            )
        )
    return out
