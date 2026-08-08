"""Generated from Smithy shape ``com.amazonaws.ec2#InferenceDeviceMemoryInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.inference_device_memory_size


class InferenceDeviceMemoryInfo(TypedDict, closed=True):
    size_in_mi_b: NotRequired[
        "capo_ec2.types.inference_device_memory_size.InferenceDeviceMemorySize"
    ]
    """<p>The size of the memory available to the inference accelerator, in MiB.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InferenceDeviceMemoryInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "size_in_mi_b" in value:
        pairs.append((f"{key_prefix}SizeInMiB", str(value["size_in_mi_b"])))


def deserialize_ec2_query(el: Element) -> InferenceDeviceMemoryInfo:
    out: InferenceDeviceMemoryInfo = {}  # type: ignore[typeddict-item]
    child_size_in_mi_b = el.find("sizeInMiB")
    if child_size_in_mi_b is not None:
        out["size_in_mi_b"] = int(child_size_in_mi_b.text or "")
    return out
