"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultFreeFormLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.free_form_layout_canvas_size_options


class DefaultFreeFormLayoutConfiguration(TypedDict):
    canvas_size_options: "aws_sdk_quicksight.types.free_form_layout_canvas_size_options.FreeFormLayoutCanvasSizeOptions"
    """<p>Determines the screen canvas size options for a free-form layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultFreeFormLayoutConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.free_form_layout_canvas_size_options

    out["CanvasSizeOptions"] = (
        aws_sdk_quicksight.types.free_form_layout_canvas_size_options.serialize_json(
            value["canvas_size_options"]
        )
    )
    return out


def deserialize_json(data: dict) -> DefaultFreeFormLayoutConfiguration:
    out: DefaultFreeFormLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "CanvasSizeOptions" in data:
        import aws_sdk_quicksight.types.free_form_layout_canvas_size_options

        out["canvas_size_options"] = (
            aws_sdk_quicksight.types.free_form_layout_canvas_size_options.deserialize_json(
                data["CanvasSizeOptions"]
            )
        )
    else:
        raise DeserializationError(
            "DefaultFreeFormLayoutConfiguration.canvas_size_options required"
        )
    return out
