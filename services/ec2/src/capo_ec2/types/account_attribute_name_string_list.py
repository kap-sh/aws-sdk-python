"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeNameStringList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_attribute_name

AccountAttributeNameStringList: TypeAlias = list[
    "capo_ec2.types.account_attribute_name.AccountAttributeName"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountAttributeNameStringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.account_attribute_name

        capo_ec2.types.account_attribute_name.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AccountAttributeNameStringList:
    import capo_ec2.types.account_attribute_name

    out: AccountAttributeNameStringList = []
    for child in el.findall("attributeName"):
        out.append(capo_ec2.types.account_attribute_name.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> AccountAttributeNameStringList:
    import capo_ec2.types.account_attribute_name

    out: AccountAttributeNameStringList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.account_attribute_name.deserialize_ec2_query(child))
    return out
