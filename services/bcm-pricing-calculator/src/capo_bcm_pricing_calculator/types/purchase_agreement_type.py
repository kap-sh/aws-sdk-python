"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#PurchaseAgreementType``."""

from typing import Literal, TypeAlias, cast

PurchaseAgreementType: TypeAlias = Literal[
    "SAVINGS_PLANS",
    "RESERVED_INSTANCE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PurchaseAgreementType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PurchaseAgreementType:
    return cast(PurchaseAgreementType, data)
