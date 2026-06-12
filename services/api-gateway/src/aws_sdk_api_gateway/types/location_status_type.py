"""Generated from Smithy shape ``com.amazonaws.apigateway#LocationStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_api_gateway.errors import DeserializationError

LocationStatusType: TypeAlias = Literal[
    "DOCUMENTED",
    "UNDOCUMENTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOCUMENTED",
        "UNDOCUMENTED",
    )
)


def serialize_json(value: LocationStatusType) -> str:
    return value


def deserialize_json(data: str) -> LocationStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LocationStatusType value: {data!r}")
    return cast(LocationStatusType, data)
