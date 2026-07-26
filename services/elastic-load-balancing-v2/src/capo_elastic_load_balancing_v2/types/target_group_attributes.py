"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetGroupAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.target_group_attribute

TargetGroupAttributes: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.target_group_attribute.TargetGroupAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetGroupAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.target_group_attribute

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.target_group_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TargetGroupAttributes:
    import capo_elastic_load_balancing_v2.types.target_group_attribute

    out: TargetGroupAttributes = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.target_group_attribute.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TargetGroupAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.target_group_attribute

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.target_group_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TargetGroupAttributes:
    import capo_elastic_load_balancing_v2.types.target_group_attribute

    out: TargetGroupAttributes = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.target_group_attribute.deserialize_query(
                child
            )
        )
    return out
