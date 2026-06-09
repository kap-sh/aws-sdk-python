"""Generated from Smithy shape ``com.amazonaws.ec2#CidrBlockSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cidr_block

CidrBlockSet: TypeAlias = list["aws_sdk_ec2.types.cidr_block.CidrBlock"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CidrBlockSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.cidr_block

        aws_sdk_ec2.types.cidr_block.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> CidrBlockSet:
    import aws_sdk_ec2.types.cidr_block

    out: CidrBlockSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.cidr_block.deserialize_ec2_query(child))
    return out
