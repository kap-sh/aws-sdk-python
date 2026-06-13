"""Generated from Smithy shape ``com.amazonaws.quicksight#TableCellImageSizingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_cell_image_scaling_configuration


class TableCellImageSizingConfiguration(TypedDict):
    table_cell_image_scaling_configuration: NotRequired[
        "aws_sdk_quicksight.types.table_cell_image_scaling_configuration.TableCellImageScalingConfiguration"
    ]
    """<p>The cell scaling configuration of the sizing options for the table image configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableCellImageSizingConfiguration) -> dict:
    out: dict = {}
    if "table_cell_image_scaling_configuration" in value:
        import aws_sdk_quicksight.types.table_cell_image_scaling_configuration

        out["TableCellImageScalingConfiguration"] = (
            aws_sdk_quicksight.types.table_cell_image_scaling_configuration.serialize_json(
                value["table_cell_image_scaling_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableCellImageSizingConfiguration:
    out: TableCellImageSizingConfiguration = {}  # type: ignore[typeddict-item]
    if "TableCellImageScalingConfiguration" in data:
        import aws_sdk_quicksight.types.table_cell_image_scaling_configuration

        out["table_cell_image_scaling_configuration"] = (
            aws_sdk_quicksight.types.table_cell_image_scaling_configuration.deserialize_json(
                data["TableCellImageScalingConfiguration"]
            )
        )
    return out
