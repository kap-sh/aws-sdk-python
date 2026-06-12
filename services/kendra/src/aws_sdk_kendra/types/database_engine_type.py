"""Generated from Smithy shape ``com.amazonaws.kendra#DatabaseEngineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

DatabaseEngineType: TypeAlias = Literal[
    "RDS_AURORA_MYSQL",
    "RDS_AURORA_POSTGRESQL",
    "RDS_MYSQL",
    "RDS_POSTGRESQL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RDS_AURORA_MYSQL",
        "RDS_AURORA_POSTGRESQL",
        "RDS_MYSQL",
        "RDS_POSTGRESQL",
    )
)


def serialize_aws_json_1_1(value: DatabaseEngineType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseEngineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseEngineType value: {data!r}")
    return cast(DatabaseEngineType, data)
