"""Generated from Smithy shape ``com.amazonaws.transcribe#ModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

ModelStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_aws_json_1_1(value: ModelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelStatus value: {data!r}")
    return cast(ModelStatus, data)
