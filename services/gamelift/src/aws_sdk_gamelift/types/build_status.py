"""Generated from Smithy shape ``com.amazonaws.gamelift#BuildStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

BuildStatus: TypeAlias = Literal[
    "INITIALIZED",
    "READY",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZED",
        "READY",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: BuildStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BuildStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BuildStatus value: {data!r}")
    return cast(BuildStatus, data)
