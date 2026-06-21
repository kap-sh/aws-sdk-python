"""Generated from Smithy shape ``com.amazonaws.guardduty#FreeTrialFeatureResult``."""

from typing import Literal, TypeAlias, cast

FreeTrialFeatureResult: TypeAlias = Literal[
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
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialFeatureResult) -> str:
    return value


def deserialize_json(data: str) -> FreeTrialFeatureResult:
    return cast(FreeTrialFeatureResult, data)
