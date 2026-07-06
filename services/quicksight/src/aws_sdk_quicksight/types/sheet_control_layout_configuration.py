"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlLayoutConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.grid_layout_configuration


class SheetControlLayoutConfiguration(TypedDict, closed=True):
    grid_layout: NotRequired[
        "aws_sdk_quicksight.types.grid_layout_configuration.GridLayoutConfiguration"
    ]
    """<p>The configuration that determines the elements and canvas size options of sheet control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlLayoutConfiguration) -> dict:
    out: dict = {}
    if "grid_layout" in value:
        import aws_sdk_quicksight.types.grid_layout_configuration

        out["GridLayout"] = (
            aws_sdk_quicksight.types.grid_layout_configuration.serialize_json(
                value["grid_layout"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetControlLayoutConfiguration:
    out: SheetControlLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "GridLayout" in data:
        import aws_sdk_quicksight.types.grid_layout_configuration

        out["grid_layout"] = (
            aws_sdk_quicksight.types.grid_layout_configuration.deserialize_json(
                data["GridLayout"]
            )
        )
    return out
