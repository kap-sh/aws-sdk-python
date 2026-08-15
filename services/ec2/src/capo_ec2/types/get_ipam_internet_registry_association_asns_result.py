"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamInternetRegistryAssociationAsnsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_internet_registry_association_asn_set
    import capo_ec2.types.next_token


class GetIpamInternetRegistryAssociationAsnsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    ipam_internet_registry_association_asns: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association_asn_set.IpamInternetRegistryAssociationAsnSet"
    ]
    """<p>The ASNs registered with the internet registry.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamInternetRegistryAssociationAsnsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "ipam_internet_registry_association_asns" in value:
        import capo_ec2.types.ipam_internet_registry_association_asn_set

        capo_ec2.types.ipam_internet_registry_association_asn_set.serialize_ec2_query(
            value["ipam_internet_registry_association_asns"],
            pairs,
            f"{key_prefix}IpamInternetRegistryAssociationAsnSet",
        )


def deserialize_ec2_query(el: Element) -> GetIpamInternetRegistryAssociationAsnsResult:
    out: GetIpamInternetRegistryAssociationAsnsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_ipam_internet_registry_association_asns = el.find(
        "ipamInternetRegistryAssociationAsnSet"
    )
    if child_ipam_internet_registry_association_asns is not None:
        import capo_ec2.types.ipam_internet_registry_association_asn_set

        out["ipam_internet_registry_association_asns"] = (
            capo_ec2.types.ipam_internet_registry_association_asn_set.deserialize_ec2_query(
                child_ipam_internet_registry_association_asns
            )
        )
    return out
