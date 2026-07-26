"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastLaunchImagesSuccessItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fast_launch_launch_template_specification_response
    import capo_ec2.types.fast_launch_resource_type
    import capo_ec2.types.fast_launch_snapshot_configuration_response
    import capo_ec2.types.fast_launch_state_code
    import capo_ec2.types.image_id
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class DescribeFastLaunchImagesSuccessItem(TypedDict, closed=True):
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The image ID that identifies the Windows fast launch enabled image.</p>"""
    resource_type: NotRequired[
        "capo_ec2.types.fast_launch_resource_type.FastLaunchResourceType"
    ]
    """<p>The resource type that Amazon EC2 uses for pre-provisioning the Windows AMI. Supported values include: <code>snapshot</code>.</p>"""
    snapshot_configuration: NotRequired[
        "capo_ec2.types.fast_launch_snapshot_configuration_response.FastLaunchSnapshotConfigurationResponse"
    ]
    """<p>A group of parameters that are used for pre-provisioning the associated Windows AMI using snapshots.</p>"""
    launch_template: NotRequired[
        "capo_ec2.types.fast_launch_launch_template_specification_response.FastLaunchLaunchTemplateSpecificationResponse"
    ]
    """<p>The launch template that the Windows fast launch enabled AMI uses when it launches Windows instances from pre-provisioned snapshots.</p>"""
    max_parallel_launches: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The owner ID for the Windows fast launch enabled AMI.</p>"""
    state: NotRequired["capo_ec2.types.fast_launch_state_code.FastLaunchStateCode"]
    """<p>The current state of Windows fast launch for the specified Windows AMI.</p>"""
    state_transition_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason that Windows fast launch for the AMI changed to the current state.</p>"""
    state_transition_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time that Windows fast launch for the AMI changed to the current state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFastLaunchImagesSuccessItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "resource_type" in value:
        import capo_ec2.types.fast_launch_resource_type

        capo_ec2.types.fast_launch_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "snapshot_configuration" in value:
        import capo_ec2.types.fast_launch_snapshot_configuration_response

        capo_ec2.types.fast_launch_snapshot_configuration_response.serialize_ec2_query(
            value["snapshot_configuration"], pairs, f"{prefix}.SnapshotConfiguration"
        )
    if "launch_template" in value:
        import capo_ec2.types.fast_launch_launch_template_specification_response

        capo_ec2.types.fast_launch_launch_template_specification_response.serialize_ec2_query(
            value["launch_template"], pairs, f"{prefix}.LaunchTemplate"
        )
    if "max_parallel_launches" in value:
        pairs.append(
            (f"{prefix}.MaxParallelLaunches", str(value["max_parallel_launches"]))
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "state" in value:
        import capo_ec2.types.fast_launch_state_code

        capo_ec2.types.fast_launch_state_code.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "state_transition_reason" in value:
        pairs.append(
            (f"{prefix}.StateTransitionReason", str(value["state_transition_reason"]))
        )
    if "state_transition_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["state_transition_time"], pairs, f"{prefix}.StateTransitionTime"
        )


def deserialize_ec2_query(el: Element) -> DescribeFastLaunchImagesSuccessItem:
    out: DescribeFastLaunchImagesSuccessItem = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.fast_launch_resource_type

        out["resource_type"] = (
            capo_ec2.types.fast_launch_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_snapshot_configuration = el.find("SnapshotConfiguration")
    if child_snapshot_configuration is not None:
        import capo_ec2.types.fast_launch_snapshot_configuration_response

        out["snapshot_configuration"] = (
            capo_ec2.types.fast_launch_snapshot_configuration_response.deserialize_ec2_query(
                child_snapshot_configuration
            )
        )
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import capo_ec2.types.fast_launch_launch_template_specification_response

        out["launch_template"] = (
            capo_ec2.types.fast_launch_launch_template_specification_response.deserialize_ec2_query(
                child_launch_template
            )
        )
    child_max_parallel_launches = el.find("MaxParallelLaunches")
    if child_max_parallel_launches is not None:
        out["max_parallel_launches"] = int(child_max_parallel_launches.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.fast_launch_state_code

        out["state"] = capo_ec2.types.fast_launch_state_code.deserialize_ec2_query(
            child_state
        )
    child_state_transition_reason = el.find("StateTransitionReason")
    if child_state_transition_reason is not None:
        out["state_transition_reason"] = str(child_state_transition_reason.text or "")
    child_state_transition_time = el.find("StateTransitionTime")
    if child_state_transition_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["state_transition_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_state_transition_time
            )
        )
    return out
