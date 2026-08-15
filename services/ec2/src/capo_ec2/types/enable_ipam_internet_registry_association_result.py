"""Generated from Smithy shape ``com.amazonaws.ec2#EnableIpamInternetRegistryAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_internet_registry_association


class EnableIpamInternetRegistryAssociationResult(TypedDict, closed=True):
    ipam_internet_registry_association: NotRequired[
        "capo_ec2.types.ipam_internet_registry_association.IpamInternetRegistryAssociation"
    ]
    """<p>Information about the enabled internet registry association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableIpamInternetRegistryAssociationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_internet_registry_association" in value:
        import capo_ec2.types.ipam_internet_registry_association

        capo_ec2.types.ipam_internet_registry_association.serialize_ec2_query(
            value["ipam_internet_registry_association"],
            pairs,
            f"{key_prefix}IpamInternetRegistryAssociation",
        )


def deserialize_ec2_query(el: Element) -> EnableIpamInternetRegistryAssociationResult:
    out: EnableIpamInternetRegistryAssociationResult = {}  # type: ignore[typeddict-item]
    child_ipam_internet_registry_association = el.find(
        "ipamInternetRegistryAssociation"
    )
    if child_ipam_internet_registry_association is not None:
        import capo_ec2.types.ipam_internet_registry_association

        out["ipam_internet_registry_association"] = (
            capo_ec2.types.ipam_internet_registry_association.deserialize_ec2_query(
                child_ipam_internet_registry_association
            )
        )
    return out
