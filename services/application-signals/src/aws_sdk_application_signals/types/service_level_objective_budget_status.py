"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveBudgetStatus``."""

from typing import Literal, TypeAlias, cast

ServiceLevelObjectiveBudgetStatus: TypeAlias = Literal[
    "OK",
    "WARNING",
    "BREACHED",
    "INSUFFICIENT_DATA",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveBudgetStatus) -> str:
    return value


def deserialize_json(data: str) -> ServiceLevelObjectiveBudgetStatus:
    return cast(ServiceLevelObjectiveBudgetStatus, data)
