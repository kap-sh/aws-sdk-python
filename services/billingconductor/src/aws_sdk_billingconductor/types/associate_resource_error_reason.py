"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociateResourceErrorReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

AssociateResourceErrorReason: TypeAlias = Literal[
    "INVALID_ARN",
    "SERVICE_LIMIT_EXCEEDED",
    "ILLEGAL_CUSTOMLINEITEM",
    "INTERNAL_SERVER_EXCEPTION",
    "INVALID_BILLING_PERIOD_RANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_ARN",
        "SERVICE_LIMIT_EXCEEDED",
        "ILLEGAL_CUSTOMLINEITEM",
        "INTERNAL_SERVER_EXCEPTION",
        "INVALID_BILLING_PERIOD_RANGE",
    )
)


def serialize_json(value: AssociateResourceErrorReason) -> str:
    return value


def deserialize_json(data: str) -> AssociateResourceErrorReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssociateResourceErrorReason value: {data!r}"
        )
    return cast(AssociateResourceErrorReason, data)
