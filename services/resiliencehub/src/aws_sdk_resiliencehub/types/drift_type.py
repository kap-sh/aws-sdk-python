"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DriftType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

DriftType: TypeAlias = Literal[
    "ApplicationCompliance",
    "AppComponentResiliencyComplianceStatus",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ApplicationCompliance",
        "AppComponentResiliencyComplianceStatus",
    )
)


def serialize_json(value: DriftType) -> str:
    return value


def deserialize_json(data: str) -> DriftType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DriftType value: {data!r}")
    return cast(DriftType, data)
