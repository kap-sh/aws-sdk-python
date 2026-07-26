"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ExecutionStats``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.long


class ExecutionStats(TypedDict, closed=True):
    execution_time_in_millis: "capo_timestream_query.types.long.Long"
    """<p>Total time, measured in milliseconds, that was needed for the scheduled query run to complete.</p>"""
    data_writes: "capo_timestream_query.types.long.Long"
    """<p>Data writes metered for records ingested in a single scheduled query run.</p>"""
    bytes_metered: "capo_timestream_query.types.long.Long"
    """<p>Bytes metered for a single scheduled query run.</p>"""
    cumulative_bytes_scanned: "capo_timestream_query.types.long.Long"
    """<p>Bytes scanned for a single scheduled query run.</p>"""
    records_ingested: "capo_timestream_query.types.long.Long"
    """<p>The number of records ingested for a single scheduled query run. </p>"""
    query_result_rows: "capo_timestream_query.types.long.Long"
    """<p>Number of rows present in the output from running a query before ingestion to destination data source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionStats) -> dict:
    out: dict = {}
    out["ExecutionTimeInMillis"] = value.get("execution_time_in_millis", 0)
    out["DataWrites"] = value.get("data_writes", 0)
    out["BytesMetered"] = value.get("bytes_metered", 0)
    out["CumulativeBytesScanned"] = value.get("cumulative_bytes_scanned", 0)
    out["RecordsIngested"] = value.get("records_ingested", 0)
    out["QueryResultRows"] = value.get("query_result_rows", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecutionStats:
    out: ExecutionStats = {}  # type: ignore[typeddict-item]
    if "ExecutionTimeInMillis" in data:
        out["execution_time_in_millis"] = data["ExecutionTimeInMillis"]
    else:
        out["execution_time_in_millis"] = 0
    if "DataWrites" in data:
        out["data_writes"] = data["DataWrites"]
    else:
        out["data_writes"] = 0
    if "BytesMetered" in data:
        out["bytes_metered"] = data["BytesMetered"]
    else:
        out["bytes_metered"] = 0
    if "CumulativeBytesScanned" in data:
        out["cumulative_bytes_scanned"] = data["CumulativeBytesScanned"]
    else:
        out["cumulative_bytes_scanned"] = 0
    if "RecordsIngested" in data:
        out["records_ingested"] = data["RecordsIngested"]
    else:
        out["records_ingested"] = 0
    if "QueryResultRows" in data:
        out["query_result_rows"] = data["QueryResultRows"]
    else:
        out["query_result_rows"] = 0
    return out
