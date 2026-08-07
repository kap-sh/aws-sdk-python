"""Generated from Smithy shape ``com.amazonaws.redshift#ResizeProgressMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.double_optional
    import capo_redshift.types.import_tables_completed
    import capo_redshift.types.import_tables_in_progress
    import capo_redshift.types.import_tables_not_started
    import capo_redshift.types.integer_optional
    import capo_redshift.types.long_optional
    import capo_redshift.types.string


class ResizeProgressMessage(TypedDict, closed=True):
    target_node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The node type that the cluster will have after the resize operation is complete.</p>"""
    target_number_of_nodes: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of nodes that the cluster will have after the resize operation is complete.</p>"""
    target_cluster_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The cluster type after the resize operation is complete.</p> <p>Valid Values: <code>multi-node</code> | <code>single-node</code> </p>"""
    status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of the resize operation.</p> <p>Valid Values: <code>NONE</code> | <code>IN_PROGRESS</code> | <code>FAILED</code> | <code>SUCCEEDED</code> | <code>CANCELLING</code> </p>"""
    import_tables_completed: NotRequired[
        "capo_redshift.types.import_tables_completed.ImportTablesCompleted"
    ]
    """<p>The names of tables that have been completely imported .</p> <p>Valid Values: List of table names.</p>"""
    import_tables_in_progress: NotRequired[
        "capo_redshift.types.import_tables_in_progress.ImportTablesInProgress"
    ]
    """<p>The names of tables that are being currently imported.</p> <p>Valid Values: List of table names.</p>"""
    import_tables_not_started: NotRequired[
        "capo_redshift.types.import_tables_not_started.ImportTablesNotStarted"
    ]
    """<p>The names of tables that have not been yet imported.</p> <p>Valid Values: List of table names</p>"""
    avg_resize_rate_in_mega_bytes_per_second: NotRequired[
        "capo_redshift.types.double_optional.DoubleOptional"
    ]
    """<p>The average rate of the resize operation over the last few minutes, measured in megabytes per second. After the resize operation completes, this value shows the average rate of the entire resize operation.</p>"""
    total_resize_data_in_mega_bytes: NotRequired[
        "capo_redshift.types.long_optional.LongOptional"
    ]
    """<p>The estimated total amount of data, in megabytes, on the cluster before the resize operation began.</p>"""
    progress_in_mega_bytes: NotRequired[
        "capo_redshift.types.long_optional.LongOptional"
    ]
    """<p>While the resize operation is in progress, this value shows the current amount of data, in megabytes, that has been processed so far. When the resize operation is complete, this value shows the total amount of data, in megabytes, on the cluster, which may be more or less than TotalResizeDataInMegaBytes (the estimated total amount of data before resize).</p>"""
    elapsed_time_in_seconds: NotRequired[
        "capo_redshift.types.long_optional.LongOptional"
    ]
    """<p>The amount of seconds that have elapsed since the resize operation began. After the resize operation completes, this value shows the total actual time, in seconds, for the resize operation.</p>"""
    estimated_time_to_completion_in_seconds: NotRequired[
        "capo_redshift.types.long_optional.LongOptional"
    ]
    """<p>The estimated time remaining, in seconds, until the resize operation is complete. This value is calculated based on the average resize rate and the estimated amount of data remaining to be processed. Once the resize operation is complete, this value will be 0.</p>"""
    resize_type: NotRequired["capo_redshift.types.string.String"]
    """<p>An enum with possible values of <code>ClassicResize</code> and <code>ElasticResize</code>. These values describe the type of resize operation being performed. </p>"""
    message: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional string to provide additional details about the resize action.</p>"""
    target_encryption_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The type of encryption for the cluster after the resize is complete.</p> <p>Possible values are <code>KMS</code> and <code>None</code>. </p>"""
    data_transfer_progress_percent: NotRequired[
        "capo_redshift.types.double_optional.DoubleOptional"
    ]
    """<p>The percent of data transferred from source cluster to target cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResizeProgressMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target_node_type" in value:
        pairs.append((f"{key_prefix}TargetNodeType", str(value["target_node_type"])))
    if "target_number_of_nodes" in value:
        pairs.append(
            (f"{key_prefix}TargetNumberOfNodes", str(value["target_number_of_nodes"]))
        )
    if "target_cluster_type" in value:
        pairs.append(
            (f"{key_prefix}TargetClusterType", str(value["target_cluster_type"]))
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "import_tables_completed" in value:
        import capo_redshift.types.import_tables_completed

        capo_redshift.types.import_tables_completed.serialize_query(
            value["import_tables_completed"],
            pairs,
            f"{key_prefix}ImportTablesCompleted",
        )
    if "import_tables_in_progress" in value:
        import capo_redshift.types.import_tables_in_progress

        capo_redshift.types.import_tables_in_progress.serialize_query(
            value["import_tables_in_progress"],
            pairs,
            f"{key_prefix}ImportTablesInProgress",
        )
    if "import_tables_not_started" in value:
        import capo_redshift.types.import_tables_not_started

        capo_redshift.types.import_tables_not_started.serialize_query(
            value["import_tables_not_started"],
            pairs,
            f"{key_prefix}ImportTablesNotStarted",
        )
    if "avg_resize_rate_in_mega_bytes_per_second" in value:
        pairs.append(
            (
                f"{key_prefix}AvgResizeRateInMegaBytesPerSecond",
                str(value["avg_resize_rate_in_mega_bytes_per_second"]),
            )
        )
    if "total_resize_data_in_mega_bytes" in value:
        pairs.append(
            (
                f"{key_prefix}TotalResizeDataInMegaBytes",
                str(value["total_resize_data_in_mega_bytes"]),
            )
        )
    if "progress_in_mega_bytes" in value:
        pairs.append(
            (f"{key_prefix}ProgressInMegaBytes", str(value["progress_in_mega_bytes"]))
        )
    if "elapsed_time_in_seconds" in value:
        pairs.append(
            (f"{key_prefix}ElapsedTimeInSeconds", str(value["elapsed_time_in_seconds"]))
        )
    if "estimated_time_to_completion_in_seconds" in value:
        pairs.append(
            (
                f"{key_prefix}EstimatedTimeToCompletionInSeconds",
                str(value["estimated_time_to_completion_in_seconds"]),
            )
        )
    if "resize_type" in value:
        pairs.append((f"{key_prefix}ResizeType", str(value["resize_type"])))
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))
    if "target_encryption_type" in value:
        pairs.append(
            (f"{key_prefix}TargetEncryptionType", str(value["target_encryption_type"]))
        )
    if "data_transfer_progress_percent" in value:
        pairs.append(
            (
                f"{key_prefix}DataTransferProgressPercent",
                str(value["data_transfer_progress_percent"]),
            )
        )


def deserialize_query(el: Element) -> ResizeProgressMessage:
    out: ResizeProgressMessage = {}  # type: ignore[typeddict-item]
    child_target_node_type = el.find("TargetNodeType")
    if child_target_node_type is not None:
        out["target_node_type"] = str(child_target_node_type.text or "")
    child_target_number_of_nodes = el.find("TargetNumberOfNodes")
    if child_target_number_of_nodes is not None:
        out["target_number_of_nodes"] = int(child_target_number_of_nodes.text or "")
    child_target_cluster_type = el.find("TargetClusterType")
    if child_target_cluster_type is not None:
        out["target_cluster_type"] = str(child_target_cluster_type.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_import_tables_completed = el.find("ImportTablesCompleted")
    if child_import_tables_completed is not None:
        import capo_redshift.types.import_tables_completed

        out["import_tables_completed"] = (
            capo_redshift.types.import_tables_completed.deserialize_query(
                child_import_tables_completed
            )
        )
    child_import_tables_in_progress = el.find("ImportTablesInProgress")
    if child_import_tables_in_progress is not None:
        import capo_redshift.types.import_tables_in_progress

        out["import_tables_in_progress"] = (
            capo_redshift.types.import_tables_in_progress.deserialize_query(
                child_import_tables_in_progress
            )
        )
    child_import_tables_not_started = el.find("ImportTablesNotStarted")
    if child_import_tables_not_started is not None:
        import capo_redshift.types.import_tables_not_started

        out["import_tables_not_started"] = (
            capo_redshift.types.import_tables_not_started.deserialize_query(
                child_import_tables_not_started
            )
        )
    child_avg_resize_rate_in_mega_bytes_per_second = el.find(
        "AvgResizeRateInMegaBytesPerSecond"
    )
    if child_avg_resize_rate_in_mega_bytes_per_second is not None:
        out["avg_resize_rate_in_mega_bytes_per_second"] = float(
            child_avg_resize_rate_in_mega_bytes_per_second.text or ""
        )
    child_total_resize_data_in_mega_bytes = el.find("TotalResizeDataInMegaBytes")
    if child_total_resize_data_in_mega_bytes is not None:
        out["total_resize_data_in_mega_bytes"] = int(
            child_total_resize_data_in_mega_bytes.text or ""
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
    child_resize_type = el.find("ResizeType")
    if child_resize_type is not None:
        out["resize_type"] = str(child_resize_type.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_target_encryption_type = el.find("TargetEncryptionType")
    if child_target_encryption_type is not None:
        out["target_encryption_type"] = str(child_target_encryption_type.text or "")
    child_data_transfer_progress_percent = el.find("DataTransferProgressPercent")
    if child_data_transfer_progress_percent is not None:
        out["data_transfer_progress_percent"] = float(
            child_data_transfer_progress_percent.text or ""
        )
    return out
