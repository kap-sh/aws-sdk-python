"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileNotificationType``."""

from typing import Literal, TypeAlias, cast

ProfileNotificationType: TypeAlias = Literal[
    "PROFILE_ANSWERS_UPDATED",
    "PROFILE_DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileNotificationType) -> str:
    return value


def deserialize_json(data: str) -> ProfileNotificationType:
    return cast(ProfileNotificationType, data)
