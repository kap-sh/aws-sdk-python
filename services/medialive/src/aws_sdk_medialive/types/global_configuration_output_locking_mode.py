"""Generated from Smithy shape ``com.amazonaws.medialive#GlobalConfigurationOutputLockingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Global Configuration Output Locking Mode"""
GlobalConfigurationOutputLockingMode: TypeAlias = Literal[
    "EPOCH_LOCKING",
    "PIPELINE_LOCKING",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EPOCH_LOCKING",
        "PIPELINE_LOCKING",
        "DISABLED",
    )
)


def serialize_json(value: GlobalConfigurationOutputLockingMode) -> str:
    return value


def deserialize_json(data: str) -> GlobalConfigurationOutputLockingMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GlobalConfigurationOutputLockingMode value: {data!r}"
        )
    return cast(GlobalConfigurationOutputLockingMode, data)
