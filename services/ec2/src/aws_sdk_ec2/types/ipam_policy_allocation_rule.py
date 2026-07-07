"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyAllocationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_id


class IpamPolicyAllocationRule(TypedDict, closed=True):
    source_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the source IPAM pool for the allocation rule.</p> <p>An IPAM pool is a collection of IP addresses in IPAM that can be allocated to Amazon Web Services resources.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicyAllocationRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_ipam_pool_id" in value:
        pairs.append((f"{prefix}.SourceIpamPoolId", str(value["source_ipam_pool_id"])))


def deserialize_ec2_query(el: Element) -> IpamPolicyAllocationRule:
    out: IpamPolicyAllocationRule = {}  # type: ignore[typeddict-item]
    child_source_ipam_pool_id = el.find("SourceIpamPoolId")
    if child_source_ipam_pool_id is not None:
        out["source_ipam_pool_id"] = str(child_source_ipam_pool_id.text or "")
    return out
