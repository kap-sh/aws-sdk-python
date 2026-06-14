"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PublishStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>Represents a publish status.</p>"""
PublishStatus: TypeAlias = Literal[
    "PUBLISHED",
    "PUBLISH_IN_PROGRESS",
    "PUBLISH_FAILED",
    "DISABLE_IN_PROGRESS",
    "DISABLE_FAILED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISHED",
        "PUBLISH_IN_PROGRESS",
        "PUBLISH_FAILED",
        "DISABLE_IN_PROGRESS",
        "DISABLE_FAILED",
        "DISABLED",
    )
)


def serialize_json(value: PublishStatus) -> str:
    return value


def deserialize_json(data: str) -> PublishStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PublishStatus value: {data!r}")
    return cast(PublishStatus, data)
