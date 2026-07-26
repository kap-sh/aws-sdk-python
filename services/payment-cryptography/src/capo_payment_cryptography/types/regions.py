"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#Regions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_payment_cryptography.types.region

Regions: TypeAlias = list["capo_payment_cryptography.types.region.Region"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Regions) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Regions:
    return list(data)
