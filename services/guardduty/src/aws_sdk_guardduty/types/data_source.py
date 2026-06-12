"""Generated from Smithy shape ``com.amazonaws.guardduty#DataSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

DataSource: TypeAlias = Literal[
    "FLOW_LOGS",
    "CLOUD_TRAIL",
    "DNS_LOGS",
    "S3_LOGS",
    "KUBERNETES_AUDIT_LOGS",
    "EC2_MALWARE_SCAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLOW_LOGS",
        "CLOUD_TRAIL",
        "DNS_LOGS",
        "S3_LOGS",
        "KUBERNETES_AUDIT_LOGS",
        "EC2_MALWARE_SCAN",
    )
)


def serialize_json(value: DataSource) -> str:
    return value


def deserialize_json(data: str) -> DataSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSource value: {data!r}")
    return cast(DataSource, data)
