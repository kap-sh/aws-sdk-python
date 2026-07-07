"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteDhcpOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dhcp_options_id


class DeleteDhcpOptionsRequest(TypedDict, closed=True):
    dhcp_options_id: NotRequired["aws_sdk_ec2.types.dhcp_options_id.DhcpOptionsId"]
    """<p>The ID of the DHCP options set.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteDhcpOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dhcp_options_id" in value:
        pairs.append((f"{prefix}.DhcpOptionsId", str(value["dhcp_options_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteDhcpOptionsRequest:
    out: DeleteDhcpOptionsRequest = {}  # type: ignore[typeddict-item]
    child_dhcp_options_id = el.find("DhcpOptionsId")
    if child_dhcp_options_id is not None:
        out["dhcp_options_id"] = str(child_dhcp_options_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
