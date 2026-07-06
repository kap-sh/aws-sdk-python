"""Generated from Smithy shape ``com.amazonaws.glue#UpdateColumnStatisticsForPartitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_statistics_errors


class UpdateColumnStatisticsForPartitionResponse(TypedDict, closed=True):
    errors: NotRequired[
        "aws_sdk_glue.types.column_statistics_errors.ColumnStatisticsErrors"
    ]
    """<p>Error occurred during updating column statistics data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateColumnStatisticsForPartitionResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_glue.types.column_statistics_errors

        out["Errors"] = (
            aws_sdk_glue.types.column_statistics_errors.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateColumnStatisticsForPartitionResponse:
    out: UpdateColumnStatisticsForPartitionResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_glue.types.column_statistics_errors

        out["errors"] = (
            aws_sdk_glue.types.column_statistics_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
