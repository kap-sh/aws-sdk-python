"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Actions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.action

Actions: TypeAlias = list["capo_elastic_load_balancing_v2.types.action.Action"]


# --- awsQuery ser/de ---
def serialize_query(value: Actions, pairs: list[tuple[str, str]], prefix: str) -> None:
    import capo_elastic_load_balancing_v2.types.action

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.action.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Actions:
    import capo_elastic_load_balancing_v2.types.action

    out: Actions = []
    for child in el.findall("member"):
        out.append(capo_elastic_load_balancing_v2.types.action.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Actions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing_v2.types.action

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.action.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Actions:
    import capo_elastic_load_balancing_v2.types.action

    out: Actions = []
    for child in parent.findall(tag):
        out.append(capo_elastic_load_balancing_v2.types.action.deserialize_query(child))
    return out
