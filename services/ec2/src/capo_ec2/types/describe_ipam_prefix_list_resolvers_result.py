"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPrefixListResolversResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_set
    import capo_ec2.types.next_token


class DescribeIpamPrefixListResolversResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_prefix_list_resolvers: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_set.IpamPrefixListResolverSet"
    ]
    """<p>Information about the IPAM prefix list resolvers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamPrefixListResolversResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "ipam_prefix_list_resolvers" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_set

        capo_ec2.types.ipam_prefix_list_resolver_set.serialize_ec2_query(
            value["ipam_prefix_list_resolvers"],
            pairs,
            f"{key_prefix}IpamPrefixListResolverSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeIpamPrefixListResolversResult:
    out: DescribeIpamPrefixListResolversResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("ipamPrefixListResolverSet") is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_set

        out["ipam_prefix_list_resolvers"] = (
            capo_ec2.types.ipam_prefix_list_resolver_set.deserialize_ec2_query(
                el, "ipamPrefixListResolverSet"
            )
        )
    return out
