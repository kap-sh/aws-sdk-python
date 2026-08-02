"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVolumeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.volume_modification


class ModifyVolumeResult(TypedDict, closed=True):
    volume_modification: NotRequired[
        "capo_ec2.types.volume_modification.VolumeModification"
    ]
    """<p>Information about the volume modification.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVolumeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "volume_modification" in value:
        import capo_ec2.types.volume_modification

        capo_ec2.types.volume_modification.serialize_ec2_query(
            value["volume_modification"], pairs, f"{key_prefix}VolumeModification"
        )


def deserialize_ec2_query(el: Element) -> ModifyVolumeResult:
    out: ModifyVolumeResult = {}  # type: ignore[typeddict-item]
    child_volume_modification = el.find("VolumeModification")
    if child_volume_modification is not None:
        import capo_ec2.types.volume_modification

        out["volume_modification"] = (
            capo_ec2.types.volume_modification.deserialize_ec2_query(
                child_volume_modification
            )
        )
    return out
