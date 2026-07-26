"""Generated from Smithy shape ``com.amazonaws.guardduty#DataSource``."""

from typing import Literal, TypeAlias, cast

DataSource: TypeAlias = Literal[
    "FLOW_LOGS",
    "CLOUD_TRAIL",
    "DNS_LOGS",
    "S3_LOGS",
    "KUBERNETES_AUDIT_LOGS",
    "EC2_MALWARE_SCAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSource) -> str:
    return value


def deserialize_json(data: str) -> DataSource:
    return cast(DataSource, data)
