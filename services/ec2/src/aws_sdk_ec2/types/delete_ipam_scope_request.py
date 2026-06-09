"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamScopeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_scope_id


class DeleteIpamScopeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the scope to delete.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamScopeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_scope_id" in value:
        pairs.append((f"{prefix}.IpamScopeId", str(value["ipam_scope_id"])))


def deserialize_ec2_query(el: Element) -> DeleteIpamScopeRequest:
    out: DeleteIpamScopeRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_scope_id = el.find("IpamScopeId")
    if child_ipam_scope_id is not None:
        out["ipam_scope_id"] = str(child_ipam_scope_id.text or "")
    return out
