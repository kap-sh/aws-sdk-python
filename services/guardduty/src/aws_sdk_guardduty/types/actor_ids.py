"""Generated from Smithy shape ``com.amazonaws.guardduty#ActorIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string

ActorIds: TypeAlias = list["aws_sdk_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ActorIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ActorIds:
    return list(data)
