"""Generated from Smithy shape ``com.amazonaws.ec2#AcceleratorNameSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.accelerator_name

AcceleratorNameSet: TypeAlias = list[
    "aws_sdk_ec2.types.accelerator_name.AcceleratorName"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceleratorNameSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.accelerator_name

        aws_sdk_ec2.types.accelerator_name.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AcceleratorNameSet:
    import aws_sdk_ec2.types.accelerator_name

    out: AcceleratorNameSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.accelerator_name.deserialize_ec2_query(child))
    return out
