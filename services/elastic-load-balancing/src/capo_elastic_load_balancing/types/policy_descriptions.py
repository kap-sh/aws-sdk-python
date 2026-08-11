"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#PolicyDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.policy_description

PolicyDescriptions: TypeAlias = list[
    "capo_elastic_load_balancing.types.policy_description.PolicyDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.policy_description

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.policy_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PolicyDescriptions:
    import capo_elastic_load_balancing.types.policy_description

    out: PolicyDescriptions = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.policy_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PolicyDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.policy_description

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.policy_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PolicyDescriptions:
    import capo_elastic_load_balancing.types.policy_description

    out: PolicyDescriptions = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.policy_description.deserialize_query(
                child
            )
        )
    return out
