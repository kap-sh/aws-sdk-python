"""Generated from Smithy shape ``com.amazonaws.ec2#EnableVolumeIORequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.volume_id


class EnableVolumeIORequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableVolumeIORequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "volume_id" in value:
        pairs.append((f"{prefix}.VolumeId", str(value["volume_id"])))


def deserialize_ec2_query(el: Element) -> EnableVolumeIORequest:
    out: EnableVolumeIORequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    return out
