"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVolumeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_modification


class ModifyVolumeResult(TypedDict):
    volume_modification: NotRequired[
        "aws_sdk_ec2.types.volume_modification.VolumeModification"
    ]
    """<p>Information about the volume modification.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVolumeResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "volume_modification" in value:
        import aws_sdk_ec2.types.volume_modification

        aws_sdk_ec2.types.volume_modification.serialize_ec2_query(
            value["volume_modification"], pairs, f"{prefix}.VolumeModification"
        )


def deserialize_ec2_query(el: Element) -> ModifyVolumeResult:
    out: ModifyVolumeResult = {}  # type: ignore[typeddict-item]
    child_volume_modification = el.find("VolumeModification")
    if child_volume_modification is not None:
        import aws_sdk_ec2.types.volume_modification

        out["volume_modification"] = (
            aws_sdk_ec2.types.volume_modification.deserialize_ec2_query(
                child_volume_modification
            )
        )
    return out
