"""Generated from Smithy shape ``com.amazonaws.ec2#GetAssociatedIpv6PoolCidrsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv6_cidr_association_set
    import capo_ec2.types.string


class GetAssociatedIpv6PoolCidrsResult(TypedDict, closed=True):
    ipv6_cidr_associations: NotRequired[
        "capo_ec2.types.ipv6_cidr_association_set.Ipv6CidrAssociationSet"
    ]
    """<p>Information about the IPv6 CIDR block associations.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetAssociatedIpv6PoolCidrsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv6_cidr_associations" in value:
        import capo_ec2.types.ipv6_cidr_association_set

        capo_ec2.types.ipv6_cidr_association_set.serialize_ec2_query(
            value["ipv6_cidr_associations"],
            pairs,
            f"{key_prefix}Ipv6CidrAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetAssociatedIpv6PoolCidrsResult:
    out: GetAssociatedIpv6PoolCidrsResult = {}  # type: ignore[typeddict-item]
    if el.find("Ipv6CidrAssociationSet") is not None:
        import capo_ec2.types.ipv6_cidr_association_set

        out["ipv6_cidr_associations"] = (
            capo_ec2.types.ipv6_cidr_association_set.deserialize_ec2_query(
                el, "Ipv6CidrAssociationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
