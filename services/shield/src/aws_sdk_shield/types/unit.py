"""Generated from Smithy shape ``com.amazonaws.shield#Unit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

Unit: TypeAlias = Literal[
    "BITS",
    "BYTES",
    "PACKETS",
    "REQUESTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BITS",
        "BYTES",
        "PACKETS",
        "REQUESTS",
    )
)


def serialize_aws_json_1_1(value: Unit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Unit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Unit value: {data!r}")
    return cast(Unit, data)
