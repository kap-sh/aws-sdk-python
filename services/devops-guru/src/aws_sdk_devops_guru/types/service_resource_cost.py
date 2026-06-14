"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceResourceCost``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.cost
    import aws_sdk_devops_guru.types.cost_estimation_service_resource_count
    import aws_sdk_devops_guru.types.cost_estimation_service_resource_state
    import aws_sdk_devops_guru.types.resource_type


class ServiceResourceCost(TypedDict):
    type: NotRequired["aws_sdk_devops_guru.types.resource_type.ResourceType"]
    """<p>The type of the Amazon Web Services resource.</p>"""
    state: NotRequired[
        "aws_sdk_devops_guru.types.cost_estimation_service_resource_state.CostEstimationServiceResourceState"
    ]
    """<p>The state of the resource. The resource is <code>ACTIVE</code> if it produces metrics, events, or logs within an hour, otherwise it is <code>INACTIVE</code>. You pay for the number of active Amazon Web Services resource hours analyzed for each resource. Inactive resources are not charged. </p>"""
    count: "aws_sdk_devops_guru.types.cost_estimation_service_resource_count.CostEstimationServiceResourceCount"
    """<p>The number of active resources analyzed for this service to create a monthly cost estimate.</p>"""
    unit_cost: "aws_sdk_devops_guru.types.cost.Cost"
    r"""<p>The price per hour to analyze the resources in the service. For more information, see <a href=\"https://docs.aws.amazon.com/devops-guru/latest/userguide/cost-estimate.html\">Estimate your Amazon DevOps Guru costs</a> and <a href=\"http://aws.amazon.com/devops-guru/pricing/\">Amazon DevOps Guru pricing</a>.</p>"""
    cost: "aws_sdk_devops_guru.types.cost.Cost"
    """<p>The total estimated monthly cost to analyze the active resources for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResourceCost) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "state" in value:
        import aws_sdk_devops_guru.types.cost_estimation_service_resource_state

        out["State"] = (
            aws_sdk_devops_guru.types.cost_estimation_service_resource_state.serialize_json(
                value["state"]
            )
        )
    out["Count"] = value.get("count", 0)
    out["UnitCost"] = value.get("unit_cost", 0)
    out["Cost"] = value.get("cost", 0)
    return out


def deserialize_json(data: dict) -> ServiceResourceCost:
    out: ServiceResourceCost = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "State" in data:
        import aws_sdk_devops_guru.types.cost_estimation_service_resource_state

        out["state"] = (
            aws_sdk_devops_guru.types.cost_estimation_service_resource_state.deserialize_json(
                data["State"]
            )
        )
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if "UnitCost" in data:
        out["unit_cost"] = data["UnitCost"]
    else:
        out["unit_cost"] = 0
    if "Cost" in data:
        out["cost"] = data["Cost"]
    else:
        out["cost"] = 0
    return out
