"""Generated from Smithy shape ``com.amazonaws.redshift#RestoreStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.double
    import aws_sdk_redshift.types.long
    import aws_sdk_redshift.types.string


class RestoreStatus(TypedDict, closed=True):
    status: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The status of the restore action. Returns starting, restoring, completed, or failed.</p>"""
    current_restore_rate_in_mega_bytes_per_second: NotRequired[
        "aws_sdk_redshift.types.double.Double"
    ]
    """<p>The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 node types. </p>"""
    snapshot_size_in_mega_bytes: NotRequired["aws_sdk_redshift.types.long.Long"]
    """<p>The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 node types. </p>"""
    progress_in_mega_bytes: NotRequired["aws_sdk_redshift.types.long.Long"]
    """<p>The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 node types. </p>"""
    elapsed_time_in_seconds: NotRequired["aws_sdk_redshift.types.long.Long"]
    """<p>The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 node types. </p>"""
    estimated_time_to_completion_in_seconds: NotRequired[
        "aws_sdk_redshift.types.long.Long"
    ]
    """<p>The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 node types. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "current_restore_rate_in_mega_bytes_per_second" in value:
        pairs.append(
            (
                f"{prefix}.CurrentRestoreRateInMegaBytesPerSecond",
                str(value["current_restore_rate_in_mega_bytes_per_second"]),
            )
        )
    if "snapshot_size_in_mega_bytes" in value:
        pairs.append(
            (
                f"{prefix}.SnapshotSizeInMegaBytes",
                str(value["snapshot_size_in_mega_bytes"]),
            )
        )
    if "progress_in_mega_bytes" in value:
        pairs.append(
            (f"{prefix}.ProgressInMegaBytes", str(value["progress_in_mega_bytes"]))
        )
    if "elapsed_time_in_seconds" in value:
        pairs.append(
            (f"{prefix}.ElapsedTimeInSeconds", str(value["elapsed_time_in_seconds"]))
        )
    if "estimated_time_to_completion_in_seconds" in value:
        pairs.append(
            (
                f"{prefix}.EstimatedTimeToCompletionInSeconds",
                str(value["estimated_time_to_completion_in_seconds"]),
            )
        )


def deserialize_query(el: Element) -> RestoreStatus:
    out: RestoreStatus = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_current_restore_rate_in_mega_bytes_per_second = el.find(
        "CurrentRestoreRateInMegaBytesPerSecond"
    )
    if child_current_restore_rate_in_mega_bytes_per_second is not None:
        out["current_restore_rate_in_mega_bytes_per_second"] = float(
            child_current_restore_rate_in_mega_bytes_per_second.text or ""
        )
    child_snapshot_size_in_mega_bytes = el.find("SnapshotSizeInMegaBytes")
    if child_snapshot_size_in_mega_bytes is not None:
        out["snapshot_size_in_mega_bytes"] = int(
            child_snapshot_size_in_mega_bytes.text or ""
        )
    child_progress_in_mega_bytes = el.find("ProgressInMegaBytes")
    if child_progress_in_mega_bytes is not None:
        out["progress_in_mega_bytes"] = int(child_progress_in_mega_bytes.text or "")
    child_elapsed_time_in_seconds = el.find("ElapsedTimeInSeconds")
    if child_elapsed_time_in_seconds is not None:
        out["elapsed_time_in_seconds"] = int(child_elapsed_time_in_seconds.text or "")
    child_estimated_time_to_completion_in_seconds = el.find(
        "EstimatedTimeToCompletionInSeconds"
    )
    if child_estimated_time_to_completion_in_seconds is not None:
        out["estimated_time_to_completion_in_seconds"] = int(
            child_estimated_time_to_completion_in_seconds.text or ""
        )
    return out
