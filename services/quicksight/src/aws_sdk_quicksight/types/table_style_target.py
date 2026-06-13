"""Generated from Smithy shape ``com.amazonaws.quicksight#TableStyleTarget``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.styled_cell_type


class TableStyleTarget(TypedDict):
    cell_type: "aws_sdk_quicksight.types.styled_cell_type.StyledCellType"
    """<p>The cell type of the table style target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableStyleTarget) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.styled_cell_type

    out["CellType"] = aws_sdk_quicksight.types.styled_cell_type.serialize_json(
        value["cell_type"]
    )
    return out


def deserialize_json(data: dict) -> TableStyleTarget:
    out: TableStyleTarget = {}  # type: ignore[typeddict-item]
    if "CellType" in data:
        import aws_sdk_quicksight.types.styled_cell_type

        out["cell_type"] = aws_sdk_quicksight.types.styled_cell_type.deserialize_json(
            data["CellType"]
        )
    else:
        raise DeserializationError("TableStyleTarget.cell_type required")
    return out
