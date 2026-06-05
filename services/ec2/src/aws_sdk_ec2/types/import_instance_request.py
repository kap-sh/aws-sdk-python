"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.disk_image_list
    import aws_sdk_ec2.types.import_instance_launch_specification
    import aws_sdk_ec2.types.platform_values
    import aws_sdk_ec2.types.string


class ImportInstanceRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the instance being imported.</p>"""
    launch_specification: NotRequired[
        "aws_sdk_ec2.types.import_instance_launch_specification.ImportInstanceLaunchSpecification"
    ]
    """<p>The launch specification.</p>"""
    disk_images: NotRequired["aws_sdk_ec2.types.disk_image_list.DiskImageList"]
    """<p>The disk image.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.platform_values.PlatformValues"]
    """<p>The instance operating system.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportInstanceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "launch_specification" in value:
        import aws_sdk_ec2.types.import_instance_launch_specification

        aws_sdk_ec2.types.import_instance_launch_specification.serialize_ec2_query(
            value["launch_specification"], pairs, f"{prefix}.LaunchSpecification"
        )
    if "disk_images" in value:
        import aws_sdk_ec2.types.disk_image_list

        aws_sdk_ec2.types.disk_image_list.serialize_ec2_query(
            value["disk_images"], pairs, f"{prefix}.DiskImage"
        )
    if "platform" in value:
        import aws_sdk_ec2.types.platform_values

        aws_sdk_ec2.types.platform_values.serialize_ec2_query(
            value["platform"], pairs, f"{prefix}.Platform"
        )


def deserialize_ec2_query(el: Element) -> ImportInstanceRequest:
    out: ImportInstanceRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_launch_specification = el.find("LaunchSpecification")
    if child_launch_specification is not None:
        import aws_sdk_ec2.types.import_instance_launch_specification

        out["launch_specification"] = (
            aws_sdk_ec2.types.import_instance_launch_specification.deserialize_ec2_query(
                child_launch_specification
            )
        )
    if el.find("DiskImage") is not None:
        import aws_sdk_ec2.types.disk_image_list

        out["disk_images"] = aws_sdk_ec2.types.disk_image_list.deserialize_ec2_query(
            el, "DiskImage"
        )
    child_platform = el.find("Platform")
    if child_platform is not None:
        import aws_sdk_ec2.types.platform_values

        out["platform"] = aws_sdk_ec2.types.platform_values.deserialize_ec2_query(
            child_platform
        )
    return out
