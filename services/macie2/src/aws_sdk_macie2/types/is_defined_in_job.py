"""Generated from Smithy shape ``com.amazonaws.macie2#IsDefinedInJob``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

IsDefinedInJob: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
        "UNKNOWN",
    )
)


def serialize_json(value: IsDefinedInJob) -> str:
    return value


def deserialize_json(data: str) -> IsDefinedInJob:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsDefinedInJob value: {data!r}")
    return cast(IsDefinedInJob, data)
