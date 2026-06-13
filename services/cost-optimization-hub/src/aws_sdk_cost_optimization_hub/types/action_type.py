"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Rightsize",
        "Stop",
        "Upgrade",
        "PurchaseSavingsPlans",
        "PurchaseReservedInstances",
        "MigrateToGraviton",
        "Delete",
        "ScaleIn",
    )
)


def serialize_aws_json_1_0(value: ActionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)
