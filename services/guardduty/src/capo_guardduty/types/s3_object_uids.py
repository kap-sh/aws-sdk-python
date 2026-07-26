"""Generated from Smithy shape ``com.amazonaws.guardduty#S3ObjectUids``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

S3ObjectUids: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: S3ObjectUids) -> list:
    return list(value)


def deserialize_json(data: list) -> S3ObjectUids:
    return list(data)
