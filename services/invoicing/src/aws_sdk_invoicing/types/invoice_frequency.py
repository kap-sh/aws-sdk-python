"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceFrequency``."""

from typing import Literal, TypeAlias, cast

InvoiceFrequency: TypeAlias = Literal[
    "ONE_TIME",
    "RECURRING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceFrequency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvoiceFrequency:
    return cast(InvoiceFrequency, data)
