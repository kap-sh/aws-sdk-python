"""Generated from Smithy shape ``com.amazonaws.iot#TaskStatisticsForAuditCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.canceled_findings_count
    import aws_sdk_iot.types.failed_findings_count
    import aws_sdk_iot.types.skipped_findings_count
    import aws_sdk_iot.types.succeeded_findings_count
    import aws_sdk_iot.types.total_findings_count


class TaskStatisticsForAuditCheck(TypedDict, closed=True):
    total_findings_count: NotRequired[
        "aws_sdk_iot.types.total_findings_count.TotalFindingsCount"
    ]
    """<p>The total number of findings to which a task is being applied.</p>"""
    failed_findings_count: NotRequired[
        "aws_sdk_iot.types.failed_findings_count.FailedFindingsCount"
    ]
    """<p>The number of findings for which at least one of the actions failed when applied.</p>"""
    succeeded_findings_count: NotRequired[
        "aws_sdk_iot.types.succeeded_findings_count.SucceededFindingsCount"
    ]
    """<p>The number of findings for which all mitigation actions succeeded when applied.</p>"""
    skipped_findings_count: NotRequired[
        "aws_sdk_iot.types.skipped_findings_count.SkippedFindingsCount"
    ]
    """<p>The number of findings skipped because of filter conditions provided in the parameters to the command.</p>"""
    canceled_findings_count: NotRequired[
        "aws_sdk_iot.types.canceled_findings_count.CanceledFindingsCount"
    ]
    """<p>The number of findings to which the mitigation action task was canceled when applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskStatisticsForAuditCheck) -> dict:
    out: dict = {}
    if "total_findings_count" in value:
        out["totalFindingsCount"] = value["total_findings_count"]
    if "failed_findings_count" in value:
        out["failedFindingsCount"] = value["failed_findings_count"]
    if "succeeded_findings_count" in value:
        out["succeededFindingsCount"] = value["succeeded_findings_count"]
    if "skipped_findings_count" in value:
        out["skippedFindingsCount"] = value["skipped_findings_count"]
    if "canceled_findings_count" in value:
        out["canceledFindingsCount"] = value["canceled_findings_count"]
    return out


def deserialize_json(data: dict) -> TaskStatisticsForAuditCheck:
    out: TaskStatisticsForAuditCheck = {}  # type: ignore[typeddict-item]
    if "totalFindingsCount" in data:
        out["total_findings_count"] = data["totalFindingsCount"]
    if "failedFindingsCount" in data:
        out["failed_findings_count"] = data["failedFindingsCount"]
    if "succeededFindingsCount" in data:
        out["succeeded_findings_count"] = data["succeededFindingsCount"]
    if "skippedFindingsCount" in data:
        out["skipped_findings_count"] = data["skippedFindingsCount"]
    if "canceledFindingsCount" in data:
        out["canceled_findings_count"] = data["canceledFindingsCount"]
    return out
