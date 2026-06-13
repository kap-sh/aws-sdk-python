"""Generated from Smithy shape ``com.amazonaws.inspector2#RepositoryAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.repository_sort_by
    import aws_sdk_inspector2.types.sort_order
    import aws_sdk_inspector2.types.string_filter_list


class RepositoryAggregation(TypedDict):
    repositories: NotRequired[
        "aws_sdk_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The names of repositories to aggregate findings on.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired["aws_sdk_inspector2.types.repository_sort_by.RepositorySortBy"]
    """<p>The value to sort results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAggregation) -> dict:
    out: dict = {}
    if "repositories" in value:
        import aws_sdk_inspector2.types.string_filter_list

        out["repositories"] = (
            aws_sdk_inspector2.types.string_filter_list.serialize_json(
                value["repositories"]
            )
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> RepositoryAggregation:
    out: RepositoryAggregation = {}  # type: ignore[typeddict-item]
    if "repositories" in data:
        import aws_sdk_inspector2.types.string_filter_list

        out["repositories"] = (
            aws_sdk_inspector2.types.string_filter_list.deserialize_json(
                data["repositories"]
            )
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
