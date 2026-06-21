"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SelectedAnalysisMethod``."""

from typing import Literal, TypeAlias, cast

SelectedAnalysisMethod: TypeAlias = Literal[
    "DIRECT_QUERY",
    "DIRECT_JOB",
]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedAnalysisMethod) -> str:
    return value


def deserialize_json(data: str) -> SelectedAnalysisMethod:
    return cast(SelectedAnalysisMethod, data)
