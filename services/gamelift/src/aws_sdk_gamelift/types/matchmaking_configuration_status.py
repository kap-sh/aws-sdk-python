"""Generated from Smithy shape ``com.amazonaws.gamelift#MatchmakingConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

MatchmakingConfigurationStatus: TypeAlias = Literal[
    "CANCELLED",
    "COMPLETED",
    "FAILED",
    "PLACING",
    "QUEUED",
    "REQUIRES_ACCEPTANCE",
    "SEARCHING",
    "TIMED_OUT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CANCELLED",
        "COMPLETED",
        "FAILED",
        "PLACING",
        "QUEUED",
        "REQUIRES_ACCEPTANCE",
        "SEARCHING",
        "TIMED_OUT",
    )
)


def serialize_aws_json_1_1(value: MatchmakingConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MatchmakingConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MatchmakingConfigurationStatus value: {data!r}"
        )
    return cast(MatchmakingConfigurationStatus, data)
