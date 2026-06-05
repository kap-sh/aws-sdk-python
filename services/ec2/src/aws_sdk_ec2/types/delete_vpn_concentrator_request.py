"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpnConcentratorRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.vpn_concentrator_id


class DeleteVpnConcentratorRequest(TypedDict):
    vpn_concentrator_id: NotRequired[
        "aws_sdk_ec2.types.vpn_concentrator_id.VpnConcentratorId"
    ]
    """<p>The ID of the VPN concentrator to delete.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteVpnConcentratorRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_concentrator_id" in value:
        pairs.append((f"{prefix}.VpnConcentratorId", str(value["vpn_concentrator_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteVpnConcentratorRequest:
    out: DeleteVpnConcentratorRequest = {}  # type: ignore[typeddict-item]
    child_vpn_concentrator_id = el.find("VpnConcentratorId")
    if child_vpn_concentrator_id is not None:
        out["vpn_concentrator_id"] = str(child_vpn_concentrator_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
