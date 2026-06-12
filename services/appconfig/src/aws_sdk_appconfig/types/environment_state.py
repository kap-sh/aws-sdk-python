"""Generated from Smithy shape ``com.amazonaws.appconfig#EnvironmentState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

EnvironmentState: TypeAlias = Literal[
    "READY_FOR_DEPLOYMENT",
    "DEPLOYING",
    "ROLLING_BACK",
    "ROLLED_BACK",
    "REVERTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY_FOR_DEPLOYMENT",
        "DEPLOYING",
        "ROLLING_BACK",
        "ROLLED_BACK",
        "REVERTED",
    )
)


def serialize_json(value: EnvironmentState) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentState value: {data!r}")
    return cast(EnvironmentState, data)
