"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyAttributeDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.policy_attribute_description

PolicyAttributeDescriptions: TypeAlias = list[
    "capo_elastic_load_balancing.types.policy_attribute_description.PolicyAttributeDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyAttributeDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.policy_attribute_description

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.policy_attribute_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PolicyAttributeDescriptions:
    import capo_elastic_load_balancing.types.policy_attribute_description

    out: PolicyAttributeDescriptions = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.policy_attribute_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PolicyAttributeDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.policy_attribute_description

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.policy_attribute_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PolicyAttributeDescriptions:
    import capo_elastic_load_balancing.types.policy_attribute_description

    out: PolicyAttributeDescriptions = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.policy_attribute_description.deserialize_query(
                child
            )
        )
    return out
