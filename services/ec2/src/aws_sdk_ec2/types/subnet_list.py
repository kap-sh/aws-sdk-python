"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet

SubnetList: TypeAlias = list["aws_sdk_ec2.types.subnet.Subnet"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.subnet

        aws_sdk_ec2.types.subnet.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> SubnetList:
    import aws_sdk_ec2.types.subnet

    out: SubnetList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.subnet.deserialize_ec2_query(child))
    return out
