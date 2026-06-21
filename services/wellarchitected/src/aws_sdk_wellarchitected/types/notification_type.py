"""Generated from Smithy shape ``com.amazonaws.wellarchitected#NotificationType``."""

from typing import Literal, TypeAlias, cast

NotificationType: TypeAlias = Literal[
    "LENS_VERSION_UPGRADED",
    "LENS_VERSION_DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationType) -> str:
    return value


def deserialize_json(data: str) -> NotificationType:
    return cast(NotificationType, data)
