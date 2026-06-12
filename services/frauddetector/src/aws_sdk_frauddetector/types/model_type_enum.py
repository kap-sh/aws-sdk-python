"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

ModelTypeEnum: TypeAlias = Literal[
    "ONLINE_FRAUD_INSIGHTS",
    "TRANSACTION_FRAUD_INSIGHTS",
    "ACCOUNT_TAKEOVER_INSIGHTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONLINE_FRAUD_INSIGHTS",
        "TRANSACTION_FRAUD_INSIGHTS",
        "ACCOUNT_TAKEOVER_INSIGHTS",
    )
)


def serialize_aws_json_1_1(value: ModelTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelTypeEnum value: {data!r}")
    return cast(ModelTypeEnum, data)
