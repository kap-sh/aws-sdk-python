"""Generated from Smithy shape ``com.amazonaws.ec2#ExcludedInstanceTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.excluded_instance_type

ExcludedInstanceTypeSet: TypeAlias = list[
    "aws_sdk_ec2.types.excluded_instance_type.ExcludedInstanceType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExcludedInstanceTypeSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(parent: Element, tag: str) -> ExcludedInstanceTypeSet:
    out: ExcludedInstanceTypeSet = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
