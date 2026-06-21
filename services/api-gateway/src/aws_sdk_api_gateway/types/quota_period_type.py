"""Generated from Smithy shape ``com.amazonaws.apigateway#QuotaPeriodType``."""

from typing import Literal, TypeAlias, cast

QuotaPeriodType: TypeAlias = Literal[
    "DAY",
    "WEEK",
    "MONTH",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaPeriodType) -> str:
    return value


def deserialize_json(data: str) -> QuotaPeriodType:
    return cast(QuotaPeriodType, data)
