"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionRepeatConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.body_section_repeat_dimension_configuration_list
    import capo_quicksight.types.body_section_repeat_page_break_configuration
    import capo_quicksight.types.non_repeating_visuals_list


class BodySectionRepeatConfiguration(TypedDict, closed=True):
    dimension_configurations: NotRequired[
        "capo_quicksight.types.body_section_repeat_dimension_configuration_list.BodySectionRepeatDimensionConfigurationList"
    ]
    """<p>List of <code>BodySectionRepeatDimensionConfiguration</code> values that describe the dataset column and constraints for the column used to repeat the contents of a section.</p>"""
    page_break_configuration: NotRequired[
        "capo_quicksight.types.body_section_repeat_page_break_configuration.BodySectionRepeatPageBreakConfiguration"
    ]
    """<p>Page break configuration to apply for each repeating instance.</p>"""
    non_repeating_visuals: NotRequired[
        "capo_quicksight.types.non_repeating_visuals_list.NonRepeatingVisualsList"
    ]
    """<p>List of visuals to exclude from repetition in repeating sections. The visuals will render identically, and ignore the repeating configurations in all repeating instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionRepeatConfiguration) -> dict:
    out: dict = {}
    if "dimension_configurations" in value:
        import capo_quicksight.types.body_section_repeat_dimension_configuration_list

        out["DimensionConfigurations"] = (
            capo_quicksight.types.body_section_repeat_dimension_configuration_list.serialize_json(
                value["dimension_configurations"]
            )
        )
    if "page_break_configuration" in value:
        import capo_quicksight.types.body_section_repeat_page_break_configuration

        out["PageBreakConfiguration"] = (
            capo_quicksight.types.body_section_repeat_page_break_configuration.serialize_json(
                value["page_break_configuration"]
            )
        )
    if "non_repeating_visuals" in value:
        import capo_quicksight.types.non_repeating_visuals_list

        out["NonRepeatingVisuals"] = (
            capo_quicksight.types.non_repeating_visuals_list.serialize_json(
                value["non_repeating_visuals"]
            )
        )
    return out


def deserialize_json(data: dict) -> BodySectionRepeatConfiguration:
    out: BodySectionRepeatConfiguration = {}  # type: ignore[typeddict-item]
    if "DimensionConfigurations" in data:
        import capo_quicksight.types.body_section_repeat_dimension_configuration_list

        out["dimension_configurations"] = (
            capo_quicksight.types.body_section_repeat_dimension_configuration_list.deserialize_json(
                data["DimensionConfigurations"]
            )
        )
    if "PageBreakConfiguration" in data:
        import capo_quicksight.types.body_section_repeat_page_break_configuration

        out["page_break_configuration"] = (
            capo_quicksight.types.body_section_repeat_page_break_configuration.deserialize_json(
                data["PageBreakConfiguration"]
            )
        )
    if "NonRepeatingVisuals" in data:
        import capo_quicksight.types.non_repeating_visuals_list

        out["non_repeating_visuals"] = (
            capo_quicksight.types.non_repeating_visuals_list.deserialize_json(
                data["NonRepeatingVisuals"]
            )
        )
    return out
