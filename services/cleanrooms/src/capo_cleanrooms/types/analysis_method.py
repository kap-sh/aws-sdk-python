"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisMethod``."""

from typing import Literal, TypeAlias, cast

AnalysisMethod: TypeAlias = Literal[
    "DIRECT_QUERY",
    "DIRECT_JOB",
    "MULTIPLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisMethod) -> str:
    return value


def deserialize_json(data: str) -> AnalysisMethod:
    return cast(AnalysisMethod, data)
