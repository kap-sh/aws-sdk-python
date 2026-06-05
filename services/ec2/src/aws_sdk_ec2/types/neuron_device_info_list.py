"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.neuron_device_info

NeuronDeviceInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.neuron_device_info.NeuronDeviceInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NeuronDeviceInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.neuron_device_info

        aws_sdk_ec2.types.neuron_device_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> NeuronDeviceInfoList:
    import aws_sdk_ec2.types.neuron_device_info

    out: NeuronDeviceInfoList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.neuron_device_info.deserialize_ec2_query(child))
    return out
