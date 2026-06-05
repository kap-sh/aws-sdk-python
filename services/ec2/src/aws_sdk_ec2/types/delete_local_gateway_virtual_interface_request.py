"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id


class DeleteLocalGatewayVirtualInterfaceRequest(TypedDict):
    local_gateway_virtual_interface_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_id.LocalGatewayVirtualInterfaceId"
    ]
    """<p>The ID of the local virtual interface to delete.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLocalGatewayVirtualInterfaceRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "local_gateway_virtual_interface_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayVirtualInterfaceId",
                str(value["local_gateway_virtual_interface_id"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteLocalGatewayVirtualInterfaceRequest:
    out: DeleteLocalGatewayVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    child_local_gateway_virtual_interface_id = el.find("LocalGatewayVirtualInterfaceId")
    if child_local_gateway_virtual_interface_id is not None:
        out["local_gateway_virtual_interface_id"] = str(
            child_local_gateway_virtual_interface_id.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
