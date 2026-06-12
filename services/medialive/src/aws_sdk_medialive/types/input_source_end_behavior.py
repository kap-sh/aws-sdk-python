"""Generated from Smithy shape ``com.amazonaws.medialive#InputSourceEndBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input Source End Behavior"""
InputSourceEndBehavior: TypeAlias = Literal[
    "CONTINUE",
    "LOOP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUE",
        "LOOP",
    )
)


def serialize_json(value: InputSourceEndBehavior) -> str:
    return value


def deserialize_json(data: str) -> InputSourceEndBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputSourceEndBehavior value: {data!r}")
    return cast(InputSourceEndBehavior, data)
