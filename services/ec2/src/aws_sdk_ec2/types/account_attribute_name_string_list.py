"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeNameStringList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_name

AccountAttributeNameStringList: TypeAlias = list[
    "aws_sdk_ec2.types.account_attribute_name.AccountAttributeName"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountAttributeNameStringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.account_attribute_name

        aws_sdk_ec2.types.account_attribute_name.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AccountAttributeNameStringList:
    import aws_sdk_ec2.types.account_attribute_name

    out: AccountAttributeNameStringList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.account_attribute_name.deserialize_ec2_query(child)
        )
    return out
