"""Generated from Smithy shape ``com.amazonaws.invoicing#SupplementalDocumentType``."""

from typing import Literal, TypeAlias, cast

SupplementalDocumentType: TypeAlias = Literal[
    "GOVERNMENT_INVOICE",
    "TAX_E_INVOICE",
    "PAYMENT_RECEIPT",
    "SUPPLEMENT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupplementalDocumentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SupplementalDocumentType:
    return cast(SupplementalDocumentType, data)
