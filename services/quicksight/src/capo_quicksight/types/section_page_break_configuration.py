"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionPageBreakConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.section_after_page_break


class SectionPageBreakConfiguration(TypedDict, closed=True):
    after: NotRequired[
        "capo_quicksight.types.section_after_page_break.SectionAfterPageBreak"
    ]
    """<p>The configuration of a page break after a section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SectionPageBreakConfiguration) -> dict:
    out: dict = {}
    if "after" in value:
        import capo_quicksight.types.section_after_page_break

        out["After"] = capo_quicksight.types.section_after_page_break.serialize_json(
            value["after"]
        )
    return out


def deserialize_json(data: dict) -> SectionPageBreakConfiguration:
    out: SectionPageBreakConfiguration = {}  # type: ignore[typeddict-item]
    if "After" in data:
        import capo_quicksight.types.section_after_page_break

        out["after"] = capo_quicksight.types.section_after_page_break.deserialize_json(
            data["After"]
        )
    return out
