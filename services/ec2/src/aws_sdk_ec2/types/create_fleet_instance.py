"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_ids_set
    import aws_sdk_ec2.types.instance_lifecycle
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.launch_template_and_overrides_response
    import aws_sdk_ec2.types.platform_values


class CreateFleetInstance(TypedDict, closed=True):
    launch_template_and_overrides: NotRequired[
        "aws_sdk_ec2.types.launch_template_and_overrides_response.LaunchTemplateAndOverridesResponse"
    ]
    """<p>The launch templates and overrides that were used for launching the instances. The values that you specify in the Overrides replace the values in the launch template.</p>"""
    lifecycle: NotRequired["aws_sdk_ec2.types.instance_lifecycle.InstanceLifecycle"]
    """<p>Indicates if the instance that was launched is a Spot, On-Demand, Capacity Block, or Interruptible Capacity Reservation instance.</p>"""
    instance_ids: NotRequired["aws_sdk_ec2.types.instance_ids_set.InstanceIdsSet"]
    """<p>The IDs of the instances.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.platform_values.PlatformValues"]
    """<p>The value is <code>windows</code> for Windows instances in an EC2 Fleet. Otherwise, the value is blank.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFleetInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_template_and_overrides" in value:
        import aws_sdk_ec2.types.launch_template_and_overrides_response

        aws_sdk_ec2.types.launch_template_and_overrides_response.serialize_ec2_query(
            value["launch_template_and_overrides"],
            pairs,
            f"{prefix}.LaunchTemplateAndOverrides",
        )
    if "lifecycle" in value:
        import aws_sdk_ec2.types.instance_lifecycle

        aws_sdk_ec2.types.instance_lifecycle.serialize_ec2_query(
            value["lifecycle"], pairs, f"{prefix}.Lifecycle"
        )
    if "instance_ids" in value:
        import aws_sdk_ec2.types.instance_ids_set

        aws_sdk_ec2.types.instance_ids_set.serialize_ec2_query(
            value["instance_ids"], pairs, f"{prefix}.InstanceIds"
        )
    if "instance_type" in value:
        import aws_sdk_ec2.types.instance_type

        aws_sdk_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "platform" in value:
        import aws_sdk_ec2.types.platform_values

        aws_sdk_ec2.types.platform_values.serialize_ec2_query(
            value["platform"], pairs, f"{prefix}.Platform"
        )


def deserialize_ec2_query(el: Element) -> CreateFleetInstance:
    out: CreateFleetInstance = {}  # type: ignore[typeddict-item]
    child_launch_template_and_overrides = el.find("LaunchTemplateAndOverrides")
    if child_launch_template_and_overrides is not None:
        import aws_sdk_ec2.types.launch_template_and_overrides_response

        out["launch_template_and_overrides"] = (
            aws_sdk_ec2.types.launch_template_and_overrides_response.deserialize_ec2_query(
                child_launch_template_and_overrides
            )
        )
    child_lifecycle = el.find("Lifecycle")
    if child_lifecycle is not None:
        import aws_sdk_ec2.types.instance_lifecycle

        out["lifecycle"] = aws_sdk_ec2.types.instance_lifecycle.deserialize_ec2_query(
            child_lifecycle
        )
    if el.find("InstanceIds") is not None:
        import aws_sdk_ec2.types.instance_ids_set

        out["instance_ids"] = aws_sdk_ec2.types.instance_ids_set.deserialize_ec2_query(
            el, "InstanceIds"
        )
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import aws_sdk_ec2.types.instance_type

        out["instance_type"] = aws_sdk_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_platform = el.find("Platform")
    if child_platform is not None:
        import aws_sdk_ec2.types.platform_values

        out["platform"] = aws_sdk_ec2.types.platform_values.deserialize_ec2_query(
            child_platform
        )
    return out
