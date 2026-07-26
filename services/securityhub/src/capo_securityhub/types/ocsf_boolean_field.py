"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfBooleanField``."""

from typing import Literal, TypeAlias, cast

OcsfBooleanField: TypeAlias = Literal[
    "compliance.assessments.meets_criteria",
    "vulnerabilities.is_exploit_available",
    "vulnerabilities.is_fix_available",
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfBooleanField) -> str:
    return value


def deserialize_json(data: str) -> OcsfBooleanField:
    return cast(OcsfBooleanField, data)
