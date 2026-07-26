"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterRestoreStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.double
    import capo_securityhub.types.long
    import capo_securityhub.types.non_empty_string


class AwsRedshiftClusterRestoreStatus(TypedDict, closed=True):
    current_restore_rate_in_mega_bytes_per_second: NotRequired[
        "capo_securityhub.types.double.Double"
    ]
    """<p>The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup.</p> <p>This field is only updated when you restore to DC2 and DS2 node types.</p>"""
    elapsed_time_in_seconds: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish.</p> <p>This field is only updated when you restore to DC2 and DS2 node types.</p>"""
    estimated_time_to_completion_in_seconds: NotRequired[
        "capo_securityhub.types.long.Long"
    ]
    """<p>The estimate of the time remaining before the restore is complete. Returns 0 for a completed restore.</p> <p>This field is only updated when you restore to DC2 and DS2 node types.</p>"""
    progress_in_mega_bytes: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The number of megabytes that were transferred from snapshot storage.</p> <p>This field is only updated when you restore to DC2 and DS2 node types.</p>"""
    snapshot_size_in_mega_bytes: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The size of the set of snapshot data that was used to restore the cluster.</p> <p>This field is only updated when you restore to DC2 and DS2 node types.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the restore action.</p> <p>Valid values: <code>starting</code> | <code>restoring</code> | <code>completed</code> | <code>failed</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterRestoreStatus) -> dict:
    out: dict = {}
    if "current_restore_rate_in_mega_bytes_per_second" in value:
        out["CurrentRestoreRateInMegaBytesPerSecond"] = value[
            "current_restore_rate_in_mega_bytes_per_second"
        ]
    if "elapsed_time_in_seconds" in value:
        out["ElapsedTimeInSeconds"] = value["elapsed_time_in_seconds"]
    if "estimated_time_to_completion_in_seconds" in value:
        out["EstimatedTimeToCompletionInSeconds"] = value[
            "estimated_time_to_completion_in_seconds"
        ]
    if "progress_in_mega_bytes" in value:
        out["ProgressInMegaBytes"] = value["progress_in_mega_bytes"]
    if "snapshot_size_in_mega_bytes" in value:
        out["SnapshotSizeInMegaBytes"] = value["snapshot_size_in_mega_bytes"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterRestoreStatus:
    out: AwsRedshiftClusterRestoreStatus = {}  # type: ignore[typeddict-item]
    if "CurrentRestoreRateInMegaBytesPerSecond" in data:
        out["current_restore_rate_in_mega_bytes_per_second"] = data[
            "CurrentRestoreRateInMegaBytesPerSecond"
        ]
    if "ElapsedTimeInSeconds" in data:
        out["elapsed_time_in_seconds"] = data["ElapsedTimeInSeconds"]
    if "EstimatedTimeToCompletionInSeconds" in data:
        out["estimated_time_to_completion_in_seconds"] = data[
            "EstimatedTimeToCompletionInSeconds"
        ]
    if "ProgressInMegaBytes" in data:
        out["progress_in_mega_bytes"] = data["ProgressInMegaBytes"]
    if "SnapshotSizeInMegaBytes" in data:
        out["snapshot_size_in_mega_bytes"] = data["SnapshotSizeInMegaBytes"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
