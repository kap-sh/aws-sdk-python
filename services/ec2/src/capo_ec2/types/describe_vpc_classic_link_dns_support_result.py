"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcClassicLinkDnsSupportResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.classic_link_dns_support_list
    import capo_ec2.types.describe_vpc_classic_link_dns_support_next_token


class DescribeVpcClassicLinkDnsSupportResult(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_ec2.types.describe_vpc_classic_link_dns_support_next_token.DescribeVpcClassicLinkDnsSupportNextToken"
    ]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    vpcs: NotRequired[
        "capo_ec2.types.classic_link_dns_support_list.ClassicLinkDnsSupportList"
    ]
    """<p>Information about the ClassicLink DNS support status of the VPCs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcClassicLinkDnsSupportResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "vpcs" in value:
        import capo_ec2.types.classic_link_dns_support_list

        capo_ec2.types.classic_link_dns_support_list.serialize_ec2_query(
            value["vpcs"], pairs, f"{key_prefix}Vpcs"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpcClassicLinkDnsSupportResult:
    out: DescribeVpcClassicLinkDnsSupportResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("Vpcs") is not None:
        import capo_ec2.types.classic_link_dns_support_list

        out["vpcs"] = (
            capo_ec2.types.classic_link_dns_support_list.deserialize_ec2_query(
                el, "Vpcs"
            )
        )
    return out
