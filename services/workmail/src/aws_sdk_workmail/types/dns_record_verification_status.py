"""Generated from Smithy shape ``com.amazonaws.workmail#DnsRecordVerificationStatus``."""

from typing import Literal, TypeAlias, cast

DnsRecordVerificationStatus: TypeAlias = Literal[
    "PENDING",
    "VERIFIED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRecordVerificationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DnsRecordVerificationStatus:
    return cast(DnsRecordVerificationStatus, data)
