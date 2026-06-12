"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntitiesDetectionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

PiiEntitiesDetectionMode: TypeAlias = Literal[
    "ONLY_REDACTION",
    "ONLY_OFFSETS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONLY_REDACTION",
        "ONLY_OFFSETS",
    )
)


def serialize_aws_json_1_1(value: PiiEntitiesDetectionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PiiEntitiesDetectionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PiiEntitiesDetectionMode value: {data!r}")
    return cast(PiiEntitiesDetectionMode, data)
