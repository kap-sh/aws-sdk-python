"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPoolAllocationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_allocation


class ModifyIpamPoolAllocationResult(TypedDict):
    ipam_pool_allocation: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation.IpamPoolAllocation"
    ]
    """<p>The modified IPAM pool allocation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamPoolAllocationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_pool_allocation" in value:
        import aws_sdk_ec2.types.ipam_pool_allocation

        aws_sdk_ec2.types.ipam_pool_allocation.serialize_ec2_query(
            value["ipam_pool_allocation"], pairs, f"{prefix}.IpamPoolAllocation"
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamPoolAllocationResult:
    out: ModifyIpamPoolAllocationResult = {}  # type: ignore[typeddict-item]
    child_ipam_pool_allocation = el.find("IpamPoolAllocation")
    if child_ipam_pool_allocation is not None:
        import aws_sdk_ec2.types.ipam_pool_allocation

        out["ipam_pool_allocation"] = (
            aws_sdk_ec2.types.ipam_pool_allocation.deserialize_ec2_query(
                child_ipam_pool_allocation
            )
        )
    return out
