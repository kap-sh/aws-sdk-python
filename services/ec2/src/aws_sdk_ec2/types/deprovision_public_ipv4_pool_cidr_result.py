"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionPublicIpv4PoolCidrResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.deprovisioned_address_set
    import aws_sdk_ec2.types.ipv4_pool_ec2_id


class DeprovisionPublicIpv4PoolCidrResult(TypedDict, closed=True):
    pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of the pool that you deprovisioned the CIDR from.</p>"""
    deprovisioned_addresses: NotRequired[
        "aws_sdk_ec2.types.deprovisioned_address_set.DeprovisionedAddressSet"
    ]
    """<p>The deprovisioned CIDRs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeprovisionPublicIpv4PoolCidrResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "pool_id" in value:
        pairs.append((f"{prefix}.PoolId", str(value["pool_id"])))
    if "deprovisioned_addresses" in value:
        import aws_sdk_ec2.types.deprovisioned_address_set

        aws_sdk_ec2.types.deprovisioned_address_set.serialize_ec2_query(
            value["deprovisioned_addresses"], pairs, f"{prefix}.DeprovisionedAddressSet"
        )


def deserialize_ec2_query(el: Element) -> DeprovisionPublicIpv4PoolCidrResult:
    out: DeprovisionPublicIpv4PoolCidrResult = {}  # type: ignore[typeddict-item]
    child_pool_id = el.find("PoolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    if el.find("DeprovisionedAddressSet") is not None:
        import aws_sdk_ec2.types.deprovisioned_address_set

        out["deprovisioned_addresses"] = (
            aws_sdk_ec2.types.deprovisioned_address_set.deserialize_ec2_query(
                el, "DeprovisionedAddressSet"
            )
        )
    return out
