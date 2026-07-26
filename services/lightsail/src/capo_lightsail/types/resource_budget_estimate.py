"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourceBudgetEstimate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.cost_estimates
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type


class ResourceBudgetEstimate(TypedDict, closed=True):
    resource_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The resource name.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The type of resource the budget will track.</p>"""
    cost_estimates: NotRequired["capo_lightsail.types.cost_estimates.CostEstimates"]
    """<p>The cost estimate for the specified budget.</p>"""
    start_time: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The estimate start time.</p>"""
    end_time: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The estimate end time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceBudgetEstimate) -> dict:
    out: dict = {}
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "cost_estimates" in value:
        import capo_lightsail.types.cost_estimates

        out["costEstimates"] = (
            capo_lightsail.types.cost_estimates.serialize_aws_json_1_1(
                value["cost_estimates"]
            )
        )
    if "start_time" in value:
        import capo_lightsail.types.iso_date

        out["startTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_lightsail.types.iso_date

        out["endTime"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceBudgetEstimate:
    out: ResourceBudgetEstimate = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "resourceType" in data:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "costEstimates" in data:
        import capo_lightsail.types.cost_estimates

        out["cost_estimates"] = (
            capo_lightsail.types.cost_estimates.deserialize_aws_json_1_1(
                data["costEstimates"]
            )
        )
    if "startTime" in data:
        import capo_lightsail.types.iso_date

        out["start_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "endTime" in data:
        import capo_lightsail.types.iso_date

        out["end_time"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["endTime"]
        )
    return out
