"""Generated from Smithy shape ``com.amazonaws.inspector2#RepositoryAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.repository_sort_by
    import capo_inspector2.types.sort_order
    import capo_inspector2.types.string_filter_list


class RepositoryAggregation(TypedDict, closed=True):
    repositories: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The names of repositories to aggregate findings on.</p>"""
    sort_order: NotRequired["capo_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired["capo_inspector2.types.repository_sort_by.RepositorySortBy"]
    """<p>The value to sort results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAggregation) -> dict:
    out: dict = {}
    if "repositories" in value:
        import capo_inspector2.types.string_filter_list

        out["repositories"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["repositories"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> RepositoryAggregation:
    out: RepositoryAggregation = {}  # type: ignore[typeddict-item]
    if "repositories" in data:
        import capo_inspector2.types.string_filter_list

        out["repositories"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["repositories"]
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
