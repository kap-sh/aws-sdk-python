"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.policy_attribute

PolicyAttributes: TypeAlias = list[
    "capo_elastic_load_balancing.types.policy_attribute.PolicyAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.policy_attribute

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.policy_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PolicyAttributes:
    import capo_elastic_load_balancing.types.policy_attribute

    out: PolicyAttributes = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.policy_attribute.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: PolicyAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.policy_attribute

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.policy_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PolicyAttributes:
    import capo_elastic_load_balancing.types.policy_attribute

    out: PolicyAttributes = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.policy_attribute.deserialize_query(child)
        )
    return out
