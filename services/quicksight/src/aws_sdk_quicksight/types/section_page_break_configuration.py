"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionPageBreakConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.section_after_page_break


class SectionPageBreakConfiguration(TypedDict):
    after: NotRequired[
        "aws_sdk_quicksight.types.section_after_page_break.SectionAfterPageBreak"
    ]
    """<p>The configuration of a page break after a section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SectionPageBreakConfiguration) -> dict:
    out: dict = {}
    if "after" in value:
        import aws_sdk_quicksight.types.section_after_page_break

        out["After"] = aws_sdk_quicksight.types.section_after_page_break.serialize_json(
            value["after"]
        )
    return out


def deserialize_json(data: dict) -> SectionPageBreakConfiguration:
    out: SectionPageBreakConfiguration = {}  # type: ignore[typeddict-item]
    if "After" in data:
        import aws_sdk_quicksight.types.section_after_page_break

        out["after"] = (
            aws_sdk_quicksight.types.section_after_page_break.deserialize_json(
                data["After"]
            )
        )
    return out
