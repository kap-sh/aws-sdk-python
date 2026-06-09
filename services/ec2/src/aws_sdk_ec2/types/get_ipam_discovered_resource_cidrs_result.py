"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamDiscoveredResourceCidrsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovered_resource_cidr_set
    import aws_sdk_ec2.types.next_token


class GetIpamDiscoveredResourceCidrsResult(TypedDict):
    ipam_discovered_resource_cidrs: NotRequired[
        "aws_sdk_ec2.types.ipam_discovered_resource_cidr_set.IpamDiscoveredResourceCidrSet"
    ]
    """<p>Discovered resource CIDRs.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamDiscoveredResourceCidrsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "ipam_discovered_resource_cidrs" in value:
        import aws_sdk_ec2.types.ipam_discovered_resource_cidr_set

        aws_sdk_ec2.types.ipam_discovered_resource_cidr_set.serialize_ec2_query(
            value["ipam_discovered_resource_cidrs"],
            pairs,
            f"{prefix}.IpamDiscoveredResourceCidrSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamDiscoveredResourceCidrsResult:
    out: GetIpamDiscoveredResourceCidrsResult = {}  # type: ignore[typeddict-item]
    if el.find("IpamDiscoveredResourceCidrSet") is not None:
        import aws_sdk_ec2.types.ipam_discovered_resource_cidr_set

        out["ipam_discovered_resource_cidrs"] = (
            aws_sdk_ec2.types.ipam_discovered_resource_cidr_set.deserialize_ec2_query(
                el, "IpamDiscoveredResourceCidrSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
