"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPrefixListResolverTargetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamPrefixListResolverTargetsResult(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_prefix_list_resolver_targets: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_target_set.IpamPrefixListResolverTargetSet"
    ]
    """<p>Information about the IPAM prefix list resolver Targets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamPrefixListResolverTargetsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "ipam_prefix_list_resolver_targets" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_set

        aws_sdk_ec2.types.ipam_prefix_list_resolver_target_set.serialize_ec2_query(
            value["ipam_prefix_list_resolver_targets"],
            pairs,
            f"{prefix}.IpamPrefixListResolverTargetSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeIpamPrefixListResolverTargetsResult:
    out: DescribeIpamPrefixListResolverTargetsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("IpamPrefixListResolverTargetSet") is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_set

        out["ipam_prefix_list_resolver_targets"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_target_set.deserialize_ec2_query(
                el, "IpamPrefixListResolverTargetSet"
            )
        )
    return out
