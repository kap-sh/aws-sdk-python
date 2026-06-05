"""Generated from Smithy shape ``com.amazonaws.ec2#MemoryInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.memory_size


class MemoryInfo(TypedDict):
    size_in_mi_b: NotRequired["aws_sdk_ec2.types.memory_size.MemorySize"]
    """<p>The size of the memory, in MiB.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MemoryInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "size_in_mi_b" in value:
        pairs.append((f"{prefix}.SizeInMiB", str(value["size_in_mi_b"])))


def deserialize_ec2_query(el: Element) -> MemoryInfo:
    out: MemoryInfo = {}  # type: ignore[typeddict-item]
    child_size_in_mi_b = el.find("SizeInMiB")
    if child_size_in_mi_b is not None:
        out["size_in_mi_b"] = int(child_size_in_mi_b.text or "")
    return out
