"""Generated from Smithy shape ``com.amazonaws.guardduty#VolumeDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.volume_detail

VolumeDetails: TypeAlias = list["capo_guardduty.types.volume_detail.VolumeDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: VolumeDetails) -> list:
    import capo_guardduty.types.volume_detail

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.volume_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> VolumeDetails:
    import capo_guardduty.types.volume_detail

    out: VolumeDetails = []
    for item in data:
        out.append(capo_guardduty.types.volume_detail.deserialize_json(item))
    return out
