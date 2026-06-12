"""Generated from Smithy shape ``com.amazonaws.fis#ActionsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fis.errors import DeserializationError

ActionsMode: TypeAlias = Literal[
    "skip-all",
    "run-all",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "skip-all",
        "run-all",
    )
)


def serialize_json(value: ActionsMode) -> str:
    return value


def deserialize_json(data: str) -> ActionsMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionsMode value: {data!r}")
    return cast(ActionsMode, data)
