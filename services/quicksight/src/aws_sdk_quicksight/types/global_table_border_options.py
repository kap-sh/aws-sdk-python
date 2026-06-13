"""Generated from Smithy shape ``com.amazonaws.quicksight#GlobalTableBorderOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_border_options
    import aws_sdk_quicksight.types.table_side_border_options


class GlobalTableBorderOptions(TypedDict):
    uniform_border: NotRequired[
        "aws_sdk_quicksight.types.table_border_options.TableBorderOptions"
    ]
    """<p>Determines the options for uniform border.</p>"""
    side_specific_border: NotRequired[
        "aws_sdk_quicksight.types.table_side_border_options.TableSideBorderOptions"
    ]
    """<p>Determines the options for side specific border.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlobalTableBorderOptions) -> dict:
    out: dict = {}
    if "uniform_border" in value:
        import aws_sdk_quicksight.types.table_border_options

        out["UniformBorder"] = (
            aws_sdk_quicksight.types.table_border_options.serialize_json(
                value["uniform_border"]
            )
        )
    if "side_specific_border" in value:
        import aws_sdk_quicksight.types.table_side_border_options

        out["SideSpecificBorder"] = (
            aws_sdk_quicksight.types.table_side_border_options.serialize_json(
                value["side_specific_border"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlobalTableBorderOptions:
    out: GlobalTableBorderOptions = {}  # type: ignore[typeddict-item]
    if "UniformBorder" in data:
        import aws_sdk_quicksight.types.table_border_options

        out["uniform_border"] = (
            aws_sdk_quicksight.types.table_border_options.deserialize_json(
                data["UniformBorder"]
            )
        )
    if "SideSpecificBorder" in data:
        import aws_sdk_quicksight.types.table_side_border_options

        out["side_specific_border"] = (
            aws_sdk_quicksight.types.table_side_border_options.deserialize_json(
                data["SideSpecificBorder"]
            )
        )
    return out
