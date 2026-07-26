"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionBasedLayoutPaperCanvasSizeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.paper_orientation
    import capo_quicksight.types.paper_size
    import capo_quicksight.types.spacing


class SectionBasedLayoutPaperCanvasSizeOptions(TypedDict, closed=True):
    paper_size: NotRequired["capo_quicksight.types.paper_size.PaperSize"]
    """<p>The paper size that is used to define canvas dimensions.</p>"""
    paper_orientation: NotRequired[
        "capo_quicksight.types.paper_orientation.PaperOrientation"
    ]
    """<p>The paper orientation that is used to define canvas dimensions. Choose one of the following options:</p> <ul> <li> <p>PORTRAIT</p> </li> <li> <p>LANDSCAPE</p> </li> </ul>"""
    paper_margin: NotRequired["capo_quicksight.types.spacing.Spacing"]
    """<p>Defines the spacing between the canvas content and the top, bottom, left, and right edges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SectionBasedLayoutPaperCanvasSizeOptions) -> dict:
    out: dict = {}
    if "paper_size" in value:
        import capo_quicksight.types.paper_size

        out["PaperSize"] = capo_quicksight.types.paper_size.serialize_json(
            value["paper_size"]
        )
    if "paper_orientation" in value:
        import capo_quicksight.types.paper_orientation

        out["PaperOrientation"] = (
            capo_quicksight.types.paper_orientation.serialize_json(
                value["paper_orientation"]
            )
        )
    if "paper_margin" in value:
        import capo_quicksight.types.spacing

        out["PaperMargin"] = capo_quicksight.types.spacing.serialize_json(
            value["paper_margin"]
        )
    return out


def deserialize_json(data: dict) -> SectionBasedLayoutPaperCanvasSizeOptions:
    out: SectionBasedLayoutPaperCanvasSizeOptions = {}  # type: ignore[typeddict-item]
    if "PaperSize" in data:
        import capo_quicksight.types.paper_size

        out["paper_size"] = capo_quicksight.types.paper_size.deserialize_json(
            data["PaperSize"]
        )
    if "PaperOrientation" in data:
        import capo_quicksight.types.paper_orientation

        out["paper_orientation"] = (
            capo_quicksight.types.paper_orientation.deserialize_json(
                data["PaperOrientation"]
            )
        )
    if "PaperMargin" in data:
        import capo_quicksight.types.spacing

        out["paper_margin"] = capo_quicksight.types.spacing.deserialize_json(
            data["PaperMargin"]
        )
    return out
