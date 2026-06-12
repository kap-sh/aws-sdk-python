"""Generated from Smithy shape ``com.amazonaws.batch#FirelensConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

FirelensConfigurationType: TypeAlias = Literal[
    "fluentd",
    "fluentbit",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "fluentd",
        "fluentbit",
    )
)


def serialize_json(value: FirelensConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> FirelensConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirelensConfigurationType value: {data!r}")
    return cast(FirelensConfigurationType, data)
