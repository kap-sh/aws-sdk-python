"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

PortalType: TypeAlias = Literal[
    "SITEWISE_PORTAL_V1",
    "SITEWISE_PORTAL_V2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SITEWISE_PORTAL_V1",
        "SITEWISE_PORTAL_V2",
    )
)


def serialize_json(value: PortalType) -> str:
    return value


def deserialize_json(data: str) -> PortalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PortalType value: {data!r}")
    return cast(PortalType, data)
