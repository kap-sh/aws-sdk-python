"""Generated from Smithy shape ``com.amazonaws.redshift#DataTransferProgress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.double_optional
    import capo_redshift.types.long
    import capo_redshift.types.long_optional
    import capo_redshift.types.string


class DataTransferProgress(TypedDict, closed=True):
    status: NotRequired["capo_redshift.types.string.String"]
    """<p>Describes the status of the cluster. While the transfer is in progress the status is <code>transferringdata</code>.</p>"""
    current_rate_in_mega_bytes_per_second: NotRequired[
        "capo_redshift.types.double_optional.DoubleOptional"
    ]
    """<p>Describes the data transfer rate in MB's per second.</p>"""
    total_data_in_mega_bytes: NotRequired["capo_redshift.types.long.Long"]
    """<p>Describes the total amount of data to be transfered in megabytes.</p>"""
    data_transferred_in_mega_bytes: NotRequired["capo_redshift.types.long.Long"]
    """<p>Describes the total amount of data that has been transfered in MB's.</p>"""
    estimated_time_to_completion_in_seconds: NotRequired[
        "capo_redshift.types.long_optional.LongOptional"
    ]
    """<p>Describes the estimated number of seconds remaining to complete the transfer.</p>"""
    elapsed_time_in_seconds: NotRequired[
        "capo_redshift.types.long_optional.LongOptional"
    ]
    """<p>Describes the number of seconds that have elapsed during the data transfer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DataTransferProgress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "current_rate_in_mega_bytes_per_second" in value:
        pairs.append(
            (
                f"{key_prefix}CurrentRateInMegaBytesPerSecond",
                str(value["current_rate_in_mega_bytes_per_second"]),
            )
        )
    if "total_data_in_mega_bytes" in value:
        pairs.append(
            (
                f"{key_prefix}TotalDataInMegaBytes",
                str(value["total_data_in_mega_bytes"]),
            )
        )
    if "data_transferred_in_mega_bytes" in value:
        pairs.append(
            (
                f"{key_prefix}DataTransferredInMegaBytes",
                str(value["data_transferred_in_mega_bytes"]),
            )
        )
    if "estimated_time_to_completion_in_seconds" in value:
        pairs.append(
            (
                f"{key_prefix}EstimatedTimeToCompletionInSeconds",
                str(value["estimated_time_to_completion_in_seconds"]),
            )
        )
    if "elapsed_time_in_seconds" in value:
        pairs.append(
            (f"{key_prefix}ElapsedTimeInSeconds", str(value["elapsed_time_in_seconds"]))
        )


def deserialize_query(el: Element) -> DataTransferProgress:
    out: DataTransferProgress = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_current_rate_in_mega_bytes_per_second = el.find(
        "CurrentRateInMegaBytesPerSecond"
    )
    if child_current_rate_in_mega_bytes_per_second is not None:
        out["current_rate_in_mega_bytes_per_second"] = float(
            child_current_rate_in_mega_bytes_per_second.text or ""
        )
    child_total_data_in_mega_bytes = el.find("TotalDataInMegaBytes")
    if child_total_data_in_mega_bytes is not None:
        out["total_data_in_mega_bytes"] = int(child_total_data_in_mega_bytes.text or "")
    child_data_transferred_in_mega_bytes = el.find("DataTransferredInMegaBytes")
    if child_data_transferred_in_mega_bytes is not None:
        out["data_transferred_in_mega_bytes"] = int(
            child_data_transferred_in_mega_bytes.text or ""
        )
    child_estimated_time_to_completion_in_seconds = el.find(
        "EstimatedTimeToCompletionInSeconds"
    )
    if child_estimated_time_to_completion_in_seconds is not None:
        out["estimated_time_to_completion_in_seconds"] = int(
            child_estimated_time_to_completion_in_seconds.text or ""
        )
    child_elapsed_time_in_seconds = el.find("ElapsedTimeInSeconds")
    if child_elapsed_time_in_seconds is not None:
        out["elapsed_time_in_seconds"] = int(child_elapsed_time_in_seconds.text or "")
    return out
