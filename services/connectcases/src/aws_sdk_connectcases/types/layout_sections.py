"""Generated from Smithy shape ``com.amazonaws.connectcases#LayoutSections``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.sections_list


class LayoutSections(TypedDict):
    sections: NotRequired["aws_sdk_connectcases.types.sections_list.SectionsList"]


# --- restJson1 ser/de ---
def serialize_json(value: LayoutSections) -> dict:
    out: dict = {}
    if "sections" in value:
        import aws_sdk_connectcases.types.sections_list

        out["sections"] = aws_sdk_connectcases.types.sections_list.serialize_json(
            value["sections"]
        )
    return out


def deserialize_json(data: dict) -> LayoutSections:
    out: LayoutSections = {}  # type: ignore[typeddict-item]
    if "sections" in data:
        import aws_sdk_connectcases.types.sections_list

        out["sections"] = aws_sdk_connectcases.types.sections_list.deserialize_json(
            data["sections"]
        )
    return out
