"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.exported_records_count
    import aws_sdk_sesv2.types.processed_records_count


class ExportStatistics(TypedDict):
    processed_records_count: NotRequired[
        "aws_sdk_sesv2.types.processed_records_count.ProcessedRecordsCount"
    ]
    """<p>The number of records that were processed to generate the final export file.</p>"""
    exported_records_count: NotRequired[
        "aws_sdk_sesv2.types.exported_records_count.ExportedRecordsCount"
    ]
    """<p>The number of records that were exported to the final export file.</p> <p>This value might not be available for all export source types</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportStatistics) -> dict:
    out: dict = {}
    if "processed_records_count" in value:
        out["ProcessedRecordsCount"] = value["processed_records_count"]
    if "exported_records_count" in value:
        out["ExportedRecordsCount"] = value["exported_records_count"]
    return out


def deserialize_json(data: dict) -> ExportStatistics:
    out: ExportStatistics = {}  # type: ignore[typeddict-item]
    if "ProcessedRecordsCount" in data:
        out["processed_records_count"] = data["ProcessedRecordsCount"]
    if "ExportedRecordsCount" in data:
        out["exported_records_count"] = data["ExportedRecordsCount"]
    return out
