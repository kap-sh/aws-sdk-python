"""Generated from Smithy shape ``com.amazonaws.guardduty#SignalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

SignalType: TypeAlias = Literal[
    "FINDING",
    "CLOUD_TRAIL",
    "S3_DATA_EVENTS",
    "EKS_AUDIT_LOGS",
    "FLOW_LOGS",
    "DNS_LOGS",
    "RUNTIME_MONITORING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FINDING",
        "CLOUD_TRAIL",
        "S3_DATA_EVENTS",
        "EKS_AUDIT_LOGS",
        "FLOW_LOGS",
        "DNS_LOGS",
        "RUNTIME_MONITORING",
    )
)


def serialize_json(value: SignalType) -> str:
    return value


def deserialize_json(data: str) -> SignalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SignalType value: {data!r}")
    return cast(SignalType, data)
