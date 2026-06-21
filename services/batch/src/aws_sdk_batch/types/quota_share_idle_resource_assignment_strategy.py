"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareIdleResourceAssignmentStrategy``."""

from typing import Literal, TypeAlias, cast

QuotaShareIdleResourceAssignmentStrategy: TypeAlias = Literal["FIFO",]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareIdleResourceAssignmentStrategy) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareIdleResourceAssignmentStrategy:
    return cast(QuotaShareIdleResourceAssignmentStrategy, data)
