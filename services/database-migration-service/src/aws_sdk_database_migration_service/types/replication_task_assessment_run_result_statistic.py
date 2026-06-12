"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskAssessmentRunResultStatistic``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.integer


class ReplicationTaskAssessmentRunResultStatistic(TypedDict):
    passed: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The number of individual assessments that successfully passed all checks in the assessment run.</p>"""
    failed: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The number of individual assessments that failed to meet the criteria defined in the assessment run.</p>"""
    error: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The number of individual assessments that encountered a critical error and could not complete properly.</p>"""
    warning: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>Indicates that the recent completed AssessmentRun triggered a warning.</p>"""
    cancelled: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p> The number of individual assessments that were cancelled during the assessment run. </p>"""
    skipped: "aws_sdk_database_migration_service.types.integer.Integer"
    """<p>The number of individual assessments that were skipped during the assessment run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskAssessmentRunResultStatistic) -> dict:
    out: dict = {}
    out["Passed"] = value.get("passed", 0)
    out["Failed"] = value.get("failed", 0)
    out["Error"] = value.get("error", 0)
    out["Warning"] = value.get("warning", 0)
    out["Cancelled"] = value.get("cancelled", 0)
    out["Skipped"] = value.get("skipped", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationTaskAssessmentRunResultStatistic:
    out: ReplicationTaskAssessmentRunResultStatistic = {}  # type: ignore[typeddict-item]
    if "Passed" in data:
        out["passed"] = data["Passed"]
    else:
        out["passed"] = 0
    if "Failed" in data:
        out["failed"] = data["Failed"]
    else:
        out["failed"] = 0
    if "Error" in data:
        out["error"] = data["Error"]
    else:
        out["error"] = 0
    if "Warning" in data:
        out["warning"] = data["Warning"]
    else:
        out["warning"] = 0
    if "Cancelled" in data:
        out["cancelled"] = data["Cancelled"]
    else:
        out["cancelled"] = 0
    if "Skipped" in data:
        out["skipped"] = data["Skipped"]
    else:
        out["skipped"] = 0
    return out
