"""Generated from Smithy shape ``com.amazonaws.invoicing#EinvoiceDeliveryDocumentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

EinvoiceDeliveryDocumentType: TypeAlias = Literal[
    "AWS_CLOUD_INVOICE",
    "AWS_CLOUD_CREDIT_MEMO",
    "AWS_MARKETPLACE_INVOICE",
    "AWS_MARKETPLACE_CREDIT_MEMO",
    "AWS_REQUEST_FOR_PAYMENT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_CLOUD_INVOICE",
        "AWS_CLOUD_CREDIT_MEMO",
        "AWS_MARKETPLACE_INVOICE",
        "AWS_MARKETPLACE_CREDIT_MEMO",
        "AWS_REQUEST_FOR_PAYMENT",
    )
)


def serialize_aws_json_1_0(value: EinvoiceDeliveryDocumentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EinvoiceDeliveryDocumentType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EinvoiceDeliveryDocumentType value: {data!r}"
        )
    return cast(EinvoiceDeliveryDocumentType, data)
