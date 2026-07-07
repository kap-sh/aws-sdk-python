"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_field_sort_options_list


class PivotTableSortConfiguration(TypedDict, closed=True):
    field_sort_options: NotRequired[
        "aws_sdk_quicksight.types.pivot_field_sort_options_list.PivotFieldSortOptionsList"
    ]
    """<p>The field sort options for a pivot table sort configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableSortConfiguration) -> dict:
    out: dict = {}
    if "field_sort_options" in value:
        import aws_sdk_quicksight.types.pivot_field_sort_options_list

        out["FieldSortOptions"] = (
            aws_sdk_quicksight.types.pivot_field_sort_options_list.serialize_json(
                value["field_sort_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableSortConfiguration:
    out: PivotTableSortConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldSortOptions" in data:
        import aws_sdk_quicksight.types.pivot_field_sort_options_list

        out["field_sort_options"] = (
            aws_sdk_quicksight.types.pivot_field_sort_options_list.deserialize_json(
                data["FieldSortOptions"]
            )
        )
    return out
