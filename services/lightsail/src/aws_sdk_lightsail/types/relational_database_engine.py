"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseEngine``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

RelationalDatabaseEngine: TypeAlias = Literal["mysql",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("mysql",))


def serialize_aws_json_1_1(value: RelationalDatabaseEngine) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelationalDatabaseEngine:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelationalDatabaseEngine value: {data!r}")
    return cast(RelationalDatabaseEngine, data)
