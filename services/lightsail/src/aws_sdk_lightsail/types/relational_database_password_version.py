"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabasePasswordVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

RelationalDatabasePasswordVersion: TypeAlias = Literal[
    "CURRENT",
    "PREVIOUS",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CURRENT",
        "PREVIOUS",
        "PENDING",
    )
)


def serialize_aws_json_1_1(value: RelationalDatabasePasswordVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationalDatabasePasswordVersion:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RelationalDatabasePasswordVersion value: {data!r}"
        )
    return cast(RelationalDatabasePasswordVersion, data)
