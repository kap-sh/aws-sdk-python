"""Generated from Smithy shape ``com.amazonaws.rds#ContextAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.context_attribute

ContextAttributeList: TypeAlias = list[
    "capo_rds.types.context_attribute.ContextAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ContextAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.context_attribute

    for n, item in enumerate(value, 1):
        capo_rds.types.context_attribute.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ContextAttributeList:
    import capo_rds.types.context_attribute

    out: ContextAttributeList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.context_attribute.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ContextAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.context_attribute

    for n, item in enumerate(value, 1):
        capo_rds.types.context_attribute.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ContextAttributeList:
    import capo_rds.types.context_attribute

    out: ContextAttributeList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.context_attribute.deserialize_query(child))
    return out
