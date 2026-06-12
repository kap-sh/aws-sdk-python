"""Generated from Smithy shape ``com.amazonaws.transfer#MapType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

MapType: TypeAlias = Literal[
    "FILE",
    "DIRECTORY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILE",
        "DIRECTORY",
    )
)


def serialize_aws_json_1_1(value: MapType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MapType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MapType value: {data!r}")
    return cast(MapType, data)
