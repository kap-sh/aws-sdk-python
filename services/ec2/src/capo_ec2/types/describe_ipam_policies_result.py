"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPoliciesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_set
    import capo_ec2.types.next_token


class DescribeIpamPoliciesResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_policies: NotRequired["capo_ec2.types.ipam_policy_set.IpamPolicySet"]
    """<p>Information about the IPAM policies.</p> <p>An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamPoliciesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "ipam_policies" in value:
        import capo_ec2.types.ipam_policy_set

        capo_ec2.types.ipam_policy_set.serialize_ec2_query(
            value["ipam_policies"], pairs, f"{key_prefix}IpamPolicySet"
        )


def deserialize_ec2_query(el: Element) -> DescribeIpamPoliciesResult:
    out: DescribeIpamPoliciesResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("ipamPolicySet") is not None:
        import capo_ec2.types.ipam_policy_set

        out["ipam_policies"] = capo_ec2.types.ipam_policy_set.deserialize_ec2_query(
            el, "ipamPolicySet"
        )
    return out
