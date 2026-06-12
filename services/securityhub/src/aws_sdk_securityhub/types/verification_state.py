"""Generated from Smithy shape ``com.amazonaws.securityhub#VerificationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

VerificationState: TypeAlias = Literal[
    "UNKNOWN",
    "TRUE_POSITIVE",
    "FALSE_POSITIVE",
    "BENIGN_POSITIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN",
        "TRUE_POSITIVE",
        "FALSE_POSITIVE",
        "BENIGN_POSITIVE",
    )
)


def serialize_json(value: VerificationState) -> str:
    return value


def deserialize_json(data: str) -> VerificationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VerificationState value: {data!r}")
    return cast(VerificationState, data)
