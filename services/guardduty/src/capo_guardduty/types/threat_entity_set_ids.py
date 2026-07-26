"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatEntitySetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

ThreatEntitySetIds: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatEntitySetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ThreatEntitySetIds:
    return list(data)
