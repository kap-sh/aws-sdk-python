"""Generated from Smithy shape ``com.amazonaws.ec2#ArchitectureTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.architecture_type

ArchitectureTypeSet: TypeAlias = list[
    "aws_sdk_ec2.types.architecture_type.ArchitectureType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ArchitectureTypeSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.architecture_type

        aws_sdk_ec2.types.architecture_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ArchitectureTypeSet:
    import aws_sdk_ec2.types.architecture_type

    out: ArchitectureTypeSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.architecture_type.deserialize_ec2_query(child))
    return out
