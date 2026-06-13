"""Generated from Smithy shape ``com.amazonaws.odb#OpenMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

OpenMode: TypeAlias = Literal[
    "READ_ONLY",
    "READ_WRITE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ_ONLY",
        "READ_WRITE",
    )
)


def serialize_aws_json_1_0(value: OpenMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpenMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenMode value: {data!r}")
    return cast(OpenMode, data)
