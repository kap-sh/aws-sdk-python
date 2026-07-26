"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionDynamicNumericDimensionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.body_section_dynamic_dimension_limit
    import capo_quicksight.types.body_section_dynamic_dimension_sort_configuration_list
    import capo_quicksight.types.column_identifier


class BodySectionDynamicNumericDimensionConfiguration(TypedDict, closed=True):
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    limit: NotRequired[
        "capo_quicksight.types.body_section_dynamic_dimension_limit.BodySectionDynamicDimensionLimit"
    ]
    """<p>Number of values to use from the column for repetition.</p>"""
    sort_by_metrics: NotRequired[
        "capo_quicksight.types.body_section_dynamic_dimension_sort_configuration_list.BodySectionDynamicDimensionSortConfigurationList"
    ]
    """<p>Sort criteria on the column values that you use for repetition. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionDynamicNumericDimensionConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "sort_by_metrics" in value:
        import capo_quicksight.types.body_section_dynamic_dimension_sort_configuration_list

        out["SortByMetrics"] = (
            capo_quicksight.types.body_section_dynamic_dimension_sort_configuration_list.serialize_json(
                value["sort_by_metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> BodySectionDynamicNumericDimensionConfiguration:
    out: BodySectionDynamicNumericDimensionConfiguration = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError(
            "BodySectionDynamicNumericDimensionConfiguration.column required"
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "SortByMetrics" in data:
        import capo_quicksight.types.body_section_dynamic_dimension_sort_configuration_list

        out["sort_by_metrics"] = (
            capo_quicksight.types.body_section_dynamic_dimension_sort_configuration_list.deserialize_json(
                data["SortByMetrics"]
            )
        )
    return out
