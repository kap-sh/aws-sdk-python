"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#InstanceStates``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.instance_state

InstanceStates: TypeAlias = list[
    "capo_elastic_load_balancing.types.instance_state.InstanceState"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.instance_state

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.instance_state.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InstanceStates:
    import capo_elastic_load_balancing.types.instance_state

    out: InstanceStates = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.instance_state.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: InstanceStates, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.instance_state

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.instance_state.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InstanceStates:
    import capo_elastic_load_balancing.types.instance_state

    out: InstanceStates = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.instance_state.deserialize_query(child)
        )
    return out
