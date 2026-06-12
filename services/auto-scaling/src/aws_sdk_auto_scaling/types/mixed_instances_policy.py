"""Generated from Smithy shape ``com.amazonaws.autoscaling#MixedInstancesPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.instances_distribution
    import aws_sdk_auto_scaling.types.launch_template


class MixedInstancesPolicy(TypedDict):
    launch_template: NotRequired[
        "aws_sdk_auto_scaling.types.launch_template.LaunchTemplate"
    ]
    """<p>One or more launch templates and the instance types (overrides) that are used to launch EC2 instances to fulfill On-Demand and Spot capacities.</p>"""
    instances_distribution: NotRequired[
        "aws_sdk_auto_scaling.types.instances_distribution.InstancesDistribution"
    ]
    """<p>The instances distribution.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MixedInstancesPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template" in value:
        import aws_sdk_auto_scaling.types.launch_template

        aws_sdk_auto_scaling.types.launch_template.serialize_query(
            value["launch_template"], pairs, f"{prefix}.LaunchTemplate"
        )
    if "instances_distribution" in value:
        import aws_sdk_auto_scaling.types.instances_distribution

        aws_sdk_auto_scaling.types.instances_distribution.serialize_query(
            value["instances_distribution"], pairs, f"{prefix}.InstancesDistribution"
        )


def deserialize_query(el: Element) -> MixedInstancesPolicy:
    out: MixedInstancesPolicy = {}  # type: ignore[typeddict-item]
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import aws_sdk_auto_scaling.types.launch_template

        out["launch_template"] = (
            aws_sdk_auto_scaling.types.launch_template.deserialize_query(
                child_launch_template
            )
        )
    child_instances_distribution = el.find("InstancesDistribution")
    if child_instances_distribution is not None:
        import aws_sdk_auto_scaling.types.instances_distribution

        out["instances_distribution"] = (
            aws_sdk_auto_scaling.types.instances_distribution.deserialize_query(
                child_instances_distribution
            )
        )
    return out
