"""Generated from Smithy shape ``com.amazonaws.wellarchitected#NotificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

NotificationType: TypeAlias = Literal[
    "LENS_VERSION_UPGRADED",
    "LENS_VERSION_DEPRECATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LENS_VERSION_UPGRADED",
        "LENS_VERSION_DEPRECATED",
    )
)


def serialize_json(value: NotificationType) -> str:
    return value


def deserialize_json(data: str) -> NotificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationType value: {data!r}")
    return cast(NotificationType, data)
