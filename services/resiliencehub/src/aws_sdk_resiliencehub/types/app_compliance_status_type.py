"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppComplianceStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

AppComplianceStatusType: TypeAlias = Literal[
    "PolicyBreached",
    "PolicyMet",
    "NotAssessed",
    "ChangesDetected",
    "NotApplicable",
    "MissingPolicy",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PolicyBreached",
        "PolicyMet",
        "NotAssessed",
        "ChangesDetected",
        "NotApplicable",
        "MissingPolicy",
    )
)


def serialize_json(value: AppComplianceStatusType) -> str:
    return value


def deserialize_json(data: str) -> AppComplianceStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppComplianceStatusType value: {data!r}")
    return cast(AppComplianceStatusType, data)
