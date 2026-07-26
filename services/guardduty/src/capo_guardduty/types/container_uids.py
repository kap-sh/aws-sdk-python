"""Generated from Smithy shape ``com.amazonaws.guardduty#ContainerUids``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.container_uid

ContainerUids: TypeAlias = list["capo_guardduty.types.container_uid.ContainerUid"]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerUids) -> list:
    return list(value)


def deserialize_json(data: list) -> ContainerUids:
    return list(data)
