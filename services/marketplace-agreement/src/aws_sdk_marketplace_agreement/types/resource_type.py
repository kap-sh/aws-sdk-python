"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "Agreement",
    "AgreementRequest",
    "AgreementProposal",
    "Charge",
    "PaymentRequest",
    "Invoice",
    "AgreementCancellationRequest",
    "BillingAdjustmentRequest",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Agreement",
        "AgreementRequest",
        "AgreementProposal",
        "Charge",
        "PaymentRequest",
        "Invoice",
        "AgreementCancellationRequest",
        "BillingAdjustmentRequest",
    )
)


def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
