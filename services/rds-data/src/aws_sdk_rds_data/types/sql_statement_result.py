"""Generated from Smithy shape ``com.amazonaws.rdsdata#SqlStatementResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.records_updated
    import aws_sdk_rds_data.types.result_frame


class SqlStatementResult(TypedDict, closed=True):
    result_frame: NotRequired["aws_sdk_rds_data.types.result_frame.ResultFrame"]
    """<p>The result set of the SQL statement.</p>"""
    number_of_records_updated: "aws_sdk_rds_data.types.records_updated.RecordsUpdated"
    """<p>The number of records updated by a SQL statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SqlStatementResult) -> dict:
    out: dict = {}
    if "result_frame" in value:
        import aws_sdk_rds_data.types.result_frame

        out["resultFrame"] = aws_sdk_rds_data.types.result_frame.serialize_json(
            value["result_frame"]
        )
    out["numberOfRecordsUpdated"] = value.get("number_of_records_updated", 0)
    return out


def deserialize_json(data: dict) -> SqlStatementResult:
    out: SqlStatementResult = {}  # type: ignore[typeddict-item]
    if "resultFrame" in data:
        import aws_sdk_rds_data.types.result_frame

        out["result_frame"] = aws_sdk_rds_data.types.result_frame.deserialize_json(
            data["resultFrame"]
        )
    if "numberOfRecordsUpdated" in data:
        out["number_of_records_updated"] = data["numberOfRecordsUpdated"]
    else:
        out["number_of_records_updated"] = 0
    return out
