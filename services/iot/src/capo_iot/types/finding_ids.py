"""Generated from Smithy shape ``com.amazonaws.iot#FindingIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.finding_id

FindingIds: TypeAlias = list["capo_iot.types.finding_id.FindingId"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingIds) -> list:
    return list(value)


def deserialize_json(data: list) -> FindingIds:
    return list(data)
