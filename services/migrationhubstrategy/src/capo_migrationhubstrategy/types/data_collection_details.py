"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#DataCollectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.assessment_status
    import capo_migrationhubstrategy.types.assessment_status_message
    import capo_migrationhubstrategy.types.integer
    import capo_migrationhubstrategy.types.time_stamp


class DataCollectionDetails(TypedDict, closed=True):
    status: NotRequired[
        "capo_migrationhubstrategy.types.assessment_status.AssessmentStatus"
    ]
    """<p> The status of the assessment. </p>"""
    servers: NotRequired["capo_migrationhubstrategy.types.integer.Integer"]
    """<p> The total number of servers in the assessment. </p>"""
    failed: NotRequired["capo_migrationhubstrategy.types.integer.Integer"]
    """<p> The number of failed servers in the assessment. </p>"""
    success: NotRequired["capo_migrationhubstrategy.types.integer.Integer"]
    """<p> The number of successful servers in the assessment. </p>"""
    in_progress: NotRequired["capo_migrationhubstrategy.types.integer.Integer"]
    """<p> The number of servers with the assessment status <code>IN_PROGESS</code>. </p>"""
    start_time: NotRequired["capo_migrationhubstrategy.types.time_stamp.TimeStamp"]
    """<p> The start time of assessment. </p>"""
    completion_time: NotRequired["capo_migrationhubstrategy.types.time_stamp.TimeStamp"]
    """<p> The time the assessment completes. </p>"""
    status_message: NotRequired[
        "capo_migrationhubstrategy.types.assessment_status_message.AssessmentStatusMessage"
    ]
    """<p>The status message of the assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataCollectionDetails) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "servers" in value:
        out["servers"] = value["servers"]
    if "failed" in value:
        out["failed"] = value["failed"]
    if "success" in value:
        out["success"] = value["success"]
    if "in_progress" in value:
        out["inProgress"] = value["in_progress"]
    if "start_time" in value:
        import capo_migrationhubstrategy.types.time_stamp

        out["startTime"] = capo_migrationhubstrategy.types.time_stamp.serialize_json(
            value["start_time"]
        )
    if "completion_time" in value:
        import capo_migrationhubstrategy.types.time_stamp

        out["completionTime"] = (
            capo_migrationhubstrategy.types.time_stamp.serialize_json(
                value["completion_time"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> DataCollectionDetails:
    out: DataCollectionDetails = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "servers" in data:
        out["servers"] = data["servers"]
    if "failed" in data:
        out["failed"] = data["failed"]
    if "success" in data:
        out["success"] = data["success"]
    if "inProgress" in data:
        out["in_progress"] = data["inProgress"]
    if "startTime" in data:
        import capo_migrationhubstrategy.types.time_stamp

        out["start_time"] = capo_migrationhubstrategy.types.time_stamp.deserialize_json(
            data["startTime"]
        )
    if "completionTime" in data:
        import capo_migrationhubstrategy.types.time_stamp

        out["completion_time"] = (
            capo_migrationhubstrategy.types.time_stamp.deserialize_json(
                data["completionTime"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
