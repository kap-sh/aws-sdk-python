"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingRecoveryPointSelectionAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

RestoreTestingRecoveryPointSelectionAlgorithm: TypeAlias = Literal[
    "LATEST_WITHIN_WINDOW",
    "RANDOM_WITHIN_WINDOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LATEST_WITHIN_WINDOW",
        "RANDOM_WITHIN_WINDOW",
    )
)


def serialize_json(value: RestoreTestingRecoveryPointSelectionAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> RestoreTestingRecoveryPointSelectionAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RestoreTestingRecoveryPointSelectionAlgorithm value: {data!r}"
        )
    return cast(RestoreTestingRecoveryPointSelectionAlgorithm, data)
