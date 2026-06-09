"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPrefixListResolversResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamPrefixListResolversResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_prefix_list_resolvers: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_set.IpamPrefixListResolverSet"
    ]
    """<p>Information about the IPAM prefix list resolvers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamPrefixListResolversResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "ipam_prefix_list_resolvers" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_set

        aws_sdk_ec2.types.ipam_prefix_list_resolver_set.serialize_ec2_query(
            value["ipam_prefix_list_resolvers"],
            pairs,
            f"{prefix}.IpamPrefixListResolverSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeIpamPrefixListResolversResult:
    out: DescribeIpamPrefixListResolversResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("IpamPrefixListResolverSet") is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_set

        out["ipam_prefix_list_resolvers"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_set.deserialize_ec2_query(
                el, "IpamPrefixListResolverSet"
            )
        )
    return out
