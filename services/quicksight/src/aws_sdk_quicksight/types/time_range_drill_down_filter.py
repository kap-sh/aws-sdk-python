"""Generated from Smithy shape ``com.amazonaws.quicksight#TimeRangeDrillDownFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.time_granularity
    import aws_sdk_quicksight.types.timestamp


class TimeRangeDrillDownFilter(TypedDict, closed=True):
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    range_minimum: "aws_sdk_quicksight.types.timestamp.Timestamp"
    """<p>The minimum value for the filter value range.</p>"""
    range_maximum: "aws_sdk_quicksight.types.timestamp.Timestamp"
    """<p>The maximum value for the filter value range.</p>"""
    time_granularity: "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeRangeDrillDownFilter) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import aws_sdk_quicksight.types.timestamp

    out["RangeMinimum"] = aws_sdk_quicksight.types.timestamp.serialize_json(
        value["range_minimum"]
    )
    import aws_sdk_quicksight.types.timestamp

    out["RangeMaximum"] = aws_sdk_quicksight.types.timestamp.serialize_json(
        value["range_maximum"]
    )
    import aws_sdk_quicksight.types.time_granularity

    out["TimeGranularity"] = aws_sdk_quicksight.types.time_granularity.serialize_json(
        value["time_granularity"]
    )
    return out


def deserialize_json(data: dict) -> TimeRangeDrillDownFilter:
    out: TimeRangeDrillDownFilter = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("TimeRangeDrillDownFilter.column required")
    if "RangeMinimum" in data:
        import aws_sdk_quicksight.types.timestamp

        out["range_minimum"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["RangeMinimum"]
        )
    else:
        raise DeserializationError("TimeRangeDrillDownFilter.range_minimum required")
    if "RangeMaximum" in data:
        import aws_sdk_quicksight.types.timestamp

        out["range_maximum"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["RangeMaximum"]
        )
    else:
        raise DeserializationError("TimeRangeDrillDownFilter.range_maximum required")
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    else:
        raise DeserializationError("TimeRangeDrillDownFilter.time_granularity required")
    return out
