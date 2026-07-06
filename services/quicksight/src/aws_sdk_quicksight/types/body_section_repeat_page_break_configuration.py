"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionRepeatPageBreakConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.section_after_page_break


class BodySectionRepeatPageBreakConfiguration(TypedDict, closed=True):
    after: NotRequired[
        "aws_sdk_quicksight.types.section_after_page_break.SectionAfterPageBreak"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionRepeatPageBreakConfiguration) -> dict:
    out: dict = {}
    if "after" in value:
        import aws_sdk_quicksight.types.section_after_page_break

        out["After"] = aws_sdk_quicksight.types.section_after_page_break.serialize_json(
            value["after"]
        )
    return out


def deserialize_json(data: dict) -> BodySectionRepeatPageBreakConfiguration:
    out: BodySectionRepeatPageBreakConfiguration = {}  # type: ignore[typeddict-item]
    if "After" in data:
        import aws_sdk_quicksight.types.section_after_page_break

        out["after"] = (
            aws_sdk_quicksight.types.section_after_page_break.deserialize_json(
                data["After"]
            )
        )
    return out
