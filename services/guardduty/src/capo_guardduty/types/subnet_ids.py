"""Generated from Smithy shape ``com.amazonaws.guardduty#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

SubnetIds: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIds:
    return list(data)
