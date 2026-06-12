"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#FailureHandlingPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_edge.errors import DeserializationError

FailureHandlingPolicy: TypeAlias = Literal[
    "ROLLBACK_ON_FAILURE",
    "DO_NOTHING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROLLBACK_ON_FAILURE",
        "DO_NOTHING",
    )
)


def serialize_json(value: FailureHandlingPolicy) -> str:
    return value


def deserialize_json(data: str) -> FailureHandlingPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailureHandlingPolicy value: {data!r}")
    return cast(FailureHandlingPolicy, data)
