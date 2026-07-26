"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionBasedLayoutCanvasSizeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.section_based_layout_paper_canvas_size_options


class SectionBasedLayoutCanvasSizeOptions(TypedDict, closed=True):
    paper_canvas_size_options: NotRequired[
        "capo_quicksight.types.section_based_layout_paper_canvas_size_options.SectionBasedLayoutPaperCanvasSizeOptions"
    ]
    """<p>The options for a paper canvas of a section-based layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SectionBasedLayoutCanvasSizeOptions) -> dict:
    out: dict = {}
    if "paper_canvas_size_options" in value:
        import capo_quicksight.types.section_based_layout_paper_canvas_size_options

        out["PaperCanvasSizeOptions"] = (
            capo_quicksight.types.section_based_layout_paper_canvas_size_options.serialize_json(
                value["paper_canvas_size_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> SectionBasedLayoutCanvasSizeOptions:
    out: SectionBasedLayoutCanvasSizeOptions = {}  # type: ignore[typeddict-item]
    if "PaperCanvasSizeOptions" in data:
        import capo_quicksight.types.section_based_layout_paper_canvas_size_options

        out["paper_canvas_size_options"] = (
            capo_quicksight.types.section_based_layout_paper_canvas_size_options.deserialize_json(
                data["PaperCanvasSizeOptions"]
            )
        )
    return out
