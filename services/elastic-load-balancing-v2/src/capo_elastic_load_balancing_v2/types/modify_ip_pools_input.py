"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ModifyIpPoolsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.ipam_pools
    import capo_elastic_load_balancing_v2.types.load_balancer_arn
    import capo_elastic_load_balancing_v2.types.remove_ipam_pools


class ModifyIpPoolsInput(TypedDict, closed=True):
    load_balancer_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    ipam_pools: NotRequired["capo_elastic_load_balancing_v2.types.ipam_pools.IpamPools"]
    """<p>The IPAM pools to be modified.</p>"""
    remove_ipam_pools: NotRequired[
        "capo_elastic_load_balancing_v2.types.remove_ipam_pools.RemoveIpamPools"
    ]
    """<p>Remove the IP pools in use by the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyIpPoolsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "load_balancer_arn" in value:
        pairs.append((f"{key_prefix}LoadBalancerArn", str(value["load_balancer_arn"])))
    if "ipam_pools" in value:
        import capo_elastic_load_balancing_v2.types.ipam_pools

        capo_elastic_load_balancing_v2.types.ipam_pools.serialize_query(
            value["ipam_pools"], pairs, f"{key_prefix}IpamPools"
        )
    if "remove_ipam_pools" in value:
        import capo_elastic_load_balancing_v2.types.remove_ipam_pools

        capo_elastic_load_balancing_v2.types.remove_ipam_pools.serialize_query(
            value["remove_ipam_pools"], pairs, f"{key_prefix}RemoveIpamPools"
        )


def deserialize_query(el: Element) -> ModifyIpPoolsInput:
    out: ModifyIpPoolsInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_ipam_pools = el.find("IpamPools")
    if child_ipam_pools is not None:
        import capo_elastic_load_balancing_v2.types.ipam_pools

        out["ipam_pools"] = (
            capo_elastic_load_balancing_v2.types.ipam_pools.deserialize_query(
                child_ipam_pools
            )
        )
    child_remove_ipam_pools = el.find("RemoveIpamPools")
    if child_remove_ipam_pools is not None:
        import capo_elastic_load_balancing_v2.types.remove_ipam_pools

        out["remove_ipam_pools"] = (
            capo_elastic_load_balancing_v2.types.remove_ipam_pools.deserialize_query(
                child_remove_ipam_pools
            )
        )
    return out
