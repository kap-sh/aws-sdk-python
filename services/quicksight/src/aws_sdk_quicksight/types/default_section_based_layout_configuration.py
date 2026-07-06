"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultSectionBasedLayoutConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.section_based_layout_canvas_size_options


class DefaultSectionBasedLayoutConfiguration(TypedDict, closed=True):
    canvas_size_options: "aws_sdk_quicksight.types.section_based_layout_canvas_size_options.SectionBasedLayoutCanvasSizeOptions"
    """<p>Determines the screen canvas size options for a section-based layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultSectionBasedLayoutConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.section_based_layout_canvas_size_options

    out["CanvasSizeOptions"] = (
        aws_sdk_quicksight.types.section_based_layout_canvas_size_options.serialize_json(
            value["canvas_size_options"]
        )
    )
    return out


def deserialize_json(data: dict) -> DefaultSectionBasedLayoutConfiguration:
    out: DefaultSectionBasedLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "CanvasSizeOptions" in data:
        import aws_sdk_quicksight.types.section_based_layout_canvas_size_options

        out["canvas_size_options"] = (
            aws_sdk_quicksight.types.section_based_layout_canvas_size_options.deserialize_json(
                data["CanvasSizeOptions"]
            )
        )
    else:
        raise DeserializationError(
            "DefaultSectionBasedLayoutConfiguration.canvas_size_options required"
        )
    return out
