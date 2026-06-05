"""Generated from Smithy shape ``com.amazonaws.ec2#ProtocolList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.protocol

ProtocolList: TypeAlias = list["aws_sdk_ec2.types.protocol.Protocol"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProtocolList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.protocol

        aws_sdk_ec2.types.protocol.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> ProtocolList:
    import aws_sdk_ec2.types.protocol

    out: ProtocolList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.protocol.deserialize_ec2_query(child))
    return out
