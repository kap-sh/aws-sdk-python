"""Generated from Smithy shape ``com.amazonaws.guardduty#OrgFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "S3_DATA_EVENTS",
        "EKS_AUDIT_LOGS",
        "EBS_MALWARE_PROTECTION",
        "RDS_LOGIN_EVENTS",
        "LAMBDA_NETWORK_LOGS",
        "EKS_RUNTIME_MONITORING",
        "RUNTIME_MONITORING",
    )
)


def serialize_json(value: OrgFeature) -> str:
    return value


def deserialize_json(data: str) -> OrgFeature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrgFeature value: {data!r}")
    return cast(OrgFeature, data)
