"""Generated from Smithy shape ``com.amazonaws.mediatailor#FillPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

FillPolicy: TypeAlias = Literal[
    "FULL_AVAIL_ONLY",
    "PARTIAL_AVAIL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL_AVAIL_ONLY",
        "PARTIAL_AVAIL",
    )
)


def serialize_json(value: FillPolicy) -> str:
    return value


def deserialize_json(data: str) -> FillPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FillPolicy value: {data!r}")
    return cast(FillPolicy, data)
