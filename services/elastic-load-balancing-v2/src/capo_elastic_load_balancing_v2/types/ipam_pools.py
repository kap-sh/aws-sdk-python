"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#IpamPools``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.ipam_pool_id


class IpamPools(TypedDict, closed=True):
    ipv4_ipam_pool_id: NotRequired[
        "capo_elastic_load_balancing_v2.types.ipam_pool_id.IpamPoolId"
    ]
    """<p>The ID of the IPv4 IPAM pool.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IpamPools, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv4_ipam_pool_id" in value:
        pairs.append((f"{prefix}.Ipv4IpamPoolId", str(value["ipv4_ipam_pool_id"])))


def deserialize_query(el: Element) -> IpamPools:
    out: IpamPools = {}  # type: ignore[typeddict-item]
    child_ipv4_ipam_pool_id = el.find("Ipv4IpamPoolId")
    if child_ipv4_ipam_pool_id is not None:
        out["ipv4_ipam_pool_id"] = str(child_ipv4_ipam_pool_id.text or "")
    return out
