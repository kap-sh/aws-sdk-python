"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#SupportDataSetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_commerce_analytics.errors import DeserializationError

SupportDataSetType: TypeAlias = Literal[
    "customer_support_contacts_data",
    "test_customer_support_contacts_data",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "customer_support_contacts_data",
        "test_customer_support_contacts_data",
    )
)


def serialize_aws_json_1_1(value: SupportDataSetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SupportDataSetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupportDataSetType value: {data!r}")
    return cast(SupportDataSetType, data)
