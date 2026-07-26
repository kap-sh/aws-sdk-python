"""Generated from Smithy shape ``com.amazonaws.redshift#AttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.attribute_value_target

AttributeValueList: TypeAlias = list[
    "capo_redshift.types.attribute_value_target.AttributeValueTarget"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AttributeValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.attribute_value_target

    for n, item in enumerate(value, 1):
        capo_redshift.types.attribute_value_target.serialize_query(
            item, pairs, f"{prefix}.AttributeValueTarget.{n}"
        )


def deserialize_query(el: Element) -> AttributeValueList:
    import capo_redshift.types.attribute_value_target

    out: AttributeValueList = []
    for child in el.findall("AttributeValueTarget"):
        out.append(capo_redshift.types.attribute_value_target.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AttributeValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.attribute_value_target

    for n, item in enumerate(value, 1):
        capo_redshift.types.attribute_value_target.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AttributeValueList:
    import capo_redshift.types.attribute_value_target

    out: AttributeValueList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.attribute_value_target.deserialize_query(child))
    return out
