"""Generated from Smithy shape ``com.amazonaws.devopsguru#CostEstimationStackNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.stack_name

CostEstimationStackNames: TypeAlias = list[
    "capo_devops_guru.types.stack_name.StackName"
]


# --- restJson1 ser/de ---
def serialize_json(value: CostEstimationStackNames) -> list:
    return list(value)


def deserialize_json(data: list) -> CostEstimationStackNames:
    return list(data)
