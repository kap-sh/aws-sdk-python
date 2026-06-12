"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysisCompletionResultCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

RouteAnalysisCompletionResultCode: TypeAlias = Literal[
    "CONNECTED",
    "NOT_CONNECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED",
        "NOT_CONNECTED",
    )
)


def serialize_json(value: RouteAnalysisCompletionResultCode) -> str:
    return value


def deserialize_json(data: str) -> RouteAnalysisCompletionResultCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteAnalysisCompletionResultCode value: {data!r}"
        )
    return cast(RouteAnalysisCompletionResultCode, data)
