"""Generated from Smithy shape ``com.amazonaws.personalize#ImportMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_personalize.errors import DeserializationError

ImportMode: TypeAlias = Literal[
    "FULL",
    "INCREMENTAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "INCREMENTAL",
    )
)


def serialize_aws_json_1_1(value: ImportMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportMode value: {data!r}")
    return cast(ImportMode, data)
