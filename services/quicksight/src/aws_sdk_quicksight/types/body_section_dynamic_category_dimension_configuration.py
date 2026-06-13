"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionDynamicCategoryDimensionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.body_section_dynamic_dimension_limit
    import aws_sdk_quicksight.types.body_section_dynamic_dimension_sort_configuration_list
    import aws_sdk_quicksight.types.column_identifier


class BodySectionDynamicCategoryDimensionConfiguration(TypedDict):
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    limit: NotRequired[
        "aws_sdk_quicksight.types.body_section_dynamic_dimension_limit.BodySectionDynamicDimensionLimit"
    ]
    """<p>Number of values to use from the column for repetition.</p>"""
    sort_by_metrics: NotRequired[
        "aws_sdk_quicksight.types.body_section_dynamic_dimension_sort_configuration_list.BodySectionDynamicDimensionSortConfigurationList"
    ]
    """<p>Sort criteria on the column values that you use for repetition. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionDynamicCategoryDimensionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "sort_by_metrics" in value:
        import aws_sdk_quicksight.types.body_section_dynamic_dimension_sort_configuration_list

        out["SortByMetrics"] = (
            aws_sdk_quicksight.types.body_section_dynamic_dimension_sort_configuration_list.serialize_json(
                value["sort_by_metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> BodySectionDynamicCategoryDimensionConfiguration:
    out: BodySectionDynamicCategoryDimensionConfiguration = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError(
            "BodySectionDynamicCategoryDimensionConfiguration.column required"
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "SortByMetrics" in data:
        import aws_sdk_quicksight.types.body_section_dynamic_dimension_sort_configuration_list

        out["sort_by_metrics"] = (
            aws_sdk_quicksight.types.body_section_dynamic_dimension_sort_configuration_list.deserialize_json(
                data["SortByMetrics"]
            )
        )
    return out
