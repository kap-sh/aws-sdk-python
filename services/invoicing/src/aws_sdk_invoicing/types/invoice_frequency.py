"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

InvoiceFrequency: TypeAlias = Literal[
    "ONE_TIME",
    "RECURRING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_TIME",
        "RECURRING",
    )
)


def serialize_aws_json_1_0(value: InvoiceFrequency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvoiceFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InvoiceFrequency value: {data!r}")
    return cast(InvoiceFrequency, data)
