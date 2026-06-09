"""Generated from Smithy shape ``com.amazonaws.lambda#FullDocument``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

FullDocument: TypeAlias = Literal[
    "UpdateLookup",
    "Default",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UpdateLookup",
        "Default",
    )
)


def serialize_json(value: FullDocument) -> str:
    return value


def deserialize_json(data: str) -> FullDocument:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FullDocument value: {data!r}")
    return cast(FullDocument, data)
