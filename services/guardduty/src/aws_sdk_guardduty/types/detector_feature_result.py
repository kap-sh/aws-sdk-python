"""Generated from Smithy shape ``com.amazonaws.guardduty#DetectorFeatureResult``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

DetectorFeatureResult: TypeAlias = Literal[
    "FLOW_LOGS",
    "CLOUD_TRAIL",
    "DNS_LOGS",
    "S3_DATA_EVENTS",
    "EKS_AUDIT_LOGS",
    "EBS_MALWARE_PROTECTION",
    "RDS_LOGIN_EVENTS",
    "LAMBDA_NETWORK_LOGS",
    "EKS_RUNTIME_MONITORING",
    "RUNTIME_MONITORING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLOW_LOGS",
        "CLOUD_TRAIL",
        "DNS_LOGS",
        "S3_DATA_EVENTS",
        "EKS_AUDIT_LOGS",
        "EBS_MALWARE_PROTECTION",
        "RDS_LOGIN_EVENTS",
        "LAMBDA_NETWORK_LOGS",
        "EKS_RUNTIME_MONITORING",
        "RUNTIME_MONITORING",
    )
)


def serialize_json(value: DetectorFeatureResult) -> str:
    return value


def deserialize_json(data: str) -> DetectorFeatureResult:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DetectorFeatureResult value: {data!r}")
    return cast(DetectorFeatureResult, data)
