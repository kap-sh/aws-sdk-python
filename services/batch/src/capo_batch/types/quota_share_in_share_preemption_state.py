"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareInSharePreemptionState``."""

from typing import Literal, TypeAlias, cast

QuotaShareInSharePreemptionState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareInSharePreemptionState) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareInSharePreemptionState:
    return cast(QuotaShareInSharePreemptionState, data)
