"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPrefixListResolverTargetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_target_set
    import capo_ec2.types.next_token


class DescribeIpamPrefixListResolverTargetsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_prefix_list_resolver_targets: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_target_set.IpamPrefixListResolverTargetSet"
    ]
    """<p>Information about the IPAM prefix list resolver Targets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamPrefixListResolverTargetsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "ipam_prefix_list_resolver_targets" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_target_set

        capo_ec2.types.ipam_prefix_list_resolver_target_set.serialize_ec2_query(
            value["ipam_prefix_list_resolver_targets"],
            pairs,
            f"{key_prefix}IpamPrefixListResolverTargetSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeIpamPrefixListResolverTargetsResult:
    out: DescribeIpamPrefixListResolverTargetsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_ipam_prefix_list_resolver_targets = el.find("ipamPrefixListResolverTargetSet")
    if child_ipam_prefix_list_resolver_targets is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_target_set

        out["ipam_prefix_list_resolver_targets"] = (
            capo_ec2.types.ipam_prefix_list_resolver_target_set.deserialize_ec2_query(
                child_ipam_prefix_list_resolver_targets
            )
        )
    return out
