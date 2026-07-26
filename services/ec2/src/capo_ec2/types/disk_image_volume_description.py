"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImageVolumeDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.long
    import capo_ec2.types.string


class DiskImageVolumeDescription(TypedDict, closed=True):
    id: NotRequired["capo_ec2.types.string.String"]
    """<p>The volume identifier.</p>"""
    size: NotRequired["capo_ec2.types.long.Long"]
    """<p>The size of the volume, in GiB.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DiskImageVolumeDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))
    if "size" in value:
        pairs.append((f"{prefix}.Size", str(value["size"])))


def deserialize_ec2_query(el: Element) -> DiskImageVolumeDescription:
    out: DiskImageVolumeDescription = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    return out
