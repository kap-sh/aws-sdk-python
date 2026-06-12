"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfBooleanField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

OcsfBooleanField: TypeAlias = Literal[
    "compliance.assessments.meets_criteria",
    "vulnerabilities.is_exploit_available",
    "vulnerabilities.is_fix_available",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "compliance.assessments.meets_criteria",
        "vulnerabilities.is_exploit_available",
        "vulnerabilities.is_fix_available",
    )
)


def serialize_json(value: OcsfBooleanField) -> str:
    return value


def deserialize_json(data: str) -> OcsfBooleanField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OcsfBooleanField value: {data!r}")
    return cast(OcsfBooleanField, data)
