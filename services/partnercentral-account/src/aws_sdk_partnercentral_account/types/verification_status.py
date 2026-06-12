"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#VerificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

VerificationStatus: TypeAlias = Literal[
    "PENDING_CUSTOMER_ACTION",
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
    "REJECTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_CUSTOMER_ACTION",
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
        "REJECTED",
    )
)


def serialize_aws_json_1_0(value: VerificationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VerificationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VerificationStatus value: {data!r}")
    return cast(VerificationStatus, data)
