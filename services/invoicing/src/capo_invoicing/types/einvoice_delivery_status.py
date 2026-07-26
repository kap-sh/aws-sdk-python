"""Generated from Smithy shape ``com.amazonaws.invoicing#EinvoiceDeliveryStatus``."""

from typing import Literal, TypeAlias, cast

EinvoiceDeliveryStatus: TypeAlias = Literal[
    "DELIVERED",
    "NOT_DELIVERED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EinvoiceDeliveryStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EinvoiceDeliveryStatus:
    return cast(EinvoiceDeliveryStatus, data)
