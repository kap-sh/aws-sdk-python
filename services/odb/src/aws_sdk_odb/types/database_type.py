"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DatabaseType: TypeAlias = Literal[
    "REGULAR",
    "CLONE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGULAR",
        "CLONE",
    )
)


def serialize_aws_json_1_0(value: DatabaseType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatabaseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseType value: {data!r}")
    return cast(DatabaseType, data)
