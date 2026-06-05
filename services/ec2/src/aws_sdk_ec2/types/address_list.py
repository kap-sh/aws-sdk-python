"""Generated from Smithy shape ``com.amazonaws.ec2#AddressList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address

AddressList: TypeAlias = list["aws_sdk_ec2.types.address.Address"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddressList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.address

        aws_sdk_ec2.types.address.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> AddressList:
    import aws_sdk_ec2.types.address

    out: AddressList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.address.deserialize_ec2_query(child))
    return out
