"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ForwardingConfigState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ForwardingConfigState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: ForwardingConfigState) -> str:
    return value


def deserialize_json(data: str) -> ForwardingConfigState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ForwardingConfigState value: {data!r}")
    return cast(ForwardingConfigState, data)
