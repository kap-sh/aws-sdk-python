"""Generated from Smithy shape ``com.amazonaws.securitylake#AccessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securitylake.errors import DeserializationError

AccessType: TypeAlias = Literal[
    "LAKEFORMATION",
    "S3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LAKEFORMATION",
        "S3",
    )
)


def serialize_json(value: AccessType) -> str:
    return value


def deserialize_json(data: str) -> AccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessType value: {data!r}")
    return cast(AccessType, data)
