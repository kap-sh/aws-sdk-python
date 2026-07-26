"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#SupportDataSetType``."""

from typing import Literal, TypeAlias, cast

SupportDataSetType: TypeAlias = Literal[
    "customer_support_contacts_data",
    "test_customer_support_contacts_data",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportDataSetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SupportDataSetType:
    return cast(SupportDataSetType, data)
