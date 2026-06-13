"""Generated from Smithy shape ``com.amazonaws.quicksight#TableSideBorderOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_border_options


class TableSideBorderOptions(TypedDict):
    inner_vertical: NotRequired[
        "aws_sdk_quicksight.types.table_border_options.TableBorderOptions"
    ]
    """<p>The table border options of the inner vertical border.</p>"""
    inner_horizontal: NotRequired[
        "aws_sdk_quicksight.types.table_border_options.TableBorderOptions"
    ]
    """<p>The table border options of the inner horizontal border.</p>"""
    left: NotRequired[
        "aws_sdk_quicksight.types.table_border_options.TableBorderOptions"
    ]
    """<p>The table border options of the left border.</p>"""
    right: NotRequired[
        "aws_sdk_quicksight.types.table_border_options.TableBorderOptions"
    ]
    """<p>The table border options of the right border.</p>"""
    top: NotRequired["aws_sdk_quicksight.types.table_border_options.TableBorderOptions"]
    """<p>The table border options of the top border.</p>"""
    bottom: NotRequired[
        "aws_sdk_quicksight.types.table_border_options.TableBorderOptions"
    ]
    """<p>The table border options of the bottom border.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableSideBorderOptions) -> dict:
    out: dict = {}
    if "inner_vertical" in value:
        import aws_sdk_quicksight.types.table_border_options

        out["InnerVertical"] = (
            aws_sdk_quicksight.types.table_border_options.serialize_json(
                value["inner_vertical"]
            )
        )
    if "inner_horizontal" in value:
        import aws_sdk_quicksight.types.table_border_options

        out["InnerHorizontal"] = (
            aws_sdk_quicksight.types.table_border_options.serialize_json(
                value["inner_horizontal"]
            )
        )
    if "left" in value:
        import aws_sdk_quicksight.types.table_border_options

        out["Left"] = aws_sdk_quicksight.types.table_border_options.serialize_json(
            value["left"]
        )
    if "right" in value:
        import aws_sdk_quicksight.types.table_border_options

        out["Right"] = aws_sdk_quicksight.types.table_border_options.serialize_json(
            value["right"]
        )
    if "top" in value:
        import aws_sdk_quicksight.types.table_border_options

        out["Top"] = aws_sdk_quicksight.types.table_border_options.serialize_json(
            value["top"]
        )
    if "bottom" in value:
        import aws_sdk_quicksight.types.table_border_options

        out["Bottom"] = aws_sdk_quicksight.types.table_border_options.serialize_json(
            value["bottom"]
        )
    return out


def deserialize_json(data: dict) -> TableSideBorderOptions:
    out: TableSideBorderOptions = {}  # type: ignore[typeddict-item]
    if "InnerVertical" in data:
        import aws_sdk_quicksight.types.table_border_options

        out["inner_vertical"] = (
            aws_sdk_quicksight.types.table_border_options.deserialize_json(
                data["InnerVertical"]
            )
        )
    if "InnerHorizontal" in data:
        import aws_sdk_quicksight.types.table_border_options

        out["inner_horizontal"] = (
            aws_sdk_quicksight.types.table_border_options.deserialize_json(
                data["InnerHorizontal"]
            )
        )
    if "Left" in data:
        import aws_sdk_quicksight.types.table_border_options

        out["left"] = aws_sdk_quicksight.types.table_border_options.deserialize_json(
            data["Left"]
        )
    if "Right" in data:
        import aws_sdk_quicksight.types.table_border_options

        out["right"] = aws_sdk_quicksight.types.table_border_options.deserialize_json(
            data["Right"]
        )
    if "Top" in data:
        import aws_sdk_quicksight.types.table_border_options

        out["top"] = aws_sdk_quicksight.types.table_border_options.deserialize_json(
            data["Top"]
        )
    if "Bottom" in data:
        import aws_sdk_quicksight.types.table_border_options

        out["bottom"] = aws_sdk_quicksight.types.table_border_options.deserialize_json(
            data["Bottom"]
        )
    return out
