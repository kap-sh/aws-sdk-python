"""Generated from Smithy shape ``com.amazonaws.inspector2#TitleAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.aggregation_finding_type
    import capo_inspector2.types.aggregation_resource_type
    import capo_inspector2.types.sort_order
    import capo_inspector2.types.string_filter_list
    import capo_inspector2.types.title_sort_by


class TitleAggregation(TypedDict, closed=True):
    titles: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>The finding titles to aggregate on.</p>"""
    vulnerability_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The vulnerability IDs of the findings.</p>"""
    resource_type: NotRequired[
        "capo_inspector2.types.aggregation_resource_type.AggregationResourceType"
    ]
    """<p>The resource type to aggregate on.</p>"""
    sort_order: NotRequired["capo_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired["capo_inspector2.types.title_sort_by.TitleSortBy"]
    """<p>The value to sort results by.</p>"""
    finding_type: NotRequired[
        "capo_inspector2.types.aggregation_finding_type.AggregationFindingType"
    ]
    """<p>The type of finding to aggregate on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TitleAggregation) -> dict:
    out: dict = {}
    if "titles" in value:
        import capo_inspector2.types.string_filter_list

        out["titles"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["titles"]
        )
    if "vulnerability_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["vulnerabilityIds"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["vulnerability_ids"]
            )
        )
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    return out


def deserialize_json(data: dict) -> TitleAggregation:
    out: TitleAggregation = {}  # type: ignore[typeddict-item]
    if "titles" in data:
        import capo_inspector2.types.string_filter_list

        out["titles"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["titles"]
        )
    if "vulnerabilityIds" in data:
        import capo_inspector2.types.string_filter_list

        out["vulnerability_ids"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["vulnerabilityIds"]
            )
        )
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    if "findingType" in data:
        out["finding_type"] = data["findingType"]
    return out
