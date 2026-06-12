"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskIndividualAssessment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.t_stamp


class ReplicationTaskIndividualAssessment(TypedDict):
    replication_task_individual_assessment_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Amazon Resource Name (ARN) of this individual assessment.</p>"""
    replication_task_assessment_run_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>ARN of the premigration assessment run that is created to run this individual assessment.</p>"""
    individual_assessment_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Name of this individual assessment.</p>"""
    status: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Individual assessment status.</p> <p>This status can have one of the following values:</p> <ul> <li> <p> <code>\"cancelled\"</code> </p> </li> <li> <p> <code>\"error\"</code> </p> </li> <li> <p> <code>\"failed\"</code> </p> </li> <li> <p> <code>\"passed\"</code> </p> </li> <li> <p> <code>\"pending\"</code> </p> </li> <li> <p> <code>\"skipped\"</code> </p> </li> <li> <p> <code>\"running\"</code> </p> </li> </ul>"""
    replication_task_individual_assessment_start_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>Date when this individual assessment was started as part of running the <code>StartReplicationTaskAssessmentRun</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskIndividualAssessment) -> dict:
    out: dict = {}
    if "replication_task_individual_assessment_arn" in value:
        out["ReplicationTaskIndividualAssessmentArn"] = value[
            "replication_task_individual_assessment_arn"
        ]
    if "replication_task_assessment_run_arn" in value:
        out["ReplicationTaskAssessmentRunArn"] = value[
            "replication_task_assessment_run_arn"
        ]
    if "individual_assessment_name" in value:
        out["IndividualAssessmentName"] = value["individual_assessment_name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "replication_task_individual_assessment_start_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["ReplicationTaskIndividualAssessmentStartDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_task_individual_assessment_start_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationTaskIndividualAssessment:
    out: ReplicationTaskIndividualAssessment = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskIndividualAssessmentArn" in data:
        out["replication_task_individual_assessment_arn"] = data[
            "ReplicationTaskIndividualAssessmentArn"
        ]
    if "ReplicationTaskAssessmentRunArn" in data:
        out["replication_task_assessment_run_arn"] = data[
            "ReplicationTaskAssessmentRunArn"
        ]
    if "IndividualAssessmentName" in data:
        out["individual_assessment_name"] = data["IndividualAssessmentName"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "ReplicationTaskIndividualAssessmentStartDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["replication_task_individual_assessment_start_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationTaskIndividualAssessmentStartDate"]
            )
        )
    return out
