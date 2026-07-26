"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyAggregationType``."""

from typing import Literal, TypeAlias, cast

DifferentialPrivacyAggregationType: TypeAlias = Literal[
    "AVG",
    "COUNT",
    "COUNT_DISTINCT",
    "SUM",
    "STDDEV",
]


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyAggregationType) -> str:
    return value


def deserialize_json(data: str) -> DifferentialPrivacyAggregationType:
    return cast(DifferentialPrivacyAggregationType, data)
