"""Generated from Smithy shape ``com.amazonaws.ecs#StabilityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

StabilityStatus: TypeAlias = Literal[
    "STEADY_STATE",
    "STABILIZING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STEADY_STATE",
        "STABILIZING",
    )
)


def serialize_aws_json_1_1(value: StabilityStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StabilityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StabilityStatus value: {data!r}")
    return cast(StabilityStatus, data)
