"""Generated from Smithy shape ``com.amazonaws.ec2#EnableImageDeregistrationProtectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.image_id


class EnableImageDeregistrationProtectionRequest(TypedDict, closed=True):
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    with_cooldown: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, enforces deregistration protection for 24 hours after deregistration protection is disabled.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableImageDeregistrationProtectionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "with_cooldown" in value:
        pairs.append(
            (f"{prefix}.WithCooldown", "true" if value["with_cooldown"] else "false")
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> EnableImageDeregistrationProtectionRequest:
    out: EnableImageDeregistrationProtectionRequest = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_with_cooldown = el.find("WithCooldown")
    if child_with_cooldown is not None:
        out["with_cooldown"] = (child_with_cooldown.text or "").lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
