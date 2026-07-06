"""Generated from Smithy shape ``com.amazonaws.quicksight#DataAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.topic_time_granularity


class DataAggregation(TypedDict, closed=True):
    dataset_row_date_granularity: NotRequired[
        "aws_sdk_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    default_date_column_name: NotRequired[
        "aws_sdk_quicksight.types.limited_string.LimitedString"
    ]
    """<p>The column name for the default date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataAggregation) -> dict:
    out: dict = {}
    if "dataset_row_date_granularity" in value:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["DatasetRowDateGranularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.serialize_json(
                value["dataset_row_date_granularity"]
            )
        )
    if "default_date_column_name" in value:
        out["DefaultDateColumnName"] = value["default_date_column_name"]
    return out


def deserialize_json(data: dict) -> DataAggregation:
    out: DataAggregation = {}  # type: ignore[typeddict-item]
    if "DatasetRowDateGranularity" in data:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["dataset_row_date_granularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.deserialize_json(
                data["DatasetRowDateGranularity"]
            )
        )
    if "DefaultDateColumnName" in data:
        out["default_date_column_name"] = data["DefaultDateColumnName"]
    return out
