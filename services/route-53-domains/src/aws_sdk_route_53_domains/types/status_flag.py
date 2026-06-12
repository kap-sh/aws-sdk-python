"""Generated from Smithy shape ``com.amazonaws.route53domains#StatusFlag``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

StatusFlag: TypeAlias = Literal[
    "PENDING_ACCEPTANCE",
    "PENDING_CUSTOMER_ACTION",
    "PENDING_AUTHORIZATION",
    "PENDING_PAYMENT_VERIFICATION",
    "PENDING_SUPPORT_CASE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_ACCEPTANCE",
        "PENDING_CUSTOMER_ACTION",
        "PENDING_AUTHORIZATION",
        "PENDING_PAYMENT_VERIFICATION",
        "PENDING_SUPPORT_CASE",
    )
)


def serialize_aws_json_1_1(value: StatusFlag) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusFlag:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusFlag value: {data!r}")
    return cast(StatusFlag, data)
