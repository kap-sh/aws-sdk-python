"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeRepositoryAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_repository_sort_by
    import capo_inspector2.types.sort_order
    import capo_inspector2.types.string_filter_list


class CodeRepositoryAggregation(TypedDict, closed=True):
    project_names: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The project names to include in the aggregation results.</p>"""
    provider_types: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The repository provider types to include in the aggregation results.</p>"""
    sort_order: NotRequired["capo_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by (ascending or descending) in the code repository aggregation.</p>"""
    sort_by: NotRequired[
        "capo_inspector2.types.code_repository_sort_by.CodeRepositorySortBy"
    ]
    """<p>The value to sort results by in the code repository aggregation.</p>"""
    resource_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The resource IDs to include in the aggregation results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeRepositoryAggregation) -> dict:
    out: dict = {}
    if "project_names" in value:
        import capo_inspector2.types.string_filter_list

        out["projectNames"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["project_names"]
        )
    if "provider_types" in value:
        import capo_inspector2.types.string_filter_list

        out["providerTypes"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["provider_types"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "resource_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["resourceIds"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["resource_ids"]
        )
    return out


def deserialize_json(data: dict) -> CodeRepositoryAggregation:
    out: CodeRepositoryAggregation = {}  # type: ignore[typeddict-item]
    if "projectNames" in data:
        import capo_inspector2.types.string_filter_list

        out["project_names"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["projectNames"]
            )
        )
    if "providerTypes" in data:
        import capo_inspector2.types.string_filter_list

        out["provider_types"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["providerTypes"]
            )
        )
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    if "resourceIds" in data:
        import capo_inspector2.types.string_filter_list

        out["resource_ids"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["resourceIds"]
        )
    return out
