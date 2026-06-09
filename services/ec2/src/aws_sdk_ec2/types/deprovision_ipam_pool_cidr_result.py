"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionIpamPoolCidrResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_cidr


class DeprovisionIpamPoolCidrResult(TypedDict):
    ipam_pool_cidr: NotRequired["aws_sdk_ec2.types.ipam_pool_cidr.IpamPoolCidr"]
    """<p>The deprovisioned pool CIDR.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeprovisionIpamPoolCidrResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_pool_cidr" in value:
        import aws_sdk_ec2.types.ipam_pool_cidr

        aws_sdk_ec2.types.ipam_pool_cidr.serialize_ec2_query(
            value["ipam_pool_cidr"], pairs, f"{prefix}.IpamPoolCidr"
        )


def deserialize_ec2_query(el: Element) -> DeprovisionIpamPoolCidrResult:
    out: DeprovisionIpamPoolCidrResult = {}  # type: ignore[typeddict-item]
    child_ipam_pool_cidr = el.find("IpamPoolCidr")
    if child_ipam_pool_cidr is not None:
        import aws_sdk_ec2.types.ipam_pool_cidr

        out["ipam_pool_cidr"] = aws_sdk_ec2.types.ipam_pool_cidr.deserialize_ec2_query(
            child_ipam_pool_cidr
        )
    return out
