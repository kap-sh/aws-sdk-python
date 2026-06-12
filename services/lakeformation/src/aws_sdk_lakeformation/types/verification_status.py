"""Generated from Smithy shape ``com.amazonaws.lakeformation#VerificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

VerificationStatus: TypeAlias = Literal[
    "VERIFIED",
    "VERIFICATION_FAILED",
    "NOT_VERIFIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VERIFIED",
        "VERIFICATION_FAILED",
        "NOT_VERIFIED",
    )
)


def serialize_json(value: VerificationStatus) -> str:
    return value


def deserialize_json(data: str) -> VerificationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VerificationStatus value: {data!r}")
    return cast(VerificationStatus, data)
