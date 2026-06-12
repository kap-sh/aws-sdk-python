"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ComplianceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ComplianceStatus: TypeAlias = Literal[
    "PolicyBreached",
    "PolicyMet",
    "NotApplicable",
    "MissingPolicy",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PolicyBreached",
        "PolicyMet",
        "NotApplicable",
        "MissingPolicy",
    )
)


def serialize_json(value: ComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> ComplianceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComplianceStatus value: {data!r}")
    return cast(ComplianceStatus, data)
