"""Generated from Smithy shape ``com.amazonaws.guardduty#SourceIps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

SourceIps: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: SourceIps) -> list:
    return list(value)


def deserialize_json(data: list) -> SourceIps:
    return list(data)
