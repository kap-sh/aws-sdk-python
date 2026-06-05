"""Generated from Smithy shape ``com.amazonaws.ec2#RootDeviceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.root_device_type

RootDeviceTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.root_device_type.RootDeviceType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RootDeviceTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.root_device_type

        aws_sdk_ec2.types.root_device_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> RootDeviceTypeList:
    import aws_sdk_ec2.types.root_device_type

    out: RootDeviceTypeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.root_device_type.deserialize_ec2_query(child))
    return out
