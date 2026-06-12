"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#EndpointStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_identity.errors import DeserializationError

EndpointStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: EndpointStatus) -> str:
    return value


def deserialize_json(data: str) -> EndpointStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointStatus value: {data!r}")
    return cast(EndpointStatus, data)
