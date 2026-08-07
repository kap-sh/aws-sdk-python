"""Generated from Smithy shape ``com.amazonaws.autoscaling#MixedInstancesPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instances_distribution
    import capo_auto_scaling.types.launch_template


class MixedInstancesPolicy(TypedDict, closed=True):
    launch_template: NotRequired[
        "capo_auto_scaling.types.launch_template.LaunchTemplate"
    ]
    """<p>One or more launch templates and the instance types (overrides) that are used to launch EC2 instances to fulfill On-Demand and Spot capacities.</p>"""
    instances_distribution: NotRequired[
        "capo_auto_scaling.types.instances_distribution.InstancesDistribution"
    ]
    """<p>The instances distribution.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MixedInstancesPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template" in value:
        import capo_auto_scaling.types.launch_template

        capo_auto_scaling.types.launch_template.serialize_query(
            value["launch_template"], pairs, f"{key_prefix}LaunchTemplate"
        )
    if "instances_distribution" in value:
        import capo_auto_scaling.types.instances_distribution

        capo_auto_scaling.types.instances_distribution.serialize_query(
            value["instances_distribution"], pairs, f"{key_prefix}InstancesDistribution"
        )


def deserialize_query(el: Element) -> MixedInstancesPolicy:
    out: MixedInstancesPolicy = {}  # type: ignore[typeddict-item]
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import capo_auto_scaling.types.launch_template

        out["launch_template"] = (
            capo_auto_scaling.types.launch_template.deserialize_query(
                child_launch_template
            )
        )
    child_instances_distribution = el.find("InstancesDistribution")
    if child_instances_distribution is not None:
        import capo_auto_scaling.types.instances_distribution

        out["instances_distribution"] = (
            capo_auto_scaling.types.instances_distribution.deserialize_query(
                child_instances_distribution
            )
        )
    return out
