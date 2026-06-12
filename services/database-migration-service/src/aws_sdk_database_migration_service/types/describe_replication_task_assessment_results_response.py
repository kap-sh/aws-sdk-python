"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationTaskAssessmentResultsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_task_assessment_result_list
    import aws_sdk_database_migration_service.types.string


class DescribeReplicationTaskAssessmentResultsResponse(TypedDict):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    bucket_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>- The Amazon S3 bucket where the task assessment report is located. </p>"""
    replication_task_assessment_results: NotRequired[
        "aws_sdk_database_migration_service.types.replication_task_assessment_result_list.ReplicationTaskAssessmentResultList"
    ]
    """<p> The task assessment report. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeReplicationTaskAssessmentResultsResponse,
) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "replication_task_assessment_results" in value:
        import aws_sdk_database_migration_service.types.replication_task_assessment_result_list

        out["ReplicationTaskAssessmentResults"] = (
            aws_sdk_database_migration_service.types.replication_task_assessment_result_list.serialize_aws_json_1_1(
                value["replication_task_assessment_results"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeReplicationTaskAssessmentResultsResponse:
    out: DescribeReplicationTaskAssessmentResultsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    if "ReplicationTaskAssessmentResults" in data:
        import aws_sdk_database_migration_service.types.replication_task_assessment_result_list

        out["replication_task_assessment_results"] = (
            aws_sdk_database_migration_service.types.replication_task_assessment_result_list.deserialize_aws_json_1_1(
                data["ReplicationTaskAssessmentResults"]
            )
        )
    return out
