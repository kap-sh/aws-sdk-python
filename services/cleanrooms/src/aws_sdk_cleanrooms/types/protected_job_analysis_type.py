"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobAnalysisType``."""

from typing import Literal, TypeAlias, cast

ProtectedJobAnalysisType: TypeAlias = Literal["DIRECT_ANALYSIS",]


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobAnalysisType) -> str:
    return value


def deserialize_json(data: str) -> ProtectedJobAnalysisType:
    return cast(ProtectedJobAnalysisType, data)
