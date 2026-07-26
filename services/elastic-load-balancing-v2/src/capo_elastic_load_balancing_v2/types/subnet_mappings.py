"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SubnetMappings``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.subnet_mapping

SubnetMappings: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.subnet_mapping.SubnetMapping"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SubnetMappings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.subnet_mapping

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.subnet_mapping.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SubnetMappings:
    import capo_elastic_load_balancing_v2.types.subnet_mapping

    out: SubnetMappings = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.subnet_mapping.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: SubnetMappings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.subnet_mapping

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.subnet_mapping.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SubnetMappings:
    import capo_elastic_load_balancing_v2.types.subnet_mapping

    out: SubnetMappings = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.subnet_mapping.deserialize_query(child)
        )
    return out
