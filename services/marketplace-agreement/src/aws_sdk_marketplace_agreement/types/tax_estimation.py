"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#TaxEstimation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

TaxEstimation: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_aws_json_1_0(value: TaxEstimation) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TaxEstimation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaxEstimation value: {data!r}")
    return cast(TaxEstimation, data)
