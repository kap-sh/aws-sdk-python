"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#InvoiceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

InvoiceType: TypeAlias = Literal[
    "INVOICE",
    "CREDIT_MEMO",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVOICE",
        "CREDIT_MEMO",
    )
)


def serialize_aws_json_1_0(value: InvoiceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvoiceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvoiceType value: {data!r}")
    return cast(InvoiceType, data)
