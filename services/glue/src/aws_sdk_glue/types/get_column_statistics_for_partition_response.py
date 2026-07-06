"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnStatisticsForPartitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_errors
    import aws_sdk_glue.types.column_statistics_list


class GetColumnStatisticsForPartitionResponse(TypedDict, closed=True):
    column_statistics_list: NotRequired[
        "aws_sdk_glue.types.column_statistics_list.ColumnStatisticsList"
    ]
    """<p>List of ColumnStatistics that failed to be retrieved.</p>"""
    errors: NotRequired["aws_sdk_glue.types.column_errors.ColumnErrors"]
    """<p>Error occurred during retrieving column statistics data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnStatisticsForPartitionResponse) -> dict:
    out: dict = {}
    if "column_statistics_list" in value:
        import aws_sdk_glue.types.column_statistics_list

        out["ColumnStatisticsList"] = (
            aws_sdk_glue.types.column_statistics_list.serialize_aws_json_1_1(
                value["column_statistics_list"]
            )
        )
    if "errors" in value:
        import aws_sdk_glue.types.column_errors

        out["Errors"] = aws_sdk_glue.types.column_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetColumnStatisticsForPartitionResponse:
    out: GetColumnStatisticsForPartitionResponse = {}  # type: ignore[typeddict-item]
    if "ColumnStatisticsList" in data:
        import aws_sdk_glue.types.column_statistics_list

        out["column_statistics_list"] = (
            aws_sdk_glue.types.column_statistics_list.deserialize_aws_json_1_1(
                data["ColumnStatisticsList"]
            )
        )
    if "Errors" in data:
        import aws_sdk_glue.types.column_errors

        out["errors"] = aws_sdk_glue.types.column_errors.deserialize_aws_json_1_1(
            data["Errors"]
        )
    return out
