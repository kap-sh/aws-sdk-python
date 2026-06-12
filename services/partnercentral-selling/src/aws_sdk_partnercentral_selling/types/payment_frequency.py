"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#PaymentFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

PaymentFrequency: TypeAlias = Literal["Monthly",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("Monthly",))


def serialize_aws_json_1_0(value: PaymentFrequency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PaymentFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentFrequency value: {data!r}")
    return cast(PaymentFrequency, data)
