"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

UsageFeature: TypeAlias = Literal[
    "FLOW_LOGS",
    "CLOUD_TRAIL",
    "DNS_LOGS",
    "S3_DATA_EVENTS",
    "EKS_AUDIT_LOGS",
    "EBS_MALWARE_PROTECTION",
    "RDS_LOGIN_EVENTS",
    "LAMBDA_NETWORK_LOGS",
    "EKS_RUNTIME_MONITORING",
    "EC2_RUNTIME_MONITORING",
    "FARGATE_RUNTIME_MONITORING",
    "RDS_DBI_PROTECTION_PROVISIONED",
    "RDS_DBI_PROTECTION_SERVERLESS",
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
        "EC2_RUNTIME_MONITORING",
        "FARGATE_RUNTIME_MONITORING",
        "RDS_DBI_PROTECTION_PROVISIONED",
        "RDS_DBI_PROTECTION_SERVERLESS",
    )
)


def serialize_json(value: UsageFeature) -> str:
    return value


def deserialize_json(data: str) -> UsageFeature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageFeature value: {data!r}")
    return cast(UsageFeature, data)
