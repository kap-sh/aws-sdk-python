"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysisCompletionResultCode``."""

from typing import Literal, TypeAlias, cast

RouteAnalysisCompletionResultCode: TypeAlias = Literal[
    "CONNECTED",
    "NOT_CONNECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAnalysisCompletionResultCode) -> str:
    return value


def deserialize_json(data: str) -> RouteAnalysisCompletionResultCode:
    return cast(RouteAnalysisCompletionResultCode, data)
