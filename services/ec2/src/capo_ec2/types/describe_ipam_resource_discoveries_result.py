"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamResourceDiscoveriesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_resource_discovery_set
    import capo_ec2.types.next_token


class DescribeIpamResourceDiscoveriesResult(TypedDict, closed=True):
    ipam_resource_discoveries: NotRequired[
        "capo_ec2.types.ipam_resource_discovery_set.IpamResourceDiscoverySet"
    ]
    """<p>The resource discoveries.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamResourceDiscoveriesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_resource_discoveries" in value:
        import capo_ec2.types.ipam_resource_discovery_set

        capo_ec2.types.ipam_resource_discovery_set.serialize_ec2_query(
            value["ipam_resource_discoveries"],
            pairs,
            f"{key_prefix}IpamResourceDiscoverySet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeIpamResourceDiscoveriesResult:
    out: DescribeIpamResourceDiscoveriesResult = {}  # type: ignore[typeddict-item]
    child_ipam_resource_discoveries = el.find("ipamResourceDiscoverySet")
    if child_ipam_resource_discoveries is not None:
        import capo_ec2.types.ipam_resource_discovery_set

        out["ipam_resource_discoveries"] = (
            capo_ec2.types.ipam_resource_discovery_set.deserialize_ec2_query(
                child_ipam_resource_discoveries
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
