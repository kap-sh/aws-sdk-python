"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_attribute_value

AccountAttributeValueList: TypeAlias = list[
    "capo_ec2.types.account_attribute_value.AccountAttributeValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountAttributeValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.account_attribute_value

        capo_ec2.types.account_attribute_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AccountAttributeValueList:
    import capo_ec2.types.account_attribute_value

    out: AccountAttributeValueList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.account_attribute_value.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AccountAttributeValueList:
    import capo_ec2.types.account_attribute_value

    out: AccountAttributeValueList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.account_attribute_value.deserialize_ec2_query(child))
    return out
