"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

OpportunityType: TypeAlias = Literal[
    "Net New Business",
    "Flat Renewal",
    "Expansion",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Net New Business",
        "Flat Renewal",
        "Expansion",
    )
)


def serialize_aws_json_1_0(value: OpportunityType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpportunityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpportunityType value: {data!r}")
    return cast(OpportunityType, data)
