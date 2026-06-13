"""Generated from Smithy shape ``com.amazonaws.emr#PersistentAppUIType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

PersistentAppUIType: TypeAlias = Literal[
    "SHS",
    "TEZ",
    "YTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHS",
        "TEZ",
        "YTS",
    )
)


def serialize_aws_json_1_1(value: PersistentAppUIType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PersistentAppUIType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PersistentAppUIType value: {data!r}")
    return cast(PersistentAppUIType, data)
