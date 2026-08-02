"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPoolResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_pool


class ModifyIpamPoolResult(TypedDict, closed=True):
    ipam_pool: NotRequired["capo_ec2.types.ipam_pool.IpamPool"]
    """<p>The results of the modification.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamPoolResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_pool" in value:
        import capo_ec2.types.ipam_pool

        capo_ec2.types.ipam_pool.serialize_ec2_query(
            value["ipam_pool"], pairs, f"{key_prefix}IpamPool"
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamPoolResult:
    out: ModifyIpamPoolResult = {}  # type: ignore[typeddict-item]
    child_ipam_pool = el.find("IpamPool")
    if child_ipam_pool is not None:
        import capo_ec2.types.ipam_pool

        out["ipam_pool"] = capo_ec2.types.ipam_pool.deserialize_ec2_query(
            child_ipam_pool
        )
    return out
