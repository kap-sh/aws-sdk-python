"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AggregatedUtterancesSortAttribute``."""

from typing import Literal, TypeAlias, cast

AggregatedUtterancesSortAttribute: TypeAlias = Literal[
    "HitCount",
    "MissedCount",
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedUtterancesSortAttribute) -> str:
    return value


def deserialize_json(data: str) -> AggregatedUtterancesSortAttribute:
    return cast(AggregatedUtterancesSortAttribute, data)
