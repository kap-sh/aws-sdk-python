"""Generated from Smithy shape ``com.amazonaws.quicksight#ControlSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_sort_configuration
    import aws_sdk_quicksight.types.selectable_values_sort


class ControlSortConfiguration(TypedDict, closed=True):
    selectable_values_sort: NotRequired[
        "aws_sdk_quicksight.types.selectable_values_sort.SelectableValuesSort"
    ]
    """<p>The sort configuration for user-specified values in the control. Use this option to sort values that are manually entered by users in a dropdown or list control.</p>"""
    control_column_sort: NotRequired[
        "aws_sdk_quicksight.types.aggregation_sort_configuration.AggregationSortConfiguration"
    ]
    """<p>The sort configuration for controls that are tied to a dataset column. Use this option to sort control values by an aggregate of a column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlSortConfiguration) -> dict:
    out: dict = {}
    if "selectable_values_sort" in value:
        import aws_sdk_quicksight.types.selectable_values_sort

        out["SelectableValuesSort"] = (
            aws_sdk_quicksight.types.selectable_values_sort.serialize_json(
                value["selectable_values_sort"]
            )
        )
    if "control_column_sort" in value:
        import aws_sdk_quicksight.types.aggregation_sort_configuration

        out["ControlColumnSort"] = (
            aws_sdk_quicksight.types.aggregation_sort_configuration.serialize_json(
                value["control_column_sort"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlSortConfiguration:
    out: ControlSortConfiguration = {}  # type: ignore[typeddict-item]
    if "SelectableValuesSort" in data:
        import aws_sdk_quicksight.types.selectable_values_sort

        out["selectable_values_sort"] = (
            aws_sdk_quicksight.types.selectable_values_sort.deserialize_json(
                data["SelectableValuesSort"]
            )
        )
    if "ControlColumnSort" in data:
        import aws_sdk_quicksight.types.aggregation_sort_configuration

        out["control_column_sort"] = (
            aws_sdk_quicksight.types.aggregation_sort_configuration.deserialize_json(
                data["ControlColumnSort"]
            )
        )
    return out
