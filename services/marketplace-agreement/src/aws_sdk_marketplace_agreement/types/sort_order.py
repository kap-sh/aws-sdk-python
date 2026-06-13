"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

SortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASCENDING",
        "DESCENDING",
    )
)


def serialize_aws_json_1_0(value: SortOrder) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortOrder value: {data!r}")
    return cast(SortOrder, data)
