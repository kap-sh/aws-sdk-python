"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_statistics
    import aws_sdk_glue.types.error_detail


class ColumnStatisticsError(TypedDict, closed=True):
    column_statistics: NotRequired[
        "aws_sdk_glue.types.column_statistics.ColumnStatistics"
    ]
    """<p>The <code>ColumnStatistics</code> of the column.</p>"""
    error: NotRequired["aws_sdk_glue.types.error_detail.ErrorDetail"]
    """<p>An error message with the reason for the failure of an operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsError) -> dict:
    out: dict = {}
    if "column_statistics" in value:
        import aws_sdk_glue.types.column_statistics

        out["ColumnStatistics"] = (
            aws_sdk_glue.types.column_statistics.serialize_aws_json_1_1(
                value["column_statistics"]
            )
        )
    if "error" in value:
        import aws_sdk_glue.types.error_detail

        out["Error"] = aws_sdk_glue.types.error_detail.serialize_aws_json_1_1(
            value["error"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnStatisticsError:
    out: ColumnStatisticsError = {}  # type: ignore[typeddict-item]
    if "ColumnStatistics" in data:
        import aws_sdk_glue.types.column_statistics

        out["column_statistics"] = (
            aws_sdk_glue.types.column_statistics.deserialize_aws_json_1_1(
                data["ColumnStatistics"]
            )
        )
    if "Error" in data:
        import aws_sdk_glue.types.error_detail

        out["error"] = aws_sdk_glue.types.error_detail.deserialize_aws_json_1_1(
            data["Error"]
        )
    return out
