"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#IteratorPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_keyspacesstreams.errors import DeserializationError

IteratorPosition: TypeAlias = Literal[
    "AT_TIP",
    "BEHIND_TIP",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AT_TIP",
        "BEHIND_TIP",
    )
)


def serialize_aws_json_1_0(value: IteratorPosition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IteratorPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IteratorPosition value: {data!r}")
    return cast(IteratorPosition, data)
