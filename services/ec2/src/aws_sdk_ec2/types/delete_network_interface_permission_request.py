"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInterfacePermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_interface_permission_id


class DeleteNetworkInterfacePermissionRequest(TypedDict):
    network_interface_permission_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_permission_id.NetworkInterfacePermissionId"
    ]
    """<p>The ID of the network interface permission.</p>"""
    force: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specify <code>true</code> to remove the permission even if the network interface is attached to an instance.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkInterfacePermissionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_interface_permission_id" in value:
        pairs.append(
            (
                f"{prefix}.NetworkInterfacePermissionId",
                str(value["network_interface_permission_id"]),
            )
        )
    if "force" in value:
        pairs.append((f"{prefix}.Force", "true" if value["force"] else "false"))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteNetworkInterfacePermissionRequest:
    out: DeleteNetworkInterfacePermissionRequest = {}  # type: ignore[typeddict-item]
    child_network_interface_permission_id = el.find("NetworkInterfacePermissionId")
    if child_network_interface_permission_id is not None:
        out["network_interface_permission_id"] = str(
            child_network_interface_permission_id.text or ""
        )
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
