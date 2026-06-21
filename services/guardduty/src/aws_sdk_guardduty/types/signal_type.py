"""Generated from Smithy shape ``com.amazonaws.guardduty#SignalType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: SignalType) -> str:
    return value


def deserialize_json(data: str) -> SignalType:
    return cast(SignalType, data)
