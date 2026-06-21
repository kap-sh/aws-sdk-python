"""Generated from Smithy shape ``com.amazonaws.artifact#CustomerAgreementState``."""

from typing import Literal, TypeAlias, cast

CustomerAgreementState: TypeAlias = Literal[
    "ACTIVE",
    "CUSTOMER_TERMINATED",
    "AWS_TERMINATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerAgreementState) -> str:
    return value


def deserialize_json(data: str) -> CustomerAgreementState:
    return cast(CustomerAgreementState, data)
