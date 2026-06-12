"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Destination``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_model_building_service.errors import DeserializationError

Destination: TypeAlias = Literal[
    "CLOUDWATCH_LOGS",
    "S3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUDWATCH_LOGS",
        "S3",
    )
)


def serialize_json(value: Destination) -> str:
    return value


def deserialize_json(data: str) -> Destination:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Destination value: {data!r}")
    return cast(Destination, data)
