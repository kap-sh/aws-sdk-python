"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#BatchLoadProgressReport``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.long


class BatchLoadProgressReport(TypedDict, closed=True):
    records_processed: "aws_sdk_timestream_write.types.long.Long"
    """<p></p>"""
    records_ingested: "aws_sdk_timestream_write.types.long.Long"
    """<p></p>"""
    parse_failures: "aws_sdk_timestream_write.types.long.Long"
    """<p></p>"""
    record_ingestion_failures: "aws_sdk_timestream_write.types.long.Long"
    """<p></p>"""
    file_failures: "aws_sdk_timestream_write.types.long.Long"
    """<p></p>"""
    bytes_metered: "aws_sdk_timestream_write.types.long.Long"
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchLoadProgressReport) -> dict:
    out: dict = {}
    out["RecordsProcessed"] = value.get("records_processed", 0)
    out["RecordsIngested"] = value.get("records_ingested", 0)
    out["ParseFailures"] = value.get("parse_failures", 0)
    out["RecordIngestionFailures"] = value.get("record_ingestion_failures", 0)
    out["FileFailures"] = value.get("file_failures", 0)
    out["BytesMetered"] = value.get("bytes_metered", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchLoadProgressReport:
    out: BatchLoadProgressReport = {}  # type: ignore[typeddict-item]
    if "RecordsProcessed" in data:
        out["records_processed"] = data["RecordsProcessed"]
    else:
        out["records_processed"] = 0
    if "RecordsIngested" in data:
        out["records_ingested"] = data["RecordsIngested"]
    else:
        out["records_ingested"] = 0
    if "ParseFailures" in data:
        out["parse_failures"] = data["ParseFailures"]
    else:
        out["parse_failures"] = 0
    if "RecordIngestionFailures" in data:
        out["record_ingestion_failures"] = data["RecordIngestionFailures"]
    else:
        out["record_ingestion_failures"] = 0
    if "FileFailures" in data:
        out["file_failures"] = data["FileFailures"]
    else:
        out["file_failures"] = 0
    if "BytesMetered" in data:
        out["bytes_metered"] = data["BytesMetered"]
    else:
        out["bytes_metered"] = 0
    return out
