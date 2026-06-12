"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#RunType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mwaa_serverless.errors import DeserializationError

RunType: TypeAlias = Literal[
    "ON_DEMAND",
    "SCHEDULED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "SCHEDULED",
    )
)


def serialize_aws_json_1_0(value: RunType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RunType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RunType value: {data!r}")
    return cast(RunType, data)
