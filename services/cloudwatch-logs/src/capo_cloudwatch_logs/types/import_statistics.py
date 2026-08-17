"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.stored_bytes


class ImportStatistics(TypedDict, closed=True):
    bytes_imported: NotRequired["capo_cloudwatch_logs.types.stored_bytes.StoredBytes"]
    """<p>The total number of bytes that have been imported to the managed log group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportStatistics) -> dict:
    out: dict = {}
    if "bytes_imported" in value:
        out["bytesImported"] = value["bytes_imported"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportStatistics:
    out: ImportStatistics = {}  # type: ignore[typeddict-item]
    if data.get("bytesImported") is not None:
        out["bytes_imported"] = data["bytesImported"]
    return out
