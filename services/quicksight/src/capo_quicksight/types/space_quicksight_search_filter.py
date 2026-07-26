"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuicksightSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.space_quick_sight_search_filter_name
    import capo_quicksight.types.space_search_operator


class SpaceQuicksightSearchFilter(TypedDict, closed=True):
    name: "capo_quicksight.types.space_quick_sight_search_filter_name.SpaceQuickSightSearchFilterName"
    """<p>The name of the filter field to use.</p>"""
    operator: "capo_quicksight.types.space_search_operator.SpaceSearchOperator"
    """<p>The comparison operator to use for the filter.</p>"""
    value: "str"
    """<p>The value to use for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceQuicksightSearchFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.space_quick_sight_search_filter_name

    out["name"] = (
        capo_quicksight.types.space_quick_sight_search_filter_name.serialize_json(
            value["name"]
        )
    )
    import capo_quicksight.types.space_search_operator

    out["operator"] = capo_quicksight.types.space_search_operator.serialize_json(
        value["operator"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SpaceQuicksightSearchFilter:
    out: SpaceQuicksightSearchFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_quicksight.types.space_quick_sight_search_filter_name

        out["name"] = (
            capo_quicksight.types.space_quick_sight_search_filter_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("SpaceQuicksightSearchFilter.name required")
    if "operator" in data:
        import capo_quicksight.types.space_search_operator

        out["operator"] = capo_quicksight.types.space_search_operator.deserialize_json(
            data["operator"]
        )
    else:
        raise DeserializationError("SpaceQuicksightSearchFilter.operator required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("SpaceQuicksightSearchFilter.value required")
    return out
