"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingRecoveryPointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

RestoreTestingRecoveryPointType: TypeAlias = Literal[
    "CONTINUOUS",
    "SNAPSHOT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUOUS",
        "SNAPSHOT",
    )
)


def serialize_json(value: RestoreTestingRecoveryPointType) -> str:
    return value


def deserialize_json(data: str) -> RestoreTestingRecoveryPointType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RestoreTestingRecoveryPointType value: {data!r}"
        )
    return cast(RestoreTestingRecoveryPointType, data)
