"""Generated from Smithy shape ``com.amazonaws.connect#RoutingCriteriaStepStatus``."""

from typing import Literal, TypeAlias, cast

RoutingCriteriaStepStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "JOINED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingCriteriaStepStatus) -> str:
    return value


def deserialize_json(data: str) -> RoutingCriteriaStepStatus:
    return cast(RoutingCriteriaStepStatus, data)
