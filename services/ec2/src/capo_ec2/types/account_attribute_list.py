"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_attribute

AccountAttributeList: TypeAlias = list[
    "capo_ec2.types.account_attribute.AccountAttribute"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.account_attribute

        capo_ec2.types.account_attribute.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AccountAttributeList:
    import capo_ec2.types.account_attribute

    out: AccountAttributeList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.account_attribute.deserialize_ec2_query(child))
    return out
