"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.body_section_content
    import aws_sdk_quicksight.types.body_section_repeat_configuration
    import aws_sdk_quicksight.types.section_page_break_configuration
    import aws_sdk_quicksight.types.section_style
    import aws_sdk_quicksight.types.short_restrictive_resource_id


class BodySectionConfiguration(TypedDict, closed=True):
    section_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of a body section.</p>"""
    content: "aws_sdk_quicksight.types.body_section_content.BodySectionContent"
    """<p>The configuration of content in a body section.</p>"""
    style: NotRequired["aws_sdk_quicksight.types.section_style.SectionStyle"]
    """<p>The style options of a body section.</p>"""
    page_break_configuration: NotRequired[
        "aws_sdk_quicksight.types.section_page_break_configuration.SectionPageBreakConfiguration"
    ]
    """<p>The configuration of a page break for a section.</p>"""
    repeat_configuration: NotRequired[
        "aws_sdk_quicksight.types.body_section_repeat_configuration.BodySectionRepeatConfiguration"
    ]
    """<p>Describes the configurations that are required to declare a section as repeating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionConfiguration) -> dict:
    out: dict = {}
    out["SectionId"] = value["section_id"]
    import aws_sdk_quicksight.types.body_section_content

    out["Content"] = aws_sdk_quicksight.types.body_section_content.serialize_json(
        value["content"]
    )
    if "style" in value:
        import aws_sdk_quicksight.types.section_style

        out["Style"] = aws_sdk_quicksight.types.section_style.serialize_json(
            value["style"]
        )
    if "page_break_configuration" in value:
        import aws_sdk_quicksight.types.section_page_break_configuration

        out["PageBreakConfiguration"] = (
            aws_sdk_quicksight.types.section_page_break_configuration.serialize_json(
                value["page_break_configuration"]
            )
        )
    if "repeat_configuration" in value:
        import aws_sdk_quicksight.types.body_section_repeat_configuration

        out["RepeatConfiguration"] = (
            aws_sdk_quicksight.types.body_section_repeat_configuration.serialize_json(
                value["repeat_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BodySectionConfiguration:
    out: BodySectionConfiguration = {}  # type: ignore[typeddict-item]
    if "SectionId" in data:
        out["section_id"] = data["SectionId"]
    else:
        raise DeserializationError("BodySectionConfiguration.section_id required")
    if "Content" in data:
        import aws_sdk_quicksight.types.body_section_content

        out["content"] = aws_sdk_quicksight.types.body_section_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("BodySectionConfiguration.content required")
    if "Style" in data:
        import aws_sdk_quicksight.types.section_style

        out["style"] = aws_sdk_quicksight.types.section_style.deserialize_json(
            data["Style"]
        )
    if "PageBreakConfiguration" in data:
        import aws_sdk_quicksight.types.section_page_break_configuration

        out["page_break_configuration"] = (
            aws_sdk_quicksight.types.section_page_break_configuration.deserialize_json(
                data["PageBreakConfiguration"]
            )
        )
    if "RepeatConfiguration" in data:
        import aws_sdk_quicksight.types.body_section_repeat_configuration

        out["repeat_configuration"] = (
            aws_sdk_quicksight.types.body_section_repeat_configuration.deserialize_json(
                data["RepeatConfiguration"]
            )
        )
    return out
