"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerRun``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.compaction_metrics
    import aws_sdk_glue.types.compaction_strategy
    import aws_sdk_glue.types.message_string
    import aws_sdk_glue.types.orphan_file_deletion_metrics
    import aws_sdk_glue.types.retention_metrics
    import aws_sdk_glue.types.run_metrics
    import aws_sdk_glue.types.table_optimizer_event_type
    import aws_sdk_glue.types.table_optimizer_run_timestamp


class TableOptimizerRun(TypedDict):
    event_type: NotRequired[
        "aws_sdk_glue.types.table_optimizer_event_type.TableOptimizerEventType"
    ]
    """<p>An event type representing the status of the table optimizer run.</p>"""
    start_timestamp: NotRequired[
        "aws_sdk_glue.types.table_optimizer_run_timestamp.TableOptimizerRunTimestamp"
    ]
    """<p>Represents the epoch timestamp at which the compaction job was started within Lake Formation.</p>"""
    end_timestamp: NotRequired[
        "aws_sdk_glue.types.table_optimizer_run_timestamp.TableOptimizerRunTimestamp"
    ]
    """<p>Represents the epoch timestamp at which the compaction job ended.</p>"""
    metrics: NotRequired["aws_sdk_glue.types.run_metrics.RunMetrics"]
    """<p>A <code>RunMetrics</code> object containing metrics for the optimizer run.</p> <p>This member is deprecated. See the individual metric members for compaction, retention, and orphan file deletion.</p>"""
    error: NotRequired["aws_sdk_glue.types.message_string.MessageString"]
    """<p>An error that occured during the optimizer run.</p>"""
    compaction_metrics: NotRequired[
        "aws_sdk_glue.types.compaction_metrics.CompactionMetrics"
    ]
    """<p>A <code>CompactionMetrics</code> object containing metrics for the optimizer run.</p>"""
    compaction_strategy: NotRequired[
        "aws_sdk_glue.types.compaction_strategy.CompactionStrategy"
    ]
    """<p>The strategy used for the compaction run. Indicates which algorithm was applied to determine how files were selected and combined during the compaction process. Valid values are:</p> <ul> <li> <p> <code>binpack</code>: Combines small files into larger files, typically targeting sizes over 100MB, while applying any pending deletes. This is the recommended compaction strategy for most use cases. </p> </li> <li> <p> <code>sort</code>: Organizes data based on specified columns which are sorted hierarchically during compaction, improving query performance for filtered operations. This strategy is recommended when your queries frequently filter on specific columns. To use this strategy, you must first define a sort order in your Iceberg table properties using the <code>sort_order</code> table property.</p> </li> <li> <p> <code>z-order</code>: Optimizes data organization by blending multiple attributes into a single scalar value that can be used for sorting, allowing efficient querying across multiple dimensions. This strategy is recommended when you need to query data across multiple dimensions simultaneously. To use this strategy, you must first define a sort order in your Iceberg table properties using the <code>sort_order</code> table property. </p> </li> </ul>"""
    retention_metrics: NotRequired[
        "aws_sdk_glue.types.retention_metrics.RetentionMetrics"
    ]
    """<p>A <code>RetentionMetrics</code> object containing metrics for the optimizer run.</p>"""
    orphan_file_deletion_metrics: NotRequired[
        "aws_sdk_glue.types.orphan_file_deletion_metrics.OrphanFileDeletionMetrics"
    ]
    """<p>An <code>OrphanFileDeletionMetrics</code> object containing metrics for the optimizer run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableOptimizerRun) -> dict:
    out: dict = {}
    if "event_type" in value:
        import aws_sdk_glue.types.table_optimizer_event_type

        out["eventType"] = (
            aws_sdk_glue.types.table_optimizer_event_type.serialize_aws_json_1_1(
                value["event_type"]
            )
        )
    if "start_timestamp" in value:
        import aws_sdk_glue.types.table_optimizer_run_timestamp

        out["startTimestamp"] = (
            aws_sdk_glue.types.table_optimizer_run_timestamp.serialize_aws_json_1_1(
                value["start_timestamp"]
            )
        )
    if "end_timestamp" in value:
        import aws_sdk_glue.types.table_optimizer_run_timestamp

        out["endTimestamp"] = (
            aws_sdk_glue.types.table_optimizer_run_timestamp.serialize_aws_json_1_1(
                value["end_timestamp"]
            )
        )
    if "metrics" in value:
        import aws_sdk_glue.types.run_metrics

        out["metrics"] = aws_sdk_glue.types.run_metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    if "error" in value:
        out["error"] = value["error"]
    if "compaction_metrics" in value:
        import aws_sdk_glue.types.compaction_metrics

        out["compactionMetrics"] = (
            aws_sdk_glue.types.compaction_metrics.serialize_aws_json_1_1(
                value["compaction_metrics"]
            )
        )
    if "compaction_strategy" in value:
        import aws_sdk_glue.types.compaction_strategy

        out["compactionStrategy"] = (
            aws_sdk_glue.types.compaction_strategy.serialize_aws_json_1_1(
                value["compaction_strategy"]
            )
        )
    if "retention_metrics" in value:
        import aws_sdk_glue.types.retention_metrics

        out["retentionMetrics"] = (
            aws_sdk_glue.types.retention_metrics.serialize_aws_json_1_1(
                value["retention_metrics"]
            )
        )
    if "orphan_file_deletion_metrics" in value:
        import aws_sdk_glue.types.orphan_file_deletion_metrics

        out["orphanFileDeletionMetrics"] = (
            aws_sdk_glue.types.orphan_file_deletion_metrics.serialize_aws_json_1_1(
                value["orphan_file_deletion_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableOptimizerRun:
    out: TableOptimizerRun = {}  # type: ignore[typeddict-item]
    if "eventType" in data:
        import aws_sdk_glue.types.table_optimizer_event_type

        out["event_type"] = (
            aws_sdk_glue.types.table_optimizer_event_type.deserialize_aws_json_1_1(
                data["eventType"]
            )
        )
    if "startTimestamp" in data:
        import aws_sdk_glue.types.table_optimizer_run_timestamp

        out["start_timestamp"] = (
            aws_sdk_glue.types.table_optimizer_run_timestamp.deserialize_aws_json_1_1(
                data["startTimestamp"]
            )
        )
    if "endTimestamp" in data:
        import aws_sdk_glue.types.table_optimizer_run_timestamp

        out["end_timestamp"] = (
            aws_sdk_glue.types.table_optimizer_run_timestamp.deserialize_aws_json_1_1(
                data["endTimestamp"]
            )
        )
    if "metrics" in data:
        import aws_sdk_glue.types.run_metrics

        out["metrics"] = aws_sdk_glue.types.run_metrics.deserialize_aws_json_1_1(
            data["metrics"]
        )
    if "error" in data:
        out["error"] = data["error"]
    if "compactionMetrics" in data:
        import aws_sdk_glue.types.compaction_metrics

        out["compaction_metrics"] = (
            aws_sdk_glue.types.compaction_metrics.deserialize_aws_json_1_1(
                data["compactionMetrics"]
            )
        )
    if "compactionStrategy" in data:
        import aws_sdk_glue.types.compaction_strategy

        out["compaction_strategy"] = (
            aws_sdk_glue.types.compaction_strategy.deserialize_aws_json_1_1(
                data["compactionStrategy"]
            )
        )
    if "retentionMetrics" in data:
        import aws_sdk_glue.types.retention_metrics

        out["retention_metrics"] = (
            aws_sdk_glue.types.retention_metrics.deserialize_aws_json_1_1(
                data["retentionMetrics"]
            )
        )
    if "orphanFileDeletionMetrics" in data:
        import aws_sdk_glue.types.orphan_file_deletion_metrics

        out["orphan_file_deletion_metrics"] = (
            aws_sdk_glue.types.orphan_file_deletion_metrics.deserialize_aws_json_1_1(
                data["orphanFileDeletionMetrics"]
            )
        )
    return out
