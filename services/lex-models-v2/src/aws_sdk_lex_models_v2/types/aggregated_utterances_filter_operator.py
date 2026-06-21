"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AggregatedUtterancesFilterOperator``."""

from typing import Literal, TypeAlias, cast

AggregatedUtterancesFilterOperator: TypeAlias = Literal[
    "CO",
    "EQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedUtterancesFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> AggregatedUtterancesFilterOperator:
    return cast(AggregatedUtterancesFilterOperator, data)
