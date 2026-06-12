"""Generated from Smithy shape ``com.amazonaws.iot#ThingConnectivityIndexingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ThingConnectivityIndexingMode: TypeAlias = Literal[
    "OFF",
    "STATUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "STATUS",
    )
)


def serialize_json(value: ThingConnectivityIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> ThingConnectivityIndexingMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ThingConnectivityIndexingMode value: {data!r}"
        )
    return cast(ThingConnectivityIndexingMode, data)
