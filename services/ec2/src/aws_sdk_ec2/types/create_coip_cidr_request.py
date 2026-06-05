"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCoipCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipv4_pool_coip_id
    import aws_sdk_ec2.types.string


class CreateCoipCidrRequest(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> A customer-owned IP address range to create. </p>"""
    coip_pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
    """<p> The ID of the address pool. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCoipCidrRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "coip_pool_id" in value:
        pairs.append((f"{prefix}.CoipPoolId", str(value["coip_pool_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateCoipCidrRequest:
    out: CreateCoipCidrRequest = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_coip_pool_id = el.find("CoipPoolId")
    if child_coip_pool_id is not None:
        out["coip_pool_id"] = str(child_coip_pool_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
