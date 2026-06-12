"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ConformancePackState: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_FAILED",
    )
)


def serialize_aws_json_1_1(value: ConformancePackState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConformancePackState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConformancePackState value: {data!r}")
    return cast(ConformancePackState, data)
