"""Generated from Smithy shape ``com.amazonaws.billingconductor#ComputationRuleEnum``."""

from typing import Literal, TypeAlias, cast

"""The display settings of the custom line item"""
ComputationRuleEnum: TypeAlias = Literal[
    "ITEMIZED",
    "CONSOLIDATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationRuleEnum) -> str:
    return value


def deserialize_json(data: str) -> ComputationRuleEnum:
    return cast(ComputationRuleEnum, data)
