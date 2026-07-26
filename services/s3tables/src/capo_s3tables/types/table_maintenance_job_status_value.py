"""Generated from Smithy shape ``com.amazonaws.s3tables#TableMaintenanceJobStatusValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.job_status


class TableMaintenanceJobStatusValue(TypedDict, closed=True):
    status: "capo_s3tables.types.job_status.JobStatus"
    """<p>The status of the job.</p>"""
    last_run_timestamp: NotRequired["datetime.datetime"]
    """<p>The date and time that the maintenance job was last run.</p>"""
    failure_message: NotRequired["str"]
    """<p>The failure message of a failed job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableMaintenanceJobStatusValue) -> dict:
    out: dict = {}
    import capo_s3tables.types.job_status

    out["status"] = capo_s3tables.types.job_status.serialize_json(value["status"])
    if "last_run_timestamp" in value:
        import capo_s3tables.types._prelude.timestamp

        out["lastRunTimestamp"] = capo_s3tables.types._prelude.timestamp.serialize_json(
            value["last_run_timestamp"]
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> TableMaintenanceJobStatusValue:
    out: TableMaintenanceJobStatusValue = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_s3tables.types.job_status

        out["status"] = capo_s3tables.types.job_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("TableMaintenanceJobStatusValue.status required")
    if "lastRunTimestamp" in data:
        import capo_s3tables.types._prelude.timestamp

        out["last_run_timestamp"] = (
            capo_s3tables.types._prelude.timestamp.deserialize_json(
                data["lastRunTimestamp"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
