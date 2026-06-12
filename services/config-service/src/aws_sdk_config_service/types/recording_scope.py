"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

RecordingScope: TypeAlias = Literal[
    "INTERNAL",
    "PAID",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL",
        "PAID",
    )
)


def serialize_aws_json_1_1(value: RecordingScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordingScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordingScope value: {data!r}")
    return cast(RecordingScope, data)
