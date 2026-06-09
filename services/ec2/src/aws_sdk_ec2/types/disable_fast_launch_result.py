"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastLaunchResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fast_launch_launch_template_specification_response
    import aws_sdk_ec2.types.fast_launch_resource_type
    import aws_sdk_ec2.types.fast_launch_snapshot_configuration_response
    import aws_sdk_ec2.types.fast_launch_state_code
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class DisableFastLaunchResult(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the image for which Windows fast launch was disabled.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.fast_launch_resource_type.FastLaunchResourceType"
    ]
    """<p>The pre-provisioning resource type that must be cleaned after turning off Windows fast launch for the Windows AMI. Supported values include: <code>snapshot</code>.</p>"""
    snapshot_configuration: NotRequired[
        "aws_sdk_ec2.types.fast_launch_snapshot_configuration_response.FastLaunchSnapshotConfigurationResponse"
    ]
    """<p>Parameters that were used for Windows fast launch for the Windows AMI before Windows fast launch was disabled. This informs the clean-up process.</p>"""
    launch_template: NotRequired[
        "aws_sdk_ec2.types.fast_launch_launch_template_specification_response.FastLaunchLaunchTemplateSpecificationResponse"
    ]
    """<p>The launch template that was used to launch Windows instances from pre-provisioned snapshots.</p>"""
    max_parallel_launches: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The owner of the Windows AMI for which Windows fast launch was disabled.</p>"""
    state: NotRequired["aws_sdk_ec2.types.fast_launch_state_code.FastLaunchStateCode"]
    """<p>The current state of Windows fast launch for the specified Windows AMI.</p>"""
    state_transition_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason that the state changed for Windows fast launch for the Windows AMI.</p>"""
    state_transition_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time that the state changed for Windows fast launch for the Windows AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableFastLaunchResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.fast_launch_resource_type

        aws_sdk_ec2.types.fast_launch_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "snapshot_configuration" in value:
        import aws_sdk_ec2.types.fast_launch_snapshot_configuration_response

        aws_sdk_ec2.types.fast_launch_snapshot_configuration_response.serialize_ec2_query(
            value["snapshot_configuration"], pairs, f"{prefix}.SnapshotConfiguration"
        )
    if "launch_template" in value:
        import aws_sdk_ec2.types.fast_launch_launch_template_specification_response

        aws_sdk_ec2.types.fast_launch_launch_template_specification_response.serialize_ec2_query(
            value["launch_template"], pairs, f"{prefix}.LaunchTemplate"
        )
    if "max_parallel_launches" in value:
        pairs.append(
            (f"{prefix}.MaxParallelLaunches", str(value["max_parallel_launches"]))
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.fast_launch_state_code

        aws_sdk_ec2.types.fast_launch_state_code.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "state_transition_reason" in value:
        pairs.append(
            (f"{prefix}.StateTransitionReason", str(value["state_transition_reason"]))
        )
    if "state_transition_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["state_transition_time"], pairs, f"{prefix}.StateTransitionTime"
        )


def deserialize_ec2_query(el: Element) -> DisableFastLaunchResult:
    out: DisableFastLaunchResult = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.fast_launch_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.fast_launch_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_snapshot_configuration = el.find("SnapshotConfiguration")
    if child_snapshot_configuration is not None:
        import aws_sdk_ec2.types.fast_launch_snapshot_configuration_response

        out["snapshot_configuration"] = (
            aws_sdk_ec2.types.fast_launch_snapshot_configuration_response.deserialize_ec2_query(
                child_snapshot_configuration
            )
        )
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import aws_sdk_ec2.types.fast_launch_launch_template_specification_response

        out["launch_template"] = (
            aws_sdk_ec2.types.fast_launch_launch_template_specification_response.deserialize_ec2_query(
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
        import aws_sdk_ec2.types.fast_launch_state_code

        out["state"] = aws_sdk_ec2.types.fast_launch_state_code.deserialize_ec2_query(
            child_state
        )
    child_state_transition_reason = el.find("StateTransitionReason")
    if child_state_transition_reason is not None:
        out["state_transition_reason"] = str(child_state_transition_reason.text or "")
    child_state_transition_time = el.find("StateTransitionTime")
    if child_state_transition_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["state_transition_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_state_transition_time
            )
        )
    return out
