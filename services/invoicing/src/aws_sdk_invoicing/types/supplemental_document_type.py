"""Generated from Smithy shape ``com.amazonaws.invoicing#SupplementalDocumentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

SupplementalDocumentType: TypeAlias = Literal[
    "GOVERNMENT_INVOICE",
    "TAX_E_INVOICE",
    "PAYMENT_RECEIPT",
    "SUPPLEMENT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GOVERNMENT_INVOICE",
        "TAX_E_INVOICE",
        "PAYMENT_RECEIPT",
        "SUPPLEMENT",
    )
)


def serialize_aws_json_1_0(value: SupplementalDocumentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SupplementalDocumentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupplementalDocumentType value: {data!r}")
    return cast(SupplementalDocumentType, data)
