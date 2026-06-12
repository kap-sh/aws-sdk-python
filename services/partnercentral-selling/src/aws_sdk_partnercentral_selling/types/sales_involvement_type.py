"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SalesInvolvementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

SalesInvolvementType: TypeAlias = Literal[
    "For Visibility Only",
    "Co-Sell",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "For Visibility Only",
        "Co-Sell",
    )
)


def serialize_aws_json_1_0(value: SalesInvolvementType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SalesInvolvementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SalesInvolvementType value: {data!r}")
    return cast(SalesInvolvementType, data)
