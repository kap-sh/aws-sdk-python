"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronDeviceInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.neuron_device_core_info
    import capo_ec2.types.neuron_device_count
    import capo_ec2.types.neuron_device_memory_info
    import capo_ec2.types.neuron_device_name


class NeuronDeviceInfo(TypedDict, closed=True):
    count: NotRequired["capo_ec2.types.neuron_device_count.NeuronDeviceCount"]
    """<p>The number of neuron accelerators for the instance type.</p>"""
    name: NotRequired["capo_ec2.types.neuron_device_name.NeuronDeviceName"]
    """<p>The name of the neuron accelerator.</p>"""
    core_info: NotRequired[
        "capo_ec2.types.neuron_device_core_info.NeuronDeviceCoreInfo"
    ]
    """<p>Describes the cores available to each neuron accelerator.</p>"""
    memory_info: NotRequired[
        "capo_ec2.types.neuron_device_memory_info.NeuronDeviceMemoryInfo"
    ]
    """<p>Describes the memory available to each neuron accelerator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NeuronDeviceInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "count" in value:
        pairs.append((f"{prefix}.Count", str(value["count"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "core_info" in value:
        import capo_ec2.types.neuron_device_core_info

        capo_ec2.types.neuron_device_core_info.serialize_ec2_query(
            value["core_info"], pairs, f"{prefix}.CoreInfo"
        )
    if "memory_info" in value:
        import capo_ec2.types.neuron_device_memory_info

        capo_ec2.types.neuron_device_memory_info.serialize_ec2_query(
            value["memory_info"], pairs, f"{prefix}.MemoryInfo"
        )


def deserialize_ec2_query(el: Element) -> NeuronDeviceInfo:
    out: NeuronDeviceInfo = {}  # type: ignore[typeddict-item]
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_core_info = el.find("CoreInfo")
    if child_core_info is not None:
        import capo_ec2.types.neuron_device_core_info

        out["core_info"] = capo_ec2.types.neuron_device_core_info.deserialize_ec2_query(
            child_core_info
        )
    child_memory_info = el.find("MemoryInfo")
    if child_memory_info is not None:
        import capo_ec2.types.neuron_device_memory_info

        out["memory_info"] = (
            capo_ec2.types.neuron_device_memory_info.deserialize_ec2_query(
                child_memory_info
            )
        )
    return out
