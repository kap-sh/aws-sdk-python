"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionRepeatDimensionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.body_section_dynamic_category_dimension_configuration
    import aws_sdk_quicksight.types.body_section_dynamic_numeric_dimension_configuration


class BodySectionRepeatDimensionConfiguration(TypedDict):
    dynamic_category_dimension_configuration: NotRequired[
        "aws_sdk_quicksight.types.body_section_dynamic_category_dimension_configuration.BodySectionDynamicCategoryDimensionConfiguration"
    ]
    """<p>Describes the <b>Category</b> dataset column and constraints around the dynamic values that will be used in repeating the section contents.</p>"""
    dynamic_numeric_dimension_configuration: NotRequired[
        "aws_sdk_quicksight.types.body_section_dynamic_numeric_dimension_configuration.BodySectionDynamicNumericDimensionConfiguration"
    ]
    """<p>Describes the <b>Numeric</b> dataset column and constraints around the dynamic values used to repeat the contents of a section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionRepeatDimensionConfiguration) -> dict:
    out: dict = {}
    if "dynamic_category_dimension_configuration" in value:
        import aws_sdk_quicksight.types.body_section_dynamic_category_dimension_configuration

        out["DynamicCategoryDimensionConfiguration"] = (
            aws_sdk_quicksight.types.body_section_dynamic_category_dimension_configuration.serialize_json(
                value["dynamic_category_dimension_configuration"]
            )
        )
    if "dynamic_numeric_dimension_configuration" in value:
        import aws_sdk_quicksight.types.body_section_dynamic_numeric_dimension_configuration

        out["DynamicNumericDimensionConfiguration"] = (
            aws_sdk_quicksight.types.body_section_dynamic_numeric_dimension_configuration.serialize_json(
                value["dynamic_numeric_dimension_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BodySectionRepeatDimensionConfiguration:
    out: BodySectionRepeatDimensionConfiguration = {}  # type: ignore[typeddict-item]
    if "DynamicCategoryDimensionConfiguration" in data:
        import aws_sdk_quicksight.types.body_section_dynamic_category_dimension_configuration

        out["dynamic_category_dimension_configuration"] = (
            aws_sdk_quicksight.types.body_section_dynamic_category_dimension_configuration.deserialize_json(
                data["DynamicCategoryDimensionConfiguration"]
            )
        )
    if "DynamicNumericDimensionConfiguration" in data:
        import aws_sdk_quicksight.types.body_section_dynamic_numeric_dimension_configuration

        out["dynamic_numeric_dimension_configuration"] = (
            aws_sdk_quicksight.types.body_section_dynamic_numeric_dimension_configuration.deserialize_json(
                data["DynamicNumericDimensionConfiguration"]
            )
        )
    return out
