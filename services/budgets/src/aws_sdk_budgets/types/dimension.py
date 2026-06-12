"""Generated from Smithy shape ``com.amazonaws.budgets#Dimension``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

Dimension: TypeAlias = Literal[
    "AZ",
    "INSTANCE_TYPE",
    "LINKED_ACCOUNT",
    "LINKED_ACCOUNT_NAME",
    "OPERATION",
    "PURCHASE_TYPE",
    "REGION",
    "SERVICE",
    "SERVICE_CODE",
    "USAGE_TYPE",
    "USAGE_TYPE_GROUP",
    "RECORD_TYPE",
    "OPERATING_SYSTEM",
    "TENANCY",
    "SCOPE",
    "PLATFORM",
    "SUBSCRIPTION_ID",
    "LEGAL_ENTITY_NAME",
    "INVOICING_ENTITY",
    "DEPLOYMENT_OPTION",
    "DATABASE_ENGINE",
    "CACHE_ENGINE",
    "INSTANCE_TYPE_FAMILY",
    "BILLING_ENTITY",
    "RESERVATION_ID",
    "RESOURCE_ID",
    "RIGHTSIZING_TYPE",
    "SAVINGS_PLANS_TYPE",
    "SAVINGS_PLAN_ARN",
    "PAYMENT_OPTION",
    "RESERVATION_MODIFIED",
    "TAG_KEY",
    "COST_CATEGORY_NAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AZ",
        "INSTANCE_TYPE",
        "LINKED_ACCOUNT",
        "LINKED_ACCOUNT_NAME",
        "OPERATION",
        "PURCHASE_TYPE",
        "REGION",
        "SERVICE",
        "SERVICE_CODE",
        "USAGE_TYPE",
        "USAGE_TYPE_GROUP",
        "RECORD_TYPE",
        "OPERATING_SYSTEM",
        "TENANCY",
        "SCOPE",
        "PLATFORM",
        "SUBSCRIPTION_ID",
        "LEGAL_ENTITY_NAME",
        "INVOICING_ENTITY",
        "DEPLOYMENT_OPTION",
        "DATABASE_ENGINE",
        "CACHE_ENGINE",
        "INSTANCE_TYPE_FAMILY",
        "BILLING_ENTITY",
        "RESERVATION_ID",
        "RESOURCE_ID",
        "RIGHTSIZING_TYPE",
        "SAVINGS_PLANS_TYPE",
        "SAVINGS_PLAN_ARN",
        "PAYMENT_OPTION",
        "RESERVATION_MODIFIED",
        "TAG_KEY",
        "COST_CATEGORY_NAME",
    )
)


def serialize_aws_json_1_1(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Dimension:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Dimension value: {data!r}")
    return cast(Dimension, data)
