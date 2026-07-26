"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ServerStatusSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.integer
    import capo_migrationhubstrategy.types.run_time_assessment_status


class ServerStatusSummary(TypedDict, closed=True):
    run_time_assessment_status: NotRequired[
        "capo_migrationhubstrategy.types.run_time_assessment_status.RunTimeAssessmentStatus"
    ]
    """<p>The status of the run time.</p>"""
    count: NotRequired["capo_migrationhubstrategy.types.integer.Integer"]
    """<p>The number of servers successfully analyzed, partially successful or failed analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerStatusSummary) -> dict:
    out: dict = {}
    if "run_time_assessment_status" in value:
        out["runTimeAssessmentStatus"] = value["run_time_assessment_status"]
    if "count" in value:
        out["count"] = value["count"]
    return out


def deserialize_json(data: dict) -> ServerStatusSummary:
    out: ServerStatusSummary = {}  # type: ignore[typeddict-item]
    if "runTimeAssessmentStatus" in data:
        out["run_time_assessment_status"] = data["runTimeAssessmentStatus"]
    if "count" in data:
        out["count"] = data["count"]
    return out
