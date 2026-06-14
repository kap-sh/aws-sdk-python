"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#TryItState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>Represents the try it state for a product REST endpoint page.</p>"""
TryItState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: TryItState) -> str:
    return value


def deserialize_json(data: str) -> TryItState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TryItState value: {data!r}")
    return cast(TryItState, data)
