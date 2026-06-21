"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ActionType``."""

from typing import Literal, TypeAlias, cast

ActionType: TypeAlias = Literal[
    "Rightsize",
    "Stop",
    "Upgrade",
    "PurchaseSavingsPlans",
    "PurchaseReservedInstances",
    "MigrateToGraviton",
    "Delete",
    "ScaleIn",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActionType:
    return cast(ActionType, data)
