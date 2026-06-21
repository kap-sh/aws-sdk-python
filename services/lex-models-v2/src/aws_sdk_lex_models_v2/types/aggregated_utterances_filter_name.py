"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AggregatedUtterancesFilterName``."""

from typing import Literal, TypeAlias, cast

AggregatedUtterancesFilterName: TypeAlias = Literal["Utterance",]


# --- restJson1 ser/de ---
def serialize_json(value: AggregatedUtterancesFilterName) -> str:
    return value


def deserialize_json(data: str) -> AggregatedUtterancesFilterName:
    return cast(AggregatedUtterancesFilterName, data)
