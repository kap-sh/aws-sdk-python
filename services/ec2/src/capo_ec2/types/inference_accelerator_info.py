"""Generated from Smithy shape ``com.amazonaws.ec2#InferenceAcceleratorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.inference_device_info_list
    import capo_ec2.types.total_inference_memory


class InferenceAcceleratorInfo(TypedDict, closed=True):
    accelerators: NotRequired[
        "capo_ec2.types.inference_device_info_list.InferenceDeviceInfoList"
    ]
    """<p>Describes the Inference accelerators for the instance type.</p>"""
    total_inference_memory_in_mi_b: NotRequired[
        "capo_ec2.types.total_inference_memory.totalInferenceMemory"
    ]
    """<p>The total size of the memory for the inference accelerators for the instance type, in MiB.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InferenceAcceleratorInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "accelerators" in value:
        import capo_ec2.types.inference_device_info_list

        capo_ec2.types.inference_device_info_list.serialize_ec2_query(
            value["accelerators"], pairs, f"{prefix}.Accelerators"
        )
    if "total_inference_memory_in_mi_b" in value:
        pairs.append(
            (
                f"{prefix}.TotalInferenceMemoryInMiB",
                str(value["total_inference_memory_in_mi_b"]),
            )
        )


def deserialize_ec2_query(el: Element) -> InferenceAcceleratorInfo:
    out: InferenceAcceleratorInfo = {}  # type: ignore[typeddict-item]
    if el.find("Accelerators") is not None:
        import capo_ec2.types.inference_device_info_list

        out["accelerators"] = (
            capo_ec2.types.inference_device_info_list.deserialize_ec2_query(
                el, "Accelerators"
            )
        )
    child_total_inference_memory_in_mi_b = el.find("TotalInferenceMemoryInMiB")
    if child_total_inference_memory_in_mi_b is not None:
        out["total_inference_memory_in_mi_b"] = int(
            child_total_inference_memory_in_mi_b.text or ""
        )
    return out
