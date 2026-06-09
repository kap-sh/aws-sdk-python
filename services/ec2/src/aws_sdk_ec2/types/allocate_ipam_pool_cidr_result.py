"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateIpamPoolCidrResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_allocation


class AllocateIpamPoolCidrResult(TypedDict):
    ipam_pool_allocation: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation.IpamPoolAllocation"
    ]
    """<p>Information about the allocation created.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AllocateIpamPoolCidrResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_pool_allocation" in value:
        import aws_sdk_ec2.types.ipam_pool_allocation

        aws_sdk_ec2.types.ipam_pool_allocation.serialize_ec2_query(
            value["ipam_pool_allocation"], pairs, f"{prefix}.IpamPoolAllocation"
        )


def deserialize_ec2_query(el: Element) -> AllocateIpamPoolCidrResult:
    out: AllocateIpamPoolCidrResult = {}  # type: ignore[typeddict-item]
    child_ipam_pool_allocation = el.find("IpamPoolAllocation")
    if child_ipam_pool_allocation is not None:
        import aws_sdk_ec2.types.ipam_pool_allocation

        out["ipam_pool_allocation"] = (
            aws_sdk_ec2.types.ipam_pool_allocation.deserialize_ec2_query(
                child_ipam_pool_allocation
            )
        )
    return out
