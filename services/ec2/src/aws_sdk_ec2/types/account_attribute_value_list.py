"""Generated from Smithy shape ``com.amazonaws.ec2#AccountAttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_value

AccountAttributeValueList: TypeAlias = list[
    "aws_sdk_ec2.types.account_attribute_value.AccountAttributeValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccountAttributeValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.account_attribute_value

        aws_sdk_ec2.types.account_attribute_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AccountAttributeValueList:
    import aws_sdk_ec2.types.account_attribute_value

    out: AccountAttributeValueList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.account_attribute_value.deserialize_ec2_query(child)
        )
    return out
