"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.grid_layout_canvas_size_options
    import aws_sdk_quicksight.types.grid_layout_element_list


class GridLayoutConfiguration(TypedDict):
    elements: "aws_sdk_quicksight.types.grid_layout_element_list.GridLayoutElementList"
    """<p>The elements that are included in a grid layout.</p>"""
    canvas_size_options: NotRequired[
        "aws_sdk_quicksight.types.grid_layout_canvas_size_options.GridLayoutCanvasSizeOptions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.grid_layout_element_list

    out["Elements"] = aws_sdk_quicksight.types.grid_layout_element_list.serialize_json(
        value["elements"]
    )
    if "canvas_size_options" in value:
        import aws_sdk_quicksight.types.grid_layout_canvas_size_options

        out["CanvasSizeOptions"] = (
            aws_sdk_quicksight.types.grid_layout_canvas_size_options.serialize_json(
                value["canvas_size_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> GridLayoutConfiguration:
    out: GridLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "Elements" in data:
        import aws_sdk_quicksight.types.grid_layout_element_list

        out["elements"] = (
            aws_sdk_quicksight.types.grid_layout_element_list.deserialize_json(
                data["Elements"]
            )
        )
    else:
        raise DeserializationError("GridLayoutConfiguration.elements required")
    if "CanvasSizeOptions" in data:
        import aws_sdk_quicksight.types.grid_layout_canvas_size_options

        out["canvas_size_options"] = (
            aws_sdk_quicksight.types.grid_layout_canvas_size_options.deserialize_json(
                data["CanvasSizeOptions"]
            )
        )
    return out
