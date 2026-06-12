"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskAssessmentRunProgress``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.integer


class ReplicationTaskAssessmentRunProgress(TypedDict):
    individual_assessment_count: (
        "aws_sdk_database_migration_service.types.integer.Integer"
    )
    """<p>The number of individual assessments that are specified to run.</p>"""
    individual_assessment_completed_count: (
        "aws_sdk_database_migration_service.types.integer.Integer"
    )
    """<p>The number of individual assessments that have completed, successfully or not.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskAssessmentRunProgress) -> dict:
    out: dict = {}
    out["IndividualAssessmentCount"] = value.get("individual_assessment_count", 0)
    out["IndividualAssessmentCompletedCount"] = value.get(
        "individual_assessment_completed_count", 0
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationTaskAssessmentRunProgress:
    out: ReplicationTaskAssessmentRunProgress = {}  # type: ignore[typeddict-item]
    if "IndividualAssessmentCount" in data:
        out["individual_assessment_count"] = data["IndividualAssessmentCount"]
    else:
        out["individual_assessment_count"] = 0
    if "IndividualAssessmentCompletedCount" in data:
        out["individual_assessment_completed_count"] = data[
            "IndividualAssessmentCompletedCount"
        ]
    else:
        out["individual_assessment_completed_count"] = 0
    return out
