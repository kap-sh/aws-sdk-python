"""Generated from Smithy shape ``com.amazonaws.inspector2#CisRuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisRuleStatus: TypeAlias = Literal[
    "FAILED",
    "PASSED",
    "NOT_EVALUATED",
    "INFORMATIONAL",
    "UNKNOWN",
    "NOT_APPLICABLE",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "PASSED",
        "NOT_EVALUATED",
        "INFORMATIONAL",
        "UNKNOWN",
        "NOT_APPLICABLE",
        "ERROR",
    )
)


def serialize_json(value: CisRuleStatus) -> str:
    return value


def deserialize_json(data: str) -> CisRuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisRuleStatus value: {data!r}")
    return cast(CisRuleStatus, data)
