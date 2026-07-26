"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.neuron_device_info_list
    import capo_ec2.types.total_neuron_memory


class NeuronInfo(TypedDict, closed=True):
    neuron_devices: NotRequired[
        "capo_ec2.types.neuron_device_info_list.NeuronDeviceInfoList"
    ]
    """<p>Describes the neuron accelerators for the instance type.</p>"""
    total_neuron_device_memory_in_mi_b: NotRequired[
        "capo_ec2.types.total_neuron_memory.TotalNeuronMemory"
    ]
    """<p>The total size of the memory for the neuron accelerators for the instance type, in MiB.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NeuronInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "neuron_devices" in value:
        import capo_ec2.types.neuron_device_info_list

        capo_ec2.types.neuron_device_info_list.serialize_ec2_query(
            value["neuron_devices"], pairs, f"{prefix}.NeuronDevices"
        )
    if "total_neuron_device_memory_in_mi_b" in value:
        pairs.append(
            (
                f"{prefix}.TotalNeuronDeviceMemoryInMiB",
                str(value["total_neuron_device_memory_in_mi_b"]),
            )
        )


def deserialize_ec2_query(el: Element) -> NeuronInfo:
    out: NeuronInfo = {}  # type: ignore[typeddict-item]
    if el.find("NeuronDevices") is not None:
        import capo_ec2.types.neuron_device_info_list

        out["neuron_devices"] = (
            capo_ec2.types.neuron_device_info_list.deserialize_ec2_query(
                el, "NeuronDevices"
            )
        )
    child_total_neuron_device_memory_in_mi_b = el.find("TotalNeuronDeviceMemoryInMiB")
    if child_total_neuron_device_memory_in_mi_b is not None:
        out["total_neuron_device_memory_in_mi_b"] = int(
            child_total_neuron_device_memory_in_mi_b.text or ""
        )
    return out
