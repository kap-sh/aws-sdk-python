"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastLaunchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fast_launch_launch_template_specification_request
    import aws_sdk_ec2.types.fast_launch_snapshot_configuration_request
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class EnableFastLaunchRequest(TypedDict, closed=True):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>Specify the ID of the image for which to enable Windows fast launch.</p>"""
    resource_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of resource to use for pre-provisioning the AMI for Windows fast launch. Supported values include: <code>snapshot</code>, which is the default value.</p>"""
    snapshot_configuration: NotRequired[
        "aws_sdk_ec2.types.fast_launch_snapshot_configuration_request.FastLaunchSnapshotConfigurationRequest"
    ]
    """<p>Configuration settings for creating and managing the snapshots that are used for pre-provisioning the AMI for Windows fast launch. The associated <code>ResourceType</code> must be <code>snapshot</code>.</p>"""
    launch_template: NotRequired[
        "aws_sdk_ec2.types.fast_launch_launch_template_specification_request.FastLaunchLaunchTemplateSpecificationRequest"
    ]
    """<p>The launch template to use when launching Windows instances from pre-provisioned snapshots. Launch template parameters can include either the name or ID of the launch template, but not both.</p>"""
    max_parallel_launches: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of instances that Amazon EC2 can launch at the same time to create pre-provisioned snapshots for Windows fast launch. Value must be <code>6</code> or greater.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableFastLaunchRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "snapshot_configuration" in value:
        import aws_sdk_ec2.types.fast_launch_snapshot_configuration_request

        aws_sdk_ec2.types.fast_launch_snapshot_configuration_request.serialize_ec2_query(
            value["snapshot_configuration"], pairs, f"{prefix}.SnapshotConfiguration"
        )
    if "launch_template" in value:
        import aws_sdk_ec2.types.fast_launch_launch_template_specification_request

        aws_sdk_ec2.types.fast_launch_launch_template_specification_request.serialize_ec2_query(
            value["launch_template"], pairs, f"{prefix}.LaunchTemplate"
        )
    if "max_parallel_launches" in value:
        pairs.append(
            (f"{prefix}.MaxParallelLaunches", str(value["max_parallel_launches"]))
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableFastLaunchRequest:
    out: EnableFastLaunchRequest = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_snapshot_configuration = el.find("SnapshotConfiguration")
    if child_snapshot_configuration is not None:
        import aws_sdk_ec2.types.fast_launch_snapshot_configuration_request

        out["snapshot_configuration"] = (
            aws_sdk_ec2.types.fast_launch_snapshot_configuration_request.deserialize_ec2_query(
                child_snapshot_configuration
            )
        )
    child_launch_template = el.find("LaunchTemplate")
    if child_launch_template is not None:
        import aws_sdk_ec2.types.fast_launch_launch_template_specification_request

        out["launch_template"] = (
            aws_sdk_ec2.types.fast_launch_launch_template_specification_request.deserialize_ec2_query(
                child_launch_template
            )
        )
    child_max_parallel_launches = el.find("MaxParallelLaunches")
    if child_max_parallel_launches is not None:
        out["max_parallel_launches"] = int(child_max_parallel_launches.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
