"""Generated from Smithy shape ``com.amazonaws.inspector2#FindingTypeAggregation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.aggregation_finding_type
    import aws_sdk_inspector2.types.aggregation_resource_type
    import aws_sdk_inspector2.types.finding_type_sort_by
    import aws_sdk_inspector2.types.sort_order


class FindingTypeAggregation(TypedDict):
    finding_type: NotRequired[
        "aws_sdk_inspector2.types.aggregation_finding_type.AggregationFindingType"
    ]
    """<p>The finding type to aggregate.</p>"""
    resource_type: NotRequired[
        "aws_sdk_inspector2.types.aggregation_resource_type.AggregationResourceType"
    ]
    """<p>The resource type to aggregate.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired[
        "aws_sdk_inspector2.types.finding_type_sort_by.FindingTypeSortBy"
    ]
    """<p>The value to sort results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeAggregation) -> dict:
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


def deserialize_json(data: dict) -> FindingTypeAggregation:
    out: FindingTypeAggregation = {}  # type: ignore[typeddict-item]
    if "findingType" in data:
        out["finding_type"] = data["findingType"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "sortOrder" in data:
        out["sort_order"] = data["sortOrder"]
    if "sortBy" in data:
        out["sort_by"] = data["sortBy"]
    return out
