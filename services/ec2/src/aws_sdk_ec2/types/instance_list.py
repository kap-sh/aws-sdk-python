"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance

InstanceList: TypeAlias = list["aws_sdk_ec2.types.instance.Instance"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance

        aws_sdk_ec2.types.instance.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceList:
    import aws_sdk_ec2.types.instance

    out: InstanceList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.instance.deserialize_ec2_query(child))
    return out
