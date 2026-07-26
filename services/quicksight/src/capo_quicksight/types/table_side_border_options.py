"""Generated from Smithy shape ``com.amazonaws.quicksight#TableSideBorderOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.table_border_options


class TableSideBorderOptions(TypedDict, closed=True):
    inner_vertical: NotRequired[
        "capo_quicksight.types.table_border_options.TableBorderOptions"
    ]
    """<p>The table border options of the inner vertical border.</p>"""
    inner_horizontal: NotRequired[
        "capo_quicksight.types.table_border_options.TableBorderOptions"
    ]
    """<p>The table border options of the inner horizontal border.</p>"""
    left: NotRequired["capo_quicksight.types.table_border_options.TableBorderOptions"]
    """<p>The table border options of the left border.</p>"""
    right: NotRequired["capo_quicksight.types.table_border_options.TableBorderOptions"]
    """<p>The table border options of the right border.</p>"""
    top: NotRequired["capo_quicksight.types.table_border_options.TableBorderOptions"]
    """<p>The table border options of the top border.</p>"""
    bottom: NotRequired["capo_quicksight.types.table_border_options.TableBorderOptions"]
    """<p>The table border options of the bottom border.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableSideBorderOptions) -> dict:
    out: dict = {}
    if "inner_vertical" in value:
        import capo_quicksight.types.table_border_options

        out["InnerVertical"] = (
            capo_quicksight.types.table_border_options.serialize_json(
                value["inner_vertical"]
            )
        )
    if "inner_horizontal" in value:
        import capo_quicksight.types.table_border_options

        out["InnerHorizontal"] = (
            capo_quicksight.types.table_border_options.serialize_json(
                value["inner_horizontal"]
            )
        )
    if "left" in value:
        import capo_quicksight.types.table_border_options

        out["Left"] = capo_quicksight.types.table_border_options.serialize_json(
            value["left"]
        )
    if "right" in value:
        import capo_quicksight.types.table_border_options

        out["Right"] = capo_quicksight.types.table_border_options.serialize_json(
            value["right"]
        )
    if "top" in value:
        import capo_quicksight.types.table_border_options

        out["Top"] = capo_quicksight.types.table_border_options.serialize_json(
            value["top"]
        )
    if "bottom" in value:
        import capo_quicksight.types.table_border_options

        out["Bottom"] = capo_quicksight.types.table_border_options.serialize_json(
            value["bottom"]
        )
    return out


def deserialize_json(data: dict) -> TableSideBorderOptions:
    out: TableSideBorderOptions = {}  # type: ignore[typeddict-item]
    if "InnerVertical" in data:
        import capo_quicksight.types.table_border_options

        out["inner_vertical"] = (
            capo_quicksight.types.table_border_options.deserialize_json(
                data["InnerVertical"]
            )
        )
    if "InnerHorizontal" in data:
        import capo_quicksight.types.table_border_options

        out["inner_horizontal"] = (
            capo_quicksight.types.table_border_options.deserialize_json(
                data["InnerHorizontal"]
            )
        )
    if "Left" in data:
        import capo_quicksight.types.table_border_options

        out["left"] = capo_quicksight.types.table_border_options.deserialize_json(
            data["Left"]
        )
    if "Right" in data:
        import capo_quicksight.types.table_border_options

        out["right"] = capo_quicksight.types.table_border_options.deserialize_json(
            data["Right"]
        )
    if "Top" in data:
        import capo_quicksight.types.table_border_options

        out["top"] = capo_quicksight.types.table_border_options.deserialize_json(
            data["Top"]
        )
    if "Bottom" in data:
        import capo_quicksight.types.table_border_options

        out["bottom"] = capo_quicksight.types.table_border_options.deserialize_json(
            data["Bottom"]
        )
    return out
