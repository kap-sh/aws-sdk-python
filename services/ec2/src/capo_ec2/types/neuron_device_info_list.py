"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronDeviceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.neuron_device_info

NeuronDeviceInfoList: TypeAlias = list[
    "capo_ec2.types.neuron_device_info.NeuronDeviceInfo"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NeuronDeviceInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.neuron_device_info

        capo_ec2.types.neuron_device_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> NeuronDeviceInfoList:
    import capo_ec2.types.neuron_device_info

    out: NeuronDeviceInfoList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.neuron_device_info.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> NeuronDeviceInfoList:
    import capo_ec2.types.neuron_device_info

    out: NeuronDeviceInfoList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.neuron_device_info.deserialize_ec2_query(child))
    return out
