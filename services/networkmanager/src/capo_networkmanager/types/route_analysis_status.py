"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysisStatus``."""

from typing import Literal, TypeAlias, cast

RouteAnalysisStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAnalysisStatus) -> str:
    return value


def deserialize_json(data: str) -> RouteAnalysisStatus:
    return cast(RouteAnalysisStatus, data)
