"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationTaskIndividualAssessmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_task_individual_assessment_list
    import aws_sdk_database_migration_service.types.string


class DescribeReplicationTaskIndividualAssessmentsResponse(TypedDict):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A pagination token returned for you to pass to a subsequent request. If you pass this token as the <code>Marker</code> value in a subsequent request, the response includes only records beyond the marker, up to the value specified in the request by <code>MaxRecords</code>.</p>"""
    replication_task_individual_assessments: NotRequired[
        "aws_sdk_database_migration_service.types.replication_task_individual_assessment_list.ReplicationTaskIndividualAssessmentList"
    ]
    """<p>One or more individual assessments as specified by <code>Filters</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeReplicationTaskIndividualAssessmentsResponse,
) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "replication_task_individual_assessments" in value:
        import aws_sdk_database_migration_service.types.replication_task_individual_assessment_list

        out["ReplicationTaskIndividualAssessments"] = (
            aws_sdk_database_migration_service.types.replication_task_individual_assessment_list.serialize_aws_json_1_1(
                value["replication_task_individual_assessments"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeReplicationTaskIndividualAssessmentsResponse:
    out: DescribeReplicationTaskIndividualAssessmentsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "ReplicationTaskIndividualAssessments" in data:
        import aws_sdk_database_migration_service.types.replication_task_individual_assessment_list

        out["replication_task_individual_assessments"] = (
            aws_sdk_database_migration_service.types.replication_task_individual_assessment_list.deserialize_aws_json_1_1(
                data["ReplicationTaskIndividualAssessments"]
            )
        )
    return out
