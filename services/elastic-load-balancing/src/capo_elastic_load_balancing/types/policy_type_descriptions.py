"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyTypeDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.policy_type_description

PolicyTypeDescriptions: TypeAlias = list[
    "capo_elastic_load_balancing.types.policy_type_description.PolicyTypeDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyTypeDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.policy_type_description

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.policy_type_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PolicyTypeDescriptions:
    import capo_elastic_load_balancing.types.policy_type_description

    out: PolicyTypeDescriptions = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.policy_type_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PolicyTypeDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.policy_type_description

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.policy_type_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PolicyTypeDescriptions:
    import capo_elastic_load_balancing.types.policy_type_description

    out: PolicyTypeDescriptions = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.policy_type_description.deserialize_query(
                child
            )
        )
    return out
