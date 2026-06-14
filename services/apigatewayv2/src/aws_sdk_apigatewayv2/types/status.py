"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#Status``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>The status.</p>"""
Status: TypeAlias = Literal[
    "AVAILABLE",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "IN_PROGRESS",
        "FAILED",
    )
)


def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Status value: {data!r}")
    return cast(Status, data)
