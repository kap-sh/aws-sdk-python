"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceMaintenancePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.int_percent100_to200_resettable
    import capo_auto_scaling.types.int_percent_resettable


class InstanceMaintenancePolicy(TypedDict, closed=True):
    min_healthy_percentage: NotRequired[
        "capo_auto_scaling.types.int_percent_resettable.IntPercentResettable"
    ]
    """<p>Specifies the lower threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the minimum percentage of the group to keep in service, healthy, and ready to use to support your workload when replacing instances. Value range is 0 to 100. To clear a previously set value, specify a value of <code>-1</code>.</p>"""
    max_healthy_percentage: NotRequired[
        "capo_auto_scaling.types.int_percent100_to200_resettable.IntPercent100To200Resettable"
    ]
    """<p>Specifies the upper threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the maximum percentage of the group that can be in service and healthy, or pending, to support your workload when replacing instances. Value range is 100 to 200. To clear a previously set value, specify a value of <code>-1</code>.</p> <p>Both <code>MinHealthyPercentage</code> and <code>MaxHealthyPercentage</code> must be specified, and the difference between them cannot be greater than 100. A large range increases the number of instances that can be replaced at the same time.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceMaintenancePolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min_healthy_percentage" in value:
        pairs.append(
            (f"{prefix}.MinHealthyPercentage", str(value["min_healthy_percentage"]))
        )
    if "max_healthy_percentage" in value:
        pairs.append(
            (f"{prefix}.MaxHealthyPercentage", str(value["max_healthy_percentage"]))
        )


def deserialize_query(el: Element) -> InstanceMaintenancePolicy:
    out: InstanceMaintenancePolicy = {}  # type: ignore[typeddict-item]
    child_min_healthy_percentage = el.find("MinHealthyPercentage")
    if child_min_healthy_percentage is not None:
        out["min_healthy_percentage"] = int(child_min_healthy_percentage.text or "")
    child_max_healthy_percentage = el.find("MaxHealthyPercentage")
    if child_max_healthy_percentage is not None:
        out["max_healthy_percentage"] = int(child_max_healthy_percentage.text or "")
    return out
