"""Generated from Smithy shape ``com.amazonaws.inspector2#AccountAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_sort_by
    import aws_sdk_inspector2.types.aggregation_finding_type
    import aws_sdk_inspector2.types.aggregation_resource_type
    import aws_sdk_inspector2.types.sort_order


class AccountAggregation(TypedDict, closed=True):
    finding_type: NotRequired[
        "aws_sdk_inspector2.types.aggregation_finding_type.AggregationFindingType"
    ]
    """<p>The type of finding.</p>"""
    resource_type: NotRequired[
        "aws_sdk_inspector2.types.aggregation_resource_type.AggregationResourceType"
    ]
    """<p>The type of resource.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The sort order (ascending or descending).</p>"""
    sort_by: NotRequired["aws_sdk_inspector2.types.account_sort_by.AccountSortBy"]
    """<p>The value to sort by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountAggregation) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> AccountAggregation:
    out: AccountAggregation = {}  # type: ignore[typeddict-item]
    if "findingType" in data:
        out["finding_type"] = data["findingType"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
