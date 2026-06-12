"""Generated from Smithy shape ``com.amazonaws.emrcontainers#FailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr_containers.errors import DeserializationError

FailureReason: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "USER_ERROR",
    "VALIDATION_ERROR",
    "CLUSTER_UNAVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_ERROR",
        "USER_ERROR",
        "VALIDATION_ERROR",
        "CLUSTER_UNAVAILABLE",
    )
)


def serialize_json(value: FailureReason) -> str:
    return value


def deserialize_json(data: str) -> FailureReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailureReason value: {data!r}")
    return cast(FailureReason, data)
