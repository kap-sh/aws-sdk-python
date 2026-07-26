"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#PublishStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: PublishStatus) -> str:
    return value


def deserialize_json(data: str) -> PublishStatus:
    return cast(PublishStatus, data)
