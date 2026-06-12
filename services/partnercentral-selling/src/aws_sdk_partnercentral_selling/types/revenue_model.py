"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#RevenueModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

RevenueModel: TypeAlias = Literal[
    "Contract",
    "Pay-as-you-go",
    "Subscription",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Contract",
        "Pay-as-you-go",
        "Subscription",
    )
)


def serialize_aws_json_1_0(value: RevenueModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RevenueModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RevenueModel value: {data!r}")
    return cast(RevenueModel, data)
