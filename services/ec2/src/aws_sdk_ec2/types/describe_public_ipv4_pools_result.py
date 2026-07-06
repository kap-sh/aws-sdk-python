"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePublicIpv4PoolsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.public_ipv4_pool_set
    import aws_sdk_ec2.types.string


class DescribePublicIpv4PoolsResult(TypedDict, closed=True):
    public_ipv4_pools: NotRequired[
        "aws_sdk_ec2.types.public_ipv4_pool_set.PublicIpv4PoolSet"
    ]
    """<p>Information about the address pools.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribePublicIpv4PoolsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "public_ipv4_pools" in value:
        import aws_sdk_ec2.types.public_ipv4_pool_set

        aws_sdk_ec2.types.public_ipv4_pool_set.serialize_ec2_query(
            value["public_ipv4_pools"], pairs, f"{prefix}.PublicIpv4PoolSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribePublicIpv4PoolsResult:
    out: DescribePublicIpv4PoolsResult = {}  # type: ignore[typeddict-item]
    if el.find("PublicIpv4PoolSet") is not None:
        import aws_sdk_ec2.types.public_ipv4_pool_set

        out["public_ipv4_pools"] = (
            aws_sdk_ec2.types.public_ipv4_pool_set.deserialize_ec2_query(
                el, "PublicIpv4PoolSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
