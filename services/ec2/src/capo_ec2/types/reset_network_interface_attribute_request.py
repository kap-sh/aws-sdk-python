"""Generated from Smithy shape ``com.amazonaws.ec2#ResetNetworkInterfaceAttributeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.string


class ResetNetworkInterfaceAttributeRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    source_dest_check: NotRequired["capo_ec2.types.string.String"]
    """<p>The source/destination checking attribute. Resets the value to <code>true</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResetNetworkInterfaceAttributeRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "source_dest_check" in value:
        pairs.append((f"{key_prefix}SourceDestCheck", str(value["source_dest_check"])))


def deserialize_ec2_query(el: Element) -> ResetNetworkInterfaceAttributeRequest:
    out: ResetNetworkInterfaceAttributeRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_source_dest_check = el.find("SourceDestCheck")
    if child_source_dest_check is not None:
        out["source_dest_check"] = str(child_source_dest_check.text or "")
    return out
