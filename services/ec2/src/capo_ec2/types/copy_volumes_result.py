"""Generated from Smithy shape ``com.amazonaws.ec2#CopyVolumesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.volume_list


class CopyVolumesResult(TypedDict, closed=True):
    volumes: NotRequired["capo_ec2.types.volume_list.VolumeList"]
    """<p>Information about the volume copy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CopyVolumesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "volumes" in value:
        import capo_ec2.types.volume_list

        capo_ec2.types.volume_list.serialize_ec2_query(
            value["volumes"], pairs, f"{prefix}.VolumeSet"
        )


def deserialize_ec2_query(el: Element) -> CopyVolumesResult:
    out: CopyVolumesResult = {}  # type: ignore[typeddict-item]
    if el.find("VolumeSet") is not None:
        import capo_ec2.types.volume_list

        out["volumes"] = capo_ec2.types.volume_list.deserialize_ec2_query(
            el, "VolumeSet"
        )
    return out
