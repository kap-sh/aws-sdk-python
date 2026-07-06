"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnStatisticsTaskSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_statistics_task_settings


class GetColumnStatisticsTaskSettingsResponse(TypedDict, closed=True):
    column_statistics_task_settings: NotRequired[
        "aws_sdk_glue.types.column_statistics_task_settings.ColumnStatisticsTaskSettings"
    ]
    """<p>A <code>ColumnStatisticsTaskSettings</code> object representing the settings for the column statistics task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnStatisticsTaskSettingsResponse) -> dict:
    out: dict = {}
    if "column_statistics_task_settings" in value:
        import aws_sdk_glue.types.column_statistics_task_settings

        out["ColumnStatisticsTaskSettings"] = (
            aws_sdk_glue.types.column_statistics_task_settings.serialize_aws_json_1_1(
                value["column_statistics_task_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetColumnStatisticsTaskSettingsResponse:
    out: GetColumnStatisticsTaskSettingsResponse = {}  # type: ignore[typeddict-item]
    if "ColumnStatisticsTaskSettings" in data:
        import aws_sdk_glue.types.column_statistics_task_settings

        out["column_statistics_task_settings"] = (
            aws_sdk_glue.types.column_statistics_task_settings.deserialize_aws_json_1_1(
                data["ColumnStatisticsTaskSettings"]
            )
        )
    return out
