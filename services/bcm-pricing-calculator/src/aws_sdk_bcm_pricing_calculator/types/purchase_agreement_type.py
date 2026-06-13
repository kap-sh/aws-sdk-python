"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#PurchaseAgreementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

PurchaseAgreementType: TypeAlias = Literal[
    "SAVINGS_PLANS",
    "RESERVED_INSTANCE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAVINGS_PLANS",
        "RESERVED_INSTANCE",
    )
)


def serialize_aws_json_1_0(value: PurchaseAgreementType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PurchaseAgreementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PurchaseAgreementType value: {data!r}")
    return cast(PurchaseAgreementType, data)
