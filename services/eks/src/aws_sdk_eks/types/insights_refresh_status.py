"""Generated from Smithy shape ``com.amazonaws.eks#InsightsRefreshStatus``."""

from typing import Literal, TypeAlias, cast

InsightsRefreshStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InsightsRefreshStatus) -> str:
    return value


def deserialize_json(data: str) -> InsightsRefreshStatus:
    return cast(InsightsRefreshStatus, data)
