"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RemoveIpamPools``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum

RemoveIpamPools: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum.RemoveIpamPoolEnum"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveIpamPools, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RemoveIpamPools:
    import capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum

    out: RemoveIpamPools = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: RemoveIpamPools, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RemoveIpamPools:
    import capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum

    out: RemoveIpamPools = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.remove_ipam_pool_enum.deserialize_query(
                child
            )
        )
    return out
