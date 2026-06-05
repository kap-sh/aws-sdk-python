"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamResourceDiscoveryAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_discovery_association_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamResourceDiscoveryAssociationsResult(TypedDict):
    ipam_resource_discovery_associations: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_association_set.IpamResourceDiscoveryAssociationSet"
    ]
    """<p>The resource discovery associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamResourceDiscoveryAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "ipam_resource_discovery_associations" in value:
        import aws_sdk_ec2.types.ipam_resource_discovery_association_set

        aws_sdk_ec2.types.ipam_resource_discovery_association_set.serialize_ec2_query(
            value["ipam_resource_discovery_associations"],
            pairs,
            f"{prefix}.IpamResourceDiscoveryAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeIpamResourceDiscoveryAssociationsResult:
    out: DescribeIpamResourceDiscoveryAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("IpamResourceDiscoveryAssociationSet") is not None:
        import aws_sdk_ec2.types.ipam_resource_discovery_association_set

        out["ipam_resource_discovery_associations"] = (
            aws_sdk_ec2.types.ipam_resource_discovery_association_set.deserialize_ec2_query(
                el, "IpamResourceDiscoveryAssociationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
