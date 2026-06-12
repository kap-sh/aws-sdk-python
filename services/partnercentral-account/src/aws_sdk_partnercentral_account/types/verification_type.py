"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#VerificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_account.errors import DeserializationError

VerificationType: TypeAlias = Literal[
    "BUSINESS_VERIFICATION",
    "REGISTRANT_VERIFICATION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUSINESS_VERIFICATION",
        "REGISTRANT_VERIFICATION",
    )
)


def serialize_aws_json_1_0(value: VerificationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VerificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VerificationType value: {data!r}")
    return cast(VerificationType, data)
