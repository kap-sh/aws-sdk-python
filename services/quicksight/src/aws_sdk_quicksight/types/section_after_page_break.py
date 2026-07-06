"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionAfterPageBreak``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.section_page_break_status


class SectionAfterPageBreak(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_quicksight.types.section_page_break_status.SectionPageBreakStatus"
    ]
    """<p>The option that enables or disables a page break at the end of a section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SectionAfterPageBreak) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_quicksight.types.section_page_break_status

        out["Status"] = (
            aws_sdk_quicksight.types.section_page_break_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SectionAfterPageBreak:
    out: SectionAfterPageBreak = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_quicksight.types.section_page_break_status

        out["status"] = (
            aws_sdk_quicksight.types.section_page_break_status.deserialize_json(
                data["Status"]
            )
        )
    return out
