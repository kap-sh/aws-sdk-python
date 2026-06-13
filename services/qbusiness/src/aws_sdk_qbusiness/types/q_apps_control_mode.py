"""Generated from Smithy shape ``com.amazonaws.qbusiness#QAppsControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

QAppsControlMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: QAppsControlMode) -> str:
    return value


def deserialize_json(data: str) -> QAppsControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QAppsControlMode value: {data!r}")
    return cast(QAppsControlMode, data)
