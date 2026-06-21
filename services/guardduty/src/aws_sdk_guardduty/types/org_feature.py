"""Generated from Smithy shape ``com.amazonaws.guardduty#OrgFeature``."""

from typing import Literal, TypeAlias, cast

OrgFeature: TypeAlias = Literal[
    "S3_DATA_EVENTS",
    "EKS_AUDIT_LOGS",
    "EBS_MALWARE_PROTECTION",
    "RDS_LOGIN_EVENTS",
    "LAMBDA_NETWORK_LOGS",
    "EKS_RUNTIME_MONITORING",
    "RUNTIME_MONITORING",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrgFeature) -> str:
    return value


def deserialize_json(data: str) -> OrgFeature:
    return cast(OrgFeature, data)
