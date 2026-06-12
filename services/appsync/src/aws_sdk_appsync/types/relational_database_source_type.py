"""Generated from Smithy shape ``com.amazonaws.appsync#RelationalDatabaseSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

RelationalDatabaseSourceType: TypeAlias = Literal["RDS_HTTP_ENDPOINT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RDS_HTTP_ENDPOINT",))


def serialize_json(value: RelationalDatabaseSourceType) -> str:
    return value


def deserialize_json(data: str) -> RelationalDatabaseSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RelationalDatabaseSourceType value: {data!r}"
        )
    return cast(RelationalDatabaseSourceType, data)
