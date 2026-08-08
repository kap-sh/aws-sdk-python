"""Generated from Smithy shape ``com.amazonaws.ec2#CreatePublicIpv4PoolResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv4_pool_ec2_id


class CreatePublicIpv4PoolResult(TypedDict, closed=True):
    pool_id: NotRequired["capo_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of the public IPv4 pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreatePublicIpv4PoolResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pool_id" in value:
        pairs.append((f"{key_prefix}PoolId", str(value["pool_id"])))


def deserialize_ec2_query(el: Element) -> CreatePublicIpv4PoolResult:
    out: CreatePublicIpv4PoolResult = {}  # type: ignore[typeddict-item]
    child_pool_id = el.find("poolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    return out
