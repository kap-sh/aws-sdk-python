"""Generated from Smithy shape ``com.amazonaws.appflow#PrefixType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

PrefixType: TypeAlias = Literal[
    "FILENAME",
    "PATH",
    "PATH_AND_FILENAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILENAME",
        "PATH",
        "PATH_AND_FILENAME",
    )
)


def serialize_json(value: PrefixType) -> str:
    return value


def deserialize_json(data: str) -> PrefixType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrefixType value: {data!r}")
    return cast(PrefixType, data)
