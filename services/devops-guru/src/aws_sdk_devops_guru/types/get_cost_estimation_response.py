"""Generated from Smithy shape ``com.amazonaws.devopsguru#GetCostEstimationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.cost
    import aws_sdk_devops_guru.types.cost_estimation_resource_collection_filter
    import aws_sdk_devops_guru.types.cost_estimation_status
    import aws_sdk_devops_guru.types.cost_estimation_time_range
    import aws_sdk_devops_guru.types.service_resource_costs
    import aws_sdk_devops_guru.types.uuid_next_token


class GetCostEstimationResponse(TypedDict):
    resource_collection: NotRequired[
        "aws_sdk_devops_guru.types.cost_estimation_resource_collection_filter.CostEstimationResourceCollectionFilter"
    ]
    """<p>The collection of the Amazon Web Services resources used to create your monthly DevOps Guru cost estimate.</p>"""
    status: NotRequired[
        "aws_sdk_devops_guru.types.cost_estimation_status.CostEstimationStatus"
    ]
    """<p>The status of creating this cost estimate. If it's still in progress, the status <code>ONGOING</code> is returned. If it is finished, the status <code>COMPLETED</code> is returned.</p>"""
    costs: NotRequired[
        "aws_sdk_devops_guru.types.service_resource_costs.ServiceResourceCosts"
    ]
    """<p>An array of <code>ResourceCost</code> objects that each contains details about the monthly cost estimate to analyze one of your Amazon Web Services resources.</p>"""
    time_range: NotRequired[
        "aws_sdk_devops_guru.types.cost_estimation_time_range.CostEstimationTimeRange"
    ]
    """<p>The start and end time of the cost estimation.</p>"""
    total_cost: "aws_sdk_devops_guru.types.cost.Cost"
    """<p>The estimated monthly cost to analyze the Amazon Web Services resources. This value is the sum of the estimated costs to analyze each resource in the <code>Costs</code> object in this response.</p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCostEstimationResponse) -> dict:
    out: dict = {}
    if "resource_collection" in value:
        import aws_sdk_devops_guru.types.cost_estimation_resource_collection_filter

        out["ResourceCollection"] = (
            aws_sdk_devops_guru.types.cost_estimation_resource_collection_filter.serialize_json(
                value["resource_collection"]
            )
        )
    if "status" in value:
        import aws_sdk_devops_guru.types.cost_estimation_status

        out["Status"] = aws_sdk_devops_guru.types.cost_estimation_status.serialize_json(
            value["status"]
        )
    if "costs" in value:
        import aws_sdk_devops_guru.types.service_resource_costs

        out["Costs"] = aws_sdk_devops_guru.types.service_resource_costs.serialize_json(
            value["costs"]
        )
    if "time_range" in value:
        import aws_sdk_devops_guru.types.cost_estimation_time_range

        out["TimeRange"] = (
            aws_sdk_devops_guru.types.cost_estimation_time_range.serialize_json(
                value["time_range"]
            )
        )
    out["TotalCost"] = value.get("total_cost", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCostEstimationResponse:
    out: GetCostEstimationResponse = {}  # type: ignore[typeddict-item]
    if "ResourceCollection" in data:
        import aws_sdk_devops_guru.types.cost_estimation_resource_collection_filter

        out["resource_collection"] = (
            aws_sdk_devops_guru.types.cost_estimation_resource_collection_filter.deserialize_json(
                data["ResourceCollection"]
            )
        )
    if "Status" in data:
        import aws_sdk_devops_guru.types.cost_estimation_status

        out["status"] = (
            aws_sdk_devops_guru.types.cost_estimation_status.deserialize_json(
                data["Status"]
            )
        )
    if "Costs" in data:
        import aws_sdk_devops_guru.types.service_resource_costs

        out["costs"] = (
            aws_sdk_devops_guru.types.service_resource_costs.deserialize_json(
                data["Costs"]
            )
        )
    if "TimeRange" in data:
        import aws_sdk_devops_guru.types.cost_estimation_time_range

        out["time_range"] = (
            aws_sdk_devops_guru.types.cost_estimation_time_range.deserialize_json(
                data["TimeRange"]
            )
        )
    if "TotalCost" in data:
        out["total_cost"] = data["TotalCost"]
    else:
        out["total_cost"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
