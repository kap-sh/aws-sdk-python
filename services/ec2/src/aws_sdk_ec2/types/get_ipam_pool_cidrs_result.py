"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPoolCidrsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_cidr_set
    import aws_sdk_ec2.types.next_token


class GetIpamPoolCidrsResult(TypedDict):
    ipam_pool_cidrs: NotRequired["aws_sdk_ec2.types.ipam_pool_cidr_set.IpamPoolCidrSet"]
    """<p>Information about the CIDRs provisioned to an IPAM pool.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPoolCidrsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_pool_cidrs" in value:
        import aws_sdk_ec2.types.ipam_pool_cidr_set

        aws_sdk_ec2.types.ipam_pool_cidr_set.serialize_ec2_query(
            value["ipam_pool_cidrs"], pairs, f"{prefix}.IpamPoolCidrSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPoolCidrsResult:
    out: GetIpamPoolCidrsResult = {}  # type: ignore[typeddict-item]
    if el.find("IpamPoolCidrSet") is not None:
        import aws_sdk_ec2.types.ipam_pool_cidr_set

        out["ipam_pool_cidrs"] = (
            aws_sdk_ec2.types.ipam_pool_cidr_set.deserialize_ec2_query(
                el, "IpamPoolCidrSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
