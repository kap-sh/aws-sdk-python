"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociateResourceErrorReason``."""

from typing import Literal, TypeAlias, cast

AssociateResourceErrorReason: TypeAlias = Literal[
    "INVALID_ARN",
    "SERVICE_LIMIT_EXCEEDED",
    "ILLEGAL_CUSTOMLINEITEM",
    "INTERNAL_SERVER_EXCEPTION",
    "INVALID_BILLING_PERIOD_RANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourceErrorReason) -> str:
    return value


def deserialize_json(data: str) -> AssociateResourceErrorReason:
    return cast(AssociateResourceErrorReason, data)
