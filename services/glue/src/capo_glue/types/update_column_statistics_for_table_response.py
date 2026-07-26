"""Generated from Smithy shape ``com.amazonaws.glue#UpdateColumnStatisticsForTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.column_statistics_errors


class UpdateColumnStatisticsForTableResponse(TypedDict, closed=True):
    errors: NotRequired[
        "capo_glue.types.column_statistics_errors.ColumnStatisticsErrors"
    ]
    """<p>List of ColumnStatisticsErrors.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateColumnStatisticsForTableResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_glue.types.column_statistics_errors

        out["Errors"] = capo_glue.types.column_statistics_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateColumnStatisticsForTableResponse:
    out: UpdateColumnStatisticsForTableResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import capo_glue.types.column_statistics_errors

        out["errors"] = (
            capo_glue.types.column_statistics_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
