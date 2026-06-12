"""Generated from Smithy shape ``com.amazonaws.autoscaling#DesiredConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.launch_template_specification
    import aws_sdk_auto_scaling.types.mixed_instances_policy


class DesiredConfiguration(TypedDict):
    launch_template: NotRequired[
        "aws_sdk_auto_scaling.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>Describes the launch template and the version of the launch template that Amazon EC2 Auto Scaling uses to launch Amazon EC2 instances. For more information about launch templates, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html\">Launch templates</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""
    mixed_instances_policy: NotRequired[
        "aws_sdk_auto_scaling.types.mixed_instances_policy.MixedInstancesPolicy"
    ]
    """<p>Use this structure to launch multiple instance types and On-Demand Instances and Spot Instances within a single Auto Scaling group.</p> <p>A mixed instances policy contains information that Amazon EC2 Auto Scaling can use to launch instances and help optimize your costs. For more information, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html\">Auto Scaling groups with multiple instance types and purchase options</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DesiredConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template" in value:
        import aws_sdk_auto_scaling.types.launch_template_specification

        aws_sdk_auto_scaling.types.launch_template_specification.serialize_query(
            value["launch_template"], pairs, f"{prefix}.LaunchTemplate"
        )
    if "mixed_instances_policy" in value:
        import aws_sdk_auto_scaling.types.mixed_instances_policy

        aws_sdk_auto_scaling.types.mixed_instances_policy.serialize_query(
            value["mixed_instances_policy"], pairs, f"{prefix}.MixedInstancesPolicy"
        )


def deserialize_query(el: Element) -> DesiredConfiguration:
    out: DesiredConfiguration = {}  # type: ignore[typeddict-item]
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import aws_sdk_auto_scaling.types.launch_template_specification

        out["launch_template"] = (
            aws_sdk_auto_scaling.types.launch_template_specification.deserialize_query(
                child_launch_template
            )
        )
    child_mixed_instances_policy = el.find("MixedInstancesPolicy")
    if child_mixed_instances_policy is not None:
        import aws_sdk_auto_scaling.types.mixed_instances_policy

        out["mixed_instances_policy"] = (
            aws_sdk_auto_scaling.types.mixed_instances_policy.deserialize_query(
                child_mixed_instances_policy
            )
        )
    return out
