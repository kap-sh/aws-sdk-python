"""Generated from Smithy shape ``com.amazonaws.ec2#GetAssociatedIpv6PoolCidrsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_cidr_association_set
    import aws_sdk_ec2.types.string


class GetAssociatedIpv6PoolCidrsResult(TypedDict):
    ipv6_cidr_associations: NotRequired[
        "aws_sdk_ec2.types.ipv6_cidr_association_set.Ipv6CidrAssociationSet"
    ]
    """<p>Information about the IPv6 CIDR block associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetAssociatedIpv6PoolCidrsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_cidr_associations" in value:
        import aws_sdk_ec2.types.ipv6_cidr_association_set

        aws_sdk_ec2.types.ipv6_cidr_association_set.serialize_ec2_query(
            value["ipv6_cidr_associations"], pairs, f"{prefix}.Ipv6CidrAssociationSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetAssociatedIpv6PoolCidrsResult:
    out: GetAssociatedIpv6PoolCidrsResult = {}  # type: ignore[typeddict-item]
    if el.find("Ipv6CidrAssociationSet") is not None:
        import aws_sdk_ec2.types.ipv6_cidr_association_set

        out["ipv6_cidr_associations"] = (
            aws_sdk_ec2.types.ipv6_cidr_association_set.deserialize_ec2_query(
                el, "Ipv6CidrAssociationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
