"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Timing``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

Timing: TypeAlias = Literal[
    "ON_ACCEPTANCE",
    "SCHEDULED",
    "BILLING_PERIOD",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_ACCEPTANCE",
        "SCHEDULED",
        "BILLING_PERIOD",
    )
)


def serialize_aws_json_1_0(value: Timing) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Timing:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Timing value: {data!r}")
    return cast(Timing, data)
