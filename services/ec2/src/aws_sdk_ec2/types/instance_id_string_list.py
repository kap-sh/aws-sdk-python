"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_id

InstanceIdStringList: TypeAlias = list["aws_sdk_ec2.types.instance_id.InstanceId"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIdStringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceIdStringList:
    out: InstanceIdStringList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
