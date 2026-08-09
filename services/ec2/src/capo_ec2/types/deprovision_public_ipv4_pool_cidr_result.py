"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionPublicIpv4PoolCidrResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.deprovisioned_address_set
    import capo_ec2.types.ipv4_pool_ec2_id


class DeprovisionPublicIpv4PoolCidrResult(TypedDict, closed=True):
    pool_id: NotRequired["capo_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of the pool that you deprovisioned the CIDR from.</p>"""
    deprovisioned_addresses: NotRequired[
        "capo_ec2.types.deprovisioned_address_set.DeprovisionedAddressSet"
    ]
    """<p>The deprovisioned CIDRs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeprovisionPublicIpv4PoolCidrResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pool_id" in value:
        pairs.append((f"{key_prefix}PoolId", str(value["pool_id"])))
    if "deprovisioned_addresses" in value:
        import capo_ec2.types.deprovisioned_address_set

        capo_ec2.types.deprovisioned_address_set.serialize_ec2_query(
            value["deprovisioned_addresses"],
            pairs,
            f"{key_prefix}DeprovisionedAddressSet",
        )


def deserialize_ec2_query(el: Element) -> DeprovisionPublicIpv4PoolCidrResult:
    out: DeprovisionPublicIpv4PoolCidrResult = {}  # type: ignore[typeddict-item]
    child_pool_id = el.find("poolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    child_deprovisioned_addresses = el.find("deprovisionedAddressSet")
    if child_deprovisioned_addresses is not None:
        import capo_ec2.types.deprovisioned_address_set

        out["deprovisioned_addresses"] = (
            capo_ec2.types.deprovisioned_address_set.deserialize_ec2_query(
                child_deprovisioned_addresses
            )
        )
    return out
