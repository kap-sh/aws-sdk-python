"""Generated from Smithy shape ``com.amazonaws.qbusiness#QAppsControlMode``."""

from typing import Literal, TypeAlias, cast

QAppsControlMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QAppsControlMode) -> str:
    return value


def deserialize_json(data: str) -> QAppsControlMode:
    return cast(QAppsControlMode, data)
