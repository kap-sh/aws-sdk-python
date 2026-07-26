"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CostCurrency``."""

from typing import Literal, TypeAlias, cast

CostCurrency: TypeAlias = Literal["USD",]


# --- restJson1 ser/de ---
def serialize_json(value: CostCurrency) -> str:
    return value


def deserialize_json(data: str) -> CostCurrency:
    return cast(CostCurrency, data)
