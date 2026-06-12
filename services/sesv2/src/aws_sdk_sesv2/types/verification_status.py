"""Generated from Smithy shape ``com.amazonaws.sesv2#VerificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

VerificationStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILED",
    "TEMPORARY_FAILURE",
    "NOT_STARTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCESS",
        "FAILED",
        "TEMPORARY_FAILURE",
        "NOT_STARTED",
    )
)


def serialize_json(value: VerificationStatus) -> str:
    return value


def deserialize_json(data: str) -> VerificationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VerificationStatus value: {data!r}")
    return cast(VerificationStatus, data)
