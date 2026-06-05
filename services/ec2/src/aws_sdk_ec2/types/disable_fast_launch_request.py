"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastLaunchRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id


class DisableFastLaunchRequest(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>Specify the ID of the image for which to disable Windows fast launch.</p>"""
    force: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Forces the image settings to turn off Windows fast launch for your Windows AMI. This parameter overrides any errors that are encountered while cleaning up resources in your account.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableFastLaunchRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "force" in value:
        pairs.append((f"{prefix}.Force", "true" if value["force"] else "false"))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DisableFastLaunchRequest:
    out: DisableFastLaunchRequest = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
