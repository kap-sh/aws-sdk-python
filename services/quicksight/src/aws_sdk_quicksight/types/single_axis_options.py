"""Generated from Smithy shape ``com.amazonaws.quicksight#SingleAxisOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.y_axis_options


class SingleAxisOptions(TypedDict, closed=True):
    y_axis_options: NotRequired["aws_sdk_quicksight.types.y_axis_options.YAxisOptions"]
    """<p>The Y axis options of a single axis configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleAxisOptions) -> dict:
    out: dict = {}
    if "y_axis_options" in value:
        import aws_sdk_quicksight.types.y_axis_options

        out["YAxisOptions"] = aws_sdk_quicksight.types.y_axis_options.serialize_json(
            value["y_axis_options"]
        )
    return out


def deserialize_json(data: dict) -> SingleAxisOptions:
    out: SingleAxisOptions = {}  # type: ignore[typeddict-item]
    if "YAxisOptions" in data:
        import aws_sdk_quicksight.types.y_axis_options

        out["y_axis_options"] = (
            aws_sdk_quicksight.types.y_axis_options.deserialize_json(
                data["YAxisOptions"]
            )
        )
    return out
