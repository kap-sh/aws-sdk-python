"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnStatisticsForPartitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.column_errors
    import capo_glue.types.column_statistics_list


class GetColumnStatisticsForPartitionResponse(TypedDict, closed=True):
    column_statistics_list: NotRequired[
        "capo_glue.types.column_statistics_list.ColumnStatisticsList"
    ]
    """<p>List of ColumnStatistics that failed to be retrieved.</p>"""
    errors: NotRequired["capo_glue.types.column_errors.ColumnErrors"]
    """<p>Error occurred during retrieving column statistics data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnStatisticsForPartitionResponse) -> dict:
    out: dict = {}
    if "column_statistics_list" in value:
        import capo_glue.types.column_statistics_list

        out["ColumnStatisticsList"] = (
            capo_glue.types.column_statistics_list.serialize_aws_json_1_1(
                value["column_statistics_list"]
            )
        )
    if "errors" in value:
        import capo_glue.types.column_errors

        out["Errors"] = capo_glue.types.column_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetColumnStatisticsForPartitionResponse:
    out: GetColumnStatisticsForPartitionResponse = {}  # type: ignore[typeddict-item]
    if "ColumnStatisticsList" in data:
        import capo_glue.types.column_statistics_list

        out["column_statistics_list"] = (
            capo_glue.types.column_statistics_list.deserialize_aws_json_1_1(
                data["ColumnStatisticsList"]
            )
        )
    if "Errors" in data:
        import capo_glue.types.column_errors

        out["errors"] = capo_glue.types.column_errors.deserialize_aws_json_1_1(
            data["Errors"]
        )
    return out
