"""Generated from Smithy shape ``com.amazonaws.workmail#DnsRecordVerificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

DnsRecordVerificationStatus: TypeAlias = Literal[
    "PENDING",
    "VERIFIED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "VERIFIED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: DnsRecordVerificationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DnsRecordVerificationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DnsRecordVerificationStatus value: {data!r}"
        )
    return cast(DnsRecordVerificationStatus, data)
