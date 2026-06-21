"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#ActionType``."""

from typing import Literal, TypeAlias, cast

ActionType: TypeAlias = Literal[
    "ADD_ALTERNATE_BILLING_CONTACT",
    "CREATE_ANOMALY_MONITOR",
    "CREATE_BUDGET",
    "ENABLE_COST_OPTIMIZATION_HUB",
    "MIGRATE_TO_GRANULAR_PERMISSIONS",
    "PAYMENTS_DUE",
    "PAYMENTS_PAST_DUE",
    "REVIEW_ANOMALIES",
    "REVIEW_BUDGET_ALERTS",
    "REVIEW_BUDGETS_EXCEEDED",
    "REVIEW_EXPIRING_RI",
    "REVIEW_EXPIRING_SP",
    "REVIEW_FREETIER_USAGE_ALERTS",
    "REVIEW_FREETIER_CREDITS_REMAINING",
    "REVIEW_FREETIER_DAYS_REMAINING",
    "REVIEW_SAVINGS_OPPORTUNITY_RECOMMENDATIONS",
    "UPDATE_EXPIRED_PAYMENT_METHOD",
    "UPDATE_INVALID_PAYMENT_METHOD",
    "UPDATE_TAX_EXEMPTION_CERTIFICATE",
    "UPDATE_TAX_REGISTRATION_NUMBER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActionType:
    return cast(ActionType, data)
