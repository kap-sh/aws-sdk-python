"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskAssessmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp


class ReplicationTaskAssessmentResult(TypedDict, closed=True):
    replication_task_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p> The replication task identifier of the task on which the task assessment was run. </p>"""
    replication_task_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replication task. </p>"""
    replication_task_last_assessment_date: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date the task assessment was completed. </p>"""
    assessment_status: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p> The status of the task assessment. </p>"""
    assessment_results_file: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p> The file containing the results of the task assessment. </p>"""
    assessment_results: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p> The task assessment results in JSON format. </p> <p>The response object only contains this field if you provide <a>DescribeReplicationTaskAssessmentResultsMessage$ReplicationTaskArn</a> in the request.</p>"""
    s3_object_url: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p> The URL of the S3 object containing the task assessment results. </p> <p>The response object only contains this field if you provide <a>DescribeReplicationTaskAssessmentResultsMessage$ReplicationTaskArn</a> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskAssessmentResult) -> dict:
    out: dict = {}
    if "replication_task_identifier" in value:
        out["ReplicationTaskIdentifier"] = value["replication_task_identifier"]
    if "replication_task_arn" in value:
        out["ReplicationTaskArn"] = value["replication_task_arn"]
    if "replication_task_last_assessment_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["ReplicationTaskLastAssessmentDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_task_last_assessment_date"]
            )
        )
    if "assessment_status" in value:
        out["AssessmentStatus"] = value["assessment_status"]
    if "assessment_results_file" in value:
        out["AssessmentResultsFile"] = value["assessment_results_file"]
    if "assessment_results" in value:
        out["AssessmentResults"] = value["assessment_results"]
    if "s3_object_url" in value:
        out["S3ObjectUrl"] = value["s3_object_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationTaskAssessmentResult:
    out: ReplicationTaskAssessmentResult = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskIdentifier" in data:
        out["replication_task_identifier"] = data["ReplicationTaskIdentifier"]
    if "ReplicationTaskArn" in data:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    if "ReplicationTaskLastAssessmentDate" in data:
        import capo_database_migration_service.types.t_stamp

        out["replication_task_last_assessment_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationTaskLastAssessmentDate"]
            )
        )
    if "AssessmentStatus" in data:
        out["assessment_status"] = data["AssessmentStatus"]
    if "AssessmentResultsFile" in data:
        out["assessment_results_file"] = data["AssessmentResultsFile"]
    if "AssessmentResults" in data:
        out["assessment_results"] = data["AssessmentResults"]
    if "S3ObjectUrl" in data:
        out["s3_object_url"] = data["S3ObjectUrl"]
    return out
