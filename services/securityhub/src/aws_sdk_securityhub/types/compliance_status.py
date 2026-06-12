"""Generated from Smithy shape ``com.amazonaws.securityhub#ComplianceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ComplianceStatus: TypeAlias = Literal[
    "PASSED",
    "WARNING",
    "FAILED",
    "NOT_AVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "WARNING",
        "FAILED",
        "NOT_AVAILABLE",
    )
)


def serialize_json(value: ComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> ComplianceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComplianceStatus value: {data!r}")
    return cast(ComplianceStatus, data)
