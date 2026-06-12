"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

ServiceEnvironmentState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: ServiceEnvironmentState) -> str:
    return value


def deserialize_json(data: str) -> ServiceEnvironmentState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceEnvironmentState value: {data!r}")
    return cast(ServiceEnvironmentState, data)
