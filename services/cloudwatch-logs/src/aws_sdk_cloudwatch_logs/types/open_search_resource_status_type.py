"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OpenSearchResourceStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

OpenSearchResourceStatusType: TypeAlias = Literal[
    "ACTIVE",
    "NOT_FOUND",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "NOT_FOUND",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: OpenSearchResourceStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenSearchResourceStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OpenSearchResourceStatusType value: {data!r}"
        )
    return cast(OpenSearchResourceStatusType, data)
