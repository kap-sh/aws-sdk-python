"""Generated from Smithy shape ``com.amazonaws.transcribe#PiiEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe.errors import DeserializationError

PiiEntityType: TypeAlias = Literal[
    "BANK_ACCOUNT_NUMBER",
    "BANK_ROUTING",
    "CREDIT_DEBIT_NUMBER",
    "CREDIT_DEBIT_CVV",
    "CREDIT_DEBIT_EXPIRY",
    "PIN",
    "EMAIL",
    "ADDRESS",
    "NAME",
    "PHONE",
    "SSN",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BANK_ACCOUNT_NUMBER",
        "BANK_ROUTING",
        "CREDIT_DEBIT_NUMBER",
        "CREDIT_DEBIT_CVV",
        "CREDIT_DEBIT_EXPIRY",
        "PIN",
        "EMAIL",
        "ADDRESS",
        "NAME",
        "PHONE",
        "SSN",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: PiiEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PiiEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PiiEntityType value: {data!r}")
    return cast(PiiEntityType, data)
