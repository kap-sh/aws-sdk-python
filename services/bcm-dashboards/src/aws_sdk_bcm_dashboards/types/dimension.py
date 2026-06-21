"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#Dimension``."""

from typing import Literal, TypeAlias, cast

Dimension: TypeAlias = Literal[
    "AZ",
    "INSTANCE_TYPE",
    "LINKED_ACCOUNT",
    "OPERATION",
    "PURCHASE_TYPE",
    "REGION",
    "SERVICE",
    "USAGE_TYPE",
    "USAGE_TYPE_GROUP",
    "RECORD_TYPE",
    "RESOURCE_ID",
    "SUBSCRIPTION_ID",
    "TAG_KEY",
    "OPERATING_SYSTEM",
    "TENANCY",
    "BILLING_ENTITY",
    "RESERVATION_ID",
    "COST_CATEGORY_NAME",
    "DATABASE_ENGINE",
    "LEGAL_ENTITY_NAME",
    "SAVINGS_PLANS_TYPE",
    "INSTANCE_TYPE_FAMILY",
    "CACHE_ENGINE",
    "DEPLOYMENT_OPTION",
    "SCOPE",
    "PLATFORM",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Dimension:
    return cast(Dimension, data)
