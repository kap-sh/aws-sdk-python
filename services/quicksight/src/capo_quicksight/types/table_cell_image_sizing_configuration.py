"""Generated from Smithy shape ``com.amazonaws.quicksight#TableCellImageSizingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.table_cell_image_scaling_configuration


class TableCellImageSizingConfiguration(TypedDict, closed=True):
    table_cell_image_scaling_configuration: NotRequired[
        "capo_quicksight.types.table_cell_image_scaling_configuration.TableCellImageScalingConfiguration"
    ]
    """<p>The cell scaling configuration of the sizing options for the table image configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableCellImageSizingConfiguration) -> dict:
    out: dict = {}
    if "table_cell_image_scaling_configuration" in value:
        import capo_quicksight.types.table_cell_image_scaling_configuration

        out["TableCellImageScalingConfiguration"] = (
            capo_quicksight.types.table_cell_image_scaling_configuration.serialize_json(
                value["table_cell_image_scaling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableCellImageSizingConfiguration:
    out: TableCellImageSizingConfiguration = {}  # type: ignore[typeddict-item]
    if "TableCellImageScalingConfiguration" in data:
        import capo_quicksight.types.table_cell_image_scaling_configuration

        out["table_cell_image_scaling_configuration"] = (
            capo_quicksight.types.table_cell_image_scaling_configuration.deserialize_json(
                data["TableCellImageScalingConfiguration"]
            )
        )
    return out
