"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityOrigin``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

OpportunityOrigin: TypeAlias = Literal[
    "AWS Referral",
    "Partner Referral",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS Referral",
        "Partner Referral",
    )
)


def serialize_aws_json_1_0(value: OpportunityOrigin) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpportunityOrigin:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpportunityOrigin value: {data!r}")
    return cast(OpportunityOrigin, data)
