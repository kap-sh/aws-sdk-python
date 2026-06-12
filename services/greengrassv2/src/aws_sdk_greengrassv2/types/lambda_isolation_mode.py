"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaIsolationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

LambdaIsolationMode: TypeAlias = Literal[
    "GreengrassContainer",
    "NoContainer",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GreengrassContainer",
        "NoContainer",
    )
)


def serialize_json(value: LambdaIsolationMode) -> str:
    return value


def deserialize_json(data: str) -> LambdaIsolationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LambdaIsolationMode value: {data!r}")
    return cast(LambdaIsolationMode, data)
