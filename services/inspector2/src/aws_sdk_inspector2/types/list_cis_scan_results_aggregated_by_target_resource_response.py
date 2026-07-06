"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScanResultsAggregatedByTargetResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_target_resource_aggregation_list
    import aws_sdk_inspector2.types.next_token


class ListCisScanResultsAggregatedByTargetResourceResponse(TypedDict, closed=True):
    target_resource_aggregations: NotRequired[
        "aws_sdk_inspector2.types.cis_target_resource_aggregation_list.CisTargetResourceAggregationList"
    ]
    """<p>The resource aggregations.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScanResultsAggregatedByTargetResourceResponse) -> dict:
    out: dict = {}
    if "target_resource_aggregations" in value:
        import aws_sdk_inspector2.types.cis_target_resource_aggregation_list

        out["targetResourceAggregations"] = (
            aws_sdk_inspector2.types.cis_target_resource_aggregation_list.serialize_json(
                value["target_resource_aggregations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(
    data: dict,
) -> ListCisScanResultsAggregatedByTargetResourceResponse:
    out: ListCisScanResultsAggregatedByTargetResourceResponse = {}  # type: ignore[typeddict-item]
    if "targetResourceAggregations" in data:
        import aws_sdk_inspector2.types.cis_target_resource_aggregation_list

        out["target_resource_aggregations"] = (
            aws_sdk_inspector2.types.cis_target_resource_aggregation_list.deserialize_json(
                data["targetResourceAggregations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
