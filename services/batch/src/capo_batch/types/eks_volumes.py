"""Generated from Smithy shape ``com.amazonaws.batch#EksVolumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.eks_volume

EksVolumes: TypeAlias = list["capo_batch.types.eks_volume.EksVolume"]


# --- restJson1 ser/de ---
def serialize_json(value: EksVolumes) -> list:
    import capo_batch.types.eks_volume

    out: list = []
    for item in value:
        out.append(capo_batch.types.eks_volume.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksVolumes:
    import capo_batch.types.eks_volume

    out: EksVolumes = []
    for item in data:
        out.append(capo_batch.types.eks_volume.deserialize_json(item))
    return out
