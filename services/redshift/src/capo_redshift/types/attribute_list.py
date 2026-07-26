"""Generated from Smithy shape ``com.amazonaws.redshift#AttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.account_attribute

AttributeList: TypeAlias = list[
    "capo_redshift.types.account_attribute.AccountAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.account_attribute

    for n, item in enumerate(value, 1):
        capo_redshift.types.account_attribute.serialize_query(
            item, pairs, f"{prefix}.AccountAttribute.{n}"
        )


def deserialize_query(el: Element) -> AttributeList:
    import capo_redshift.types.account_attribute

    out: AttributeList = []
    for child in el.findall("AccountAttribute"):
        out.append(capo_redshift.types.account_attribute.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.account_attribute

    for n, item in enumerate(value, 1):
        capo_redshift.types.account_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AttributeList:
    import capo_redshift.types.account_attribute

    out: AttributeList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.account_attribute.deserialize_query(child))
    return out
