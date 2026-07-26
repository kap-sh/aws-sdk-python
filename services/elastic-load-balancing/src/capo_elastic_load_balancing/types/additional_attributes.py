"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#AdditionalAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.additional_attribute

AdditionalAttributes: TypeAlias = list[
    "capo_elastic_load_balancing.types.additional_attribute.AdditionalAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AdditionalAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.additional_attribute

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.additional_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AdditionalAttributes:
    import capo_elastic_load_balancing.types.additional_attribute

    out: AdditionalAttributes = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing.types.additional_attribute.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: AdditionalAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_load_balancing.types.additional_attribute

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing.types.additional_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AdditionalAttributes:
    import capo_elastic_load_balancing.types.additional_attribute

    out: AdditionalAttributes = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing.types.additional_attribute.deserialize_query(
                child
            )
        )
    return out
