"""Generated from Smithy shape ``com.amazonaws.gamelift#LogDestination``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

LogDestination: TypeAlias = Literal[
    "NONE",
    "CLOUDWATCH",
    "S3",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "CLOUDWATCH",
        "S3",
    )
)


def serialize_aws_json_1_1(value: LogDestination) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogDestination:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogDestination value: {data!r}")
    return cast(LogDestination, data)
