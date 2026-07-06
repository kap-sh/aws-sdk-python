"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.section_layout_configuration


class BodySectionContent(TypedDict, closed=True):
    layout: NotRequired[
        "aws_sdk_quicksight.types.section_layout_configuration.SectionLayoutConfiguration"
    ]
    """<p>The layout configuration of a body section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionContent) -> dict:
    out: dict = {}
    if "layout" in value:
        import aws_sdk_quicksight.types.section_layout_configuration

        out["Layout"] = (
            aws_sdk_quicksight.types.section_layout_configuration.serialize_json(
                value["layout"]
            )
        )
    return out


def deserialize_json(data: dict) -> BodySectionContent:
    out: BodySectionContent = {}  # type: ignore[typeddict-item]
    if "Layout" in data:
        import aws_sdk_quicksight.types.section_layout_configuration

        out["layout"] = (
            aws_sdk_quicksight.types.section_layout_configuration.deserialize_json(
                data["Layout"]
            )
        )
    return out
