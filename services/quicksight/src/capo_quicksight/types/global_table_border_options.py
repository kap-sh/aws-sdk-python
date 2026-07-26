"""Generated from Smithy shape ``com.amazonaws.quicksight#GlobalTableBorderOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.table_border_options
    import capo_quicksight.types.table_side_border_options


class GlobalTableBorderOptions(TypedDict, closed=True):
    uniform_border: NotRequired[
        "capo_quicksight.types.table_border_options.TableBorderOptions"
    ]
    """<p>Determines the options for uniform border.</p>"""
    side_specific_border: NotRequired[
        "capo_quicksight.types.table_side_border_options.TableSideBorderOptions"
    ]
    """<p>Determines the options for side specific border.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlobalTableBorderOptions) -> dict:
    out: dict = {}
    if "uniform_border" in value:
        import capo_quicksight.types.table_border_options

        out["UniformBorder"] = (
            capo_quicksight.types.table_border_options.serialize_json(
                value["uniform_border"]
            )
        )
    if "side_specific_border" in value:
        import capo_quicksight.types.table_side_border_options

        out["SideSpecificBorder"] = (
            capo_quicksight.types.table_side_border_options.serialize_json(
                value["side_specific_border"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlobalTableBorderOptions:
    out: GlobalTableBorderOptions = {}  # type: ignore[typeddict-item]
    if "UniformBorder" in data:
        import capo_quicksight.types.table_border_options

        out["uniform_border"] = (
            capo_quicksight.types.table_border_options.deserialize_json(
                data["UniformBorder"]
            )
        )
    if "SideSpecificBorder" in data:
        import capo_quicksight.types.table_side_border_options

        out["side_specific_border"] = (
            capo_quicksight.types.table_side_border_options.deserialize_json(
                data["SideSpecificBorder"]
            )
        )
    return out
