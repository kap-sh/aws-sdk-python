"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RewriteConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.rewrite_config

RewriteConfigList: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.rewrite_config.RewriteConfig"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RewriteConfigList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.rewrite_config

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.rewrite_config.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RewriteConfigList:
    import capo_elastic_load_balancing_v2.types.rewrite_config

    out: RewriteConfigList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.rewrite_config.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: RewriteConfigList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.rewrite_config

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.rewrite_config.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RewriteConfigList:
    import capo_elastic_load_balancing_v2.types.rewrite_config

    out: RewriteConfigList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.rewrite_config.deserialize_query(child)
        )
    return out
