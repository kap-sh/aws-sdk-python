"""Generated from Smithy shape ``com.amazonaws.kafka#ConfigurationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The state of a configuration.</p>"""
ConfigurationState: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
        "DELETE_FAILED",
    )
)


def serialize_json(value: ConfigurationState) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationState value: {data!r}")
    return cast(ConfigurationState, data)
