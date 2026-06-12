"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateDataRetentionOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

UpdateDataRetentionOperation: TypeAlias = Literal[
    "INCREASE_DATA_RETENTION",
    "DECREASE_DATA_RETENTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCREASE_DATA_RETENTION",
        "DECREASE_DATA_RETENTION",
    )
)


def serialize_json(value: UpdateDataRetentionOperation) -> str:
    return value


def deserialize_json(data: str) -> UpdateDataRetentionOperation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UpdateDataRetentionOperation value: {data!r}"
        )
    return cast(UpdateDataRetentionOperation, data)
