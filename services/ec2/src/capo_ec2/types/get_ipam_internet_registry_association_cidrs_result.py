"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamInternetRegistryAssociationCidrsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_internet_registry_association_cidr_set
    import capo_ec2.types.next_token


class GetIpamInternetRegistryAssociationCidrsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    ipam_internet_registry_association_cidrs: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association_cidr_set.IpamInternetRegistryAssociationCidrSet"
    ]
    """<p>The CIDRs registered with the internet registry.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamInternetRegistryAssociationCidrsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "ipam_internet_registry_association_cidrs" in value:
        import capo_ec2.types.ipam_internet_registry_association_cidr_set

        capo_ec2.types.ipam_internet_registry_association_cidr_set.serialize_ec2_query(
            value["ipam_internet_registry_association_cidrs"],
            pairs,
            f"{key_prefix}IpamInternetRegistryAssociationCidrSet",
        )


def deserialize_ec2_query(el: Element) -> GetIpamInternetRegistryAssociationCidrsResult:
    out: GetIpamInternetRegistryAssociationCidrsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_ipam_internet_registry_association_cidrs = el.find(
        "ipamInternetRegistryAssociationCidrSet"
    )
    if child_ipam_internet_registry_association_cidrs is not None:
        import capo_ec2.types.ipam_internet_registry_association_cidr_set

        out["ipam_internet_registry_association_cidrs"] = (
            capo_ec2.types.ipam_internet_registry_association_cidr_set.deserialize_ec2_query(
                child_ipam_internet_registry_association_cidrs
            )
        )
    return out
