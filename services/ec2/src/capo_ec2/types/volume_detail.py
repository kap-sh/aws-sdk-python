"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.long


class VolumeDetail(TypedDict, closed=True):
    size: NotRequired["capo_ec2.types.long.Long"]
    """<p>The size of the volume, in GiB.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "size" in value:
        pairs.append((f"{key_prefix}Size", str(value["size"])))


def deserialize_ec2_query(el: Element) -> VolumeDetail:
    out: VolumeDetail = {}  # type: ignore[typeddict-item]
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    return out
