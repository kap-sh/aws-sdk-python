"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPoolResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool


class DeleteIpamPoolResult(TypedDict):
    ipam_pool: NotRequired["aws_sdk_ec2.types.ipam_pool.IpamPool"]
    """<p>Information about the results of the deletion.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamPoolResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_pool" in value:
        import aws_sdk_ec2.types.ipam_pool

        aws_sdk_ec2.types.ipam_pool.serialize_ec2_query(
            value["ipam_pool"], pairs, f"{prefix}.IpamPool"
        )


def deserialize_ec2_query(el: Element) -> DeleteIpamPoolResult:
    out: DeleteIpamPoolResult = {}  # type: ignore[typeddict-item]
    child_ipam_pool = el.find("IpamPool")
    if child_ipam_pool is not None:
        import aws_sdk_ec2.types.ipam_pool

        out["ipam_pool"] = aws_sdk_ec2.types.ipam_pool.deserialize_ec2_query(
            child_ipam_pool
        )
    return out
