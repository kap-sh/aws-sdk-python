"""Generated from Smithy shape ``com.amazonaws.ec2#ProtocolIntList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.protocol_int

ProtocolIntList: TypeAlias = list["aws_sdk_ec2.types.protocol_int.ProtocolInt"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ProtocolIntList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(parent: Element, tag: str) -> ProtocolIntList:
    out: ProtocolIntList = []
    for child in parent.findall(tag):
        out.append(int(child.text or ""))
    return out
