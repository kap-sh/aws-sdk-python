"""Generated from Smithy shape ``com.amazonaws.ec2#CpuManufacturerSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cpu_manufacturer

CpuManufacturerSet: TypeAlias = list[
    "aws_sdk_ec2.types.cpu_manufacturer.CpuManufacturer"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CpuManufacturerSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.cpu_manufacturer

        aws_sdk_ec2.types.cpu_manufacturer.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CpuManufacturerSet:
    import aws_sdk_ec2.types.cpu_manufacturer

    out: CpuManufacturerSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.cpu_manufacturer.deserialize_ec2_query(child))
    return out
