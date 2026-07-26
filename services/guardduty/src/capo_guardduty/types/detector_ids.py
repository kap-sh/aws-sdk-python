"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id

DetectorIds: TypeAlias = list["capo_guardduty.types.detector_id.DetectorId"]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorIds) -> list:
    return list(value)


def deserialize_json(data: list) -> DetectorIds:
    return list(data)
