"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreAddressToClassicRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class RestoreAddressToClassicRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    public_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The Elastic IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RestoreAddressToClassicRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "public_ip" in value:
        pairs.append((f"{key_prefix}PublicIp", str(value["public_ip"])))


def deserialize_ec2_query(el: Element) -> RestoreAddressToClassicRequest:
    out: RestoreAddressToClassicRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_public_ip = el.find("publicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    return out
