"""Generated from Smithy shape ``com.amazonaws.freetier#AccountPlanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_freetier.errors import DeserializationError

AccountPlanType: TypeAlias = Literal[
    "FREE",
    "PAID",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FREE",
        "PAID",
    )
)


def serialize_aws_json_1_0(value: AccountPlanType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccountPlanType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountPlanType value: {data!r}")
    return cast(AccountPlanType, data)
