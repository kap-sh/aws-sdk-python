"""Generated from Smithy shape ``com.amazonaws.iot#VerificationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

VerificationState: TypeAlias = Literal[
    "FALSE_POSITIVE",
    "BENIGN_POSITIVE",
    "TRUE_POSITIVE",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FALSE_POSITIVE",
        "BENIGN_POSITIVE",
        "TRUE_POSITIVE",
        "UNKNOWN",
    )
)


def serialize_json(value: VerificationState) -> str:
    return value


def deserialize_json(data: str) -> VerificationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VerificationState value: {data!r}")
    return cast(VerificationState, data)
