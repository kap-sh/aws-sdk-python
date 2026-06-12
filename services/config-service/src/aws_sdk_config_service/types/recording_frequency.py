"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

RecordingFrequency: TypeAlias = Literal[
    "CONTINUOUS",
    "DAILY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUOUS",
        "DAILY",
    )
)


def serialize_aws_json_1_1(value: RecordingFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordingFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordingFrequency value: {data!r}")
    return cast(RecordingFrequency, data)
