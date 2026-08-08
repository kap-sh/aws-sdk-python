"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_ids_set
    import capo_ec2.types.instance_lifecycle
    import capo_ec2.types.instance_type
    import capo_ec2.types.launch_template_and_overrides_response
    import capo_ec2.types.platform_values


class CreateFleetInstance(TypedDict, closed=True):
    launch_template_and_overrides: NotRequired[
        "capo_ec2.types.launch_template_and_overrides_response.LaunchTemplateAndOverridesResponse"
    ]
    """<p>The launch templates and overrides that were used for launching the instances. The values that you specify in the Overrides replace the values in the launch template.</p>"""
    lifecycle: NotRequired["capo_ec2.types.instance_lifecycle.InstanceLifecycle"]
    """<p>Indicates if the instance that was launched is a Spot, On-Demand, Capacity Block, or Interruptible Capacity Reservation instance.</p>"""
    instance_ids: NotRequired["capo_ec2.types.instance_ids_set.InstanceIdsSet"]
    """<p>The IDs of the instances.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    platform: NotRequired["capo_ec2.types.platform_values.PlatformValues"]
    """<p>The value is <code>windows</code> for Windows instances in an EC2 Fleet. Otherwise, the value is blank.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFleetInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_and_overrides" in value:
        import capo_ec2.types.launch_template_and_overrides_response

        capo_ec2.types.launch_template_and_overrides_response.serialize_ec2_query(
            value["launch_template_and_overrides"],
            pairs,
            f"{key_prefix}LaunchTemplateAndOverrides",
        )
    if "lifecycle" in value:
        import capo_ec2.types.instance_lifecycle

        capo_ec2.types.instance_lifecycle.serialize_ec2_query(
            value["lifecycle"], pairs, f"{key_prefix}Lifecycle"
        )
    if "instance_ids" in value:
        import capo_ec2.types.instance_ids_set

        capo_ec2.types.instance_ids_set.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceIds"
        )
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "platform" in value:
        import capo_ec2.types.platform_values

        capo_ec2.types.platform_values.serialize_ec2_query(
            value["platform"], pairs, f"{key_prefix}Platform"
        )


def deserialize_ec2_query(el: Element) -> CreateFleetInstance:
    out: CreateFleetInstance = {}  # type: ignore[typeddict-item]
    child_launch_template_and_overrides = el.find("launchTemplateAndOverrides")
    if child_launch_template_and_overrides is not None:
        import capo_ec2.types.launch_template_and_overrides_response

        out["launch_template_and_overrides"] = (
            capo_ec2.types.launch_template_and_overrides_response.deserialize_ec2_query(
                child_launch_template_and_overrides
            )
        )
    child_lifecycle = el.find("lifecycle")
    if child_lifecycle is not None:
        import capo_ec2.types.instance_lifecycle

        out["lifecycle"] = capo_ec2.types.instance_lifecycle.deserialize_ec2_query(
            child_lifecycle
        )
    if el.find("instanceIds") is not None:
        import capo_ec2.types.instance_ids_set

        out["instance_ids"] = capo_ec2.types.instance_ids_set.deserialize_ec2_query(
            el, "instanceIds"
        )
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_platform = el.find("platform")
    if child_platform is not None:
        import capo_ec2.types.platform_values

        out["platform"] = capo_ec2.types.platform_values.deserialize_ec2_query(
            child_platform
        )
    return out
