"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionPublicIpv4PoolCidrResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv4_pool_ec2_id
    import capo_ec2.types.public_ipv4_pool_range


class ProvisionPublicIpv4PoolCidrResult(TypedDict, closed=True):
    pool_id: NotRequired["capo_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of the pool that you want to provision the CIDR to.</p>"""
    pool_address_range: NotRequired[
        "capo_ec2.types.public_ipv4_pool_range.PublicIpv4PoolRange"
    ]
    """<p>Information about the address range of the public IPv4 pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProvisionPublicIpv4PoolCidrResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "pool_id" in value:
        pairs.append((f"{prefix}.PoolId", str(value["pool_id"])))
    if "pool_address_range" in value:
        import capo_ec2.types.public_ipv4_pool_range

        capo_ec2.types.public_ipv4_pool_range.serialize_ec2_query(
            value["pool_address_range"], pairs, f"{prefix}.PoolAddressRange"
        )


def deserialize_ec2_query(el: Element) -> ProvisionPublicIpv4PoolCidrResult:
    out: ProvisionPublicIpv4PoolCidrResult = {}  # type: ignore[typeddict-item]
    child_pool_id = el.find("PoolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    child_pool_address_range = el.find("PoolAddressRange")
    if child_pool_address_range is not None:
        import capo_ec2.types.public_ipv4_pool_range

        out["pool_address_range"] = (
            capo_ec2.types.public_ipv4_pool_range.deserialize_ec2_query(
                child_pool_address_range
            )
        )
    return out
