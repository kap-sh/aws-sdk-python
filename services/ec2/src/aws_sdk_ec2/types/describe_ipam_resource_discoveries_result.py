"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamResourceDiscoveriesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_discovery_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamResourceDiscoveriesResult(TypedDict):
    ipam_resource_discoveries: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_set.IpamResourceDiscoverySet"
    ]
    """<p>The resource discoveries.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamResourceDiscoveriesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "ipam_resource_discoveries" in value:
        import aws_sdk_ec2.types.ipam_resource_discovery_set

        aws_sdk_ec2.types.ipam_resource_discovery_set.serialize_ec2_query(
            value["ipam_resource_discoveries"],
            pairs,
            f"{prefix}.IpamResourceDiscoverySet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeIpamResourceDiscoveriesResult:
    out: DescribeIpamResourceDiscoveriesResult = {}  # type: ignore[typeddict-item]
    if el.find("IpamResourceDiscoverySet") is not None:
        import aws_sdk_ec2.types.ipam_resource_discovery_set

        out["ipam_resource_discoveries"] = (
            aws_sdk_ec2.types.ipam_resource_discovery_set.deserialize_ec2_query(
                el, "IpamResourceDiscoverySet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
