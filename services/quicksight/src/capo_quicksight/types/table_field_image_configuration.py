"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldImageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.table_cell_image_sizing_configuration


class TableFieldImageConfiguration(TypedDict, closed=True):
    sizing_options: NotRequired[
        "capo_quicksight.types.table_cell_image_sizing_configuration.TableCellImageSizingConfiguration"
    ]
    """<p>The sizing options for the table image configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldImageConfiguration) -> dict:
    out: dict = {}
    if "sizing_options" in value:
        import capo_quicksight.types.table_cell_image_sizing_configuration

        out["SizingOptions"] = (
            capo_quicksight.types.table_cell_image_sizing_configuration.serialize_json(
                value["sizing_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableFieldImageConfiguration:
    out: TableFieldImageConfiguration = {}  # type: ignore[typeddict-item]
    if "SizingOptions" in data:
        import capo_quicksight.types.table_cell_image_sizing_configuration

        out["sizing_options"] = (
            capo_quicksight.types.table_cell_image_sizing_configuration.deserialize_json(
                data["SizingOptions"]
            )
        )
    return out
