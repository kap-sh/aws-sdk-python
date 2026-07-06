"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id


class DeregisterImageRequest(TypedDict, closed=True):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    delete_associated_snapshots: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to delete the snapshots associated with the AMI during deregistration.</p> <note> <p>If a snapshot is associated with multiple AMIs, it is not deleted, regardless of this setting.</p> </note> <p>Default: The snapshots are not deleted.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeregisterImageRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "delete_associated_snapshots" in value:
        pairs.append(
            (
                f"{prefix}.DeleteAssociatedSnapshots",
                "true" if value["delete_associated_snapshots"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeregisterImageRequest:
    out: DeregisterImageRequest = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_delete_associated_snapshots = el.find("DeleteAssociatedSnapshots")
    if child_delete_associated_snapshots is not None:
        out["delete_associated_snapshots"] = (
            child_delete_associated_snapshots.text or ""
        ).lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
