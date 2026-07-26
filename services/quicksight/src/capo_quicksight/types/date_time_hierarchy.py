"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeHierarchy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.drill_down_filter_list
    import capo_quicksight.types.hierarchy_id


class DateTimeHierarchy(TypedDict, closed=True):
    hierarchy_id: "capo_quicksight.types.hierarchy_id.HierarchyId"
    """<p>The hierarchy ID of the <code>DateTime</code> hierarchy.</p>"""
    drill_down_filters: NotRequired[
        "capo_quicksight.types.drill_down_filter_list.DrillDownFilterList"
    ]
    """<p>The option that determines the drill down filters for the <code>DateTime</code> hierarchy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeHierarchy) -> dict:
    out: dict = {}
    out["HierarchyId"] = value["hierarchy_id"]
    if "drill_down_filters" in value:
        import capo_quicksight.types.drill_down_filter_list

        out["DrillDownFilters"] = (
            capo_quicksight.types.drill_down_filter_list.serialize_json(
                value["drill_down_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateTimeHierarchy:
    out: DateTimeHierarchy = {}  # type: ignore[typeddict-item]
    if "HierarchyId" in data:
        out["hierarchy_id"] = data["HierarchyId"]
    else:
        raise DeserializationError("DateTimeHierarchy.hierarchy_id required")
    if "DrillDownFilters" in data:
        import capo_quicksight.types.drill_down_filter_list

        out["drill_down_filters"] = (
            capo_quicksight.types.drill_down_filter_list.deserialize_json(
                data["DrillDownFilters"]
            )
        )
    return out
