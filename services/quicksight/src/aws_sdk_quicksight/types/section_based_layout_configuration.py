"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionBasedLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.body_section_configuration_list
    import aws_sdk_quicksight.types.header_footer_section_configuration_list
    import aws_sdk_quicksight.types.section_based_layout_canvas_size_options


class SectionBasedLayoutConfiguration(TypedDict):
    header_sections: "aws_sdk_quicksight.types.header_footer_section_configuration_list.HeaderFooterSectionConfigurationList"
    """<p>A list of header section configurations.</p>"""
    body_sections: "aws_sdk_quicksight.types.body_section_configuration_list.BodySectionConfigurationList"
    """<p>A list of body section configurations.</p>"""
    footer_sections: "aws_sdk_quicksight.types.header_footer_section_configuration_list.HeaderFooterSectionConfigurationList"
    """<p>A list of footer section configurations.</p>"""
    canvas_size_options: "aws_sdk_quicksight.types.section_based_layout_canvas_size_options.SectionBasedLayoutCanvasSizeOptions"
    """<p>The options for the canvas of a section-based layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SectionBasedLayoutConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.header_footer_section_configuration_list

    out["HeaderSections"] = (
        aws_sdk_quicksight.types.header_footer_section_configuration_list.serialize_json(
            value["header_sections"]
        )
    )
    import aws_sdk_quicksight.types.body_section_configuration_list

    out["BodySections"] = (
        aws_sdk_quicksight.types.body_section_configuration_list.serialize_json(
            value["body_sections"]
        )
    )
    import aws_sdk_quicksight.types.header_footer_section_configuration_list

    out["FooterSections"] = (
        aws_sdk_quicksight.types.header_footer_section_configuration_list.serialize_json(
            value["footer_sections"]
        )
    )
    import aws_sdk_quicksight.types.section_based_layout_canvas_size_options

    out["CanvasSizeOptions"] = (
        aws_sdk_quicksight.types.section_based_layout_canvas_size_options.serialize_json(
            value["canvas_size_options"]
        )
    )
    return out


def deserialize_json(data: dict) -> SectionBasedLayoutConfiguration:
    out: SectionBasedLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "HeaderSections" in data:
        import aws_sdk_quicksight.types.header_footer_section_configuration_list

        out["header_sections"] = (
            aws_sdk_quicksight.types.header_footer_section_configuration_list.deserialize_json(
                data["HeaderSections"]
            )
        )
    else:
        raise DeserializationError(
            "SectionBasedLayoutConfiguration.header_sections required"
        )
    if "BodySections" in data:
        import aws_sdk_quicksight.types.body_section_configuration_list

        out["body_sections"] = (
            aws_sdk_quicksight.types.body_section_configuration_list.deserialize_json(
                data["BodySections"]
            )
        )
    else:
        raise DeserializationError(
            "SectionBasedLayoutConfiguration.body_sections required"
        )
    if "FooterSections" in data:
        import aws_sdk_quicksight.types.header_footer_section_configuration_list

        out["footer_sections"] = (
            aws_sdk_quicksight.types.header_footer_section_configuration_list.deserialize_json(
                data["FooterSections"]
            )
        )
    else:
        raise DeserializationError(
            "SectionBasedLayoutConfiguration.footer_sections required"
        )
    if "CanvasSizeOptions" in data:
        import aws_sdk_quicksight.types.section_based_layout_canvas_size_options

        out["canvas_size_options"] = (
            aws_sdk_quicksight.types.section_based_layout_canvas_size_options.deserialize_json(
                data["CanvasSizeOptions"]
            )
        )
    else:
        raise DeserializationError(
            "SectionBasedLayoutConfiguration.canvas_size_options required"
        )
    return out
