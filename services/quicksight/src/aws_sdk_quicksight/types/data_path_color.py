"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathColor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_path_value
    import aws_sdk_quicksight.types.hex_color
    import aws_sdk_quicksight.types.time_granularity


class DataPathColor(TypedDict):
    element: "aws_sdk_quicksight.types.data_path_value.DataPathValue"
    """<p>The element that the color needs to be applied to.</p>"""
    color: "aws_sdk_quicksight.types.hex_color.HexColor"
    """<p>The color that needs to be applied to the element.</p>"""
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The time granularity of the field that the color needs to be applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPathColor) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_path_value

    out["Element"] = aws_sdk_quicksight.types.data_path_value.serialize_json(
        value["element"]
    )
    out["Color"] = value["color"]
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataPathColor:
    out: DataPathColor = {}  # type: ignore[typeddict-item]
    if "Element" in data:
        import aws_sdk_quicksight.types.data_path_value

        out["element"] = aws_sdk_quicksight.types.data_path_value.deserialize_json(
            data["Element"]
        )
    else:
        raise DeserializationError("DataPathColor.element required")
    if "Color" in data:
        out["color"] = data["Color"]
    else:
        raise DeserializationError("DataPathColor.color required")
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    return out
