"""Generated from Smithy shape ``com.amazonaws.quicksight#LookbackWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.lookback_window_size_unit
    import aws_sdk_quicksight.types.positive_long
    import aws_sdk_quicksight.types.string


class LookbackWindow(TypedDict, closed=True):
    column_name: "aws_sdk_quicksight.types.string.String"
    """<p>The name of the lookback window column.</p>"""
    size: "aws_sdk_quicksight.types.positive_long.PositiveLong"
    """<p>The lookback window column size.</p>"""
    size_unit: (
        "aws_sdk_quicksight.types.lookback_window_size_unit.LookbackWindowSizeUnit"
    )
    """<p>The size unit that is used for the lookback window column. Valid values for this structure are <code>HOUR</code>, <code>DAY</code>, and <code>WEEK</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LookbackWindow) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    out["Size"] = value["size"]
    import aws_sdk_quicksight.types.lookback_window_size_unit

    out["SizeUnit"] = aws_sdk_quicksight.types.lookback_window_size_unit.serialize_json(
        value["size_unit"]
    )
    return out


def deserialize_json(data: dict) -> LookbackWindow:
    out: LookbackWindow = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("LookbackWindow.column_name required")
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        raise DeserializationError("LookbackWindow.size required")
    if "SizeUnit" in data:
        import aws_sdk_quicksight.types.lookback_window_size_unit

        out["size_unit"] = (
            aws_sdk_quicksight.types.lookback_window_size_unit.deserialize_json(
                data["SizeUnit"]
            )
        )
    else:
        raise DeserializationError("LookbackWindow.size_unit required")
    return out
