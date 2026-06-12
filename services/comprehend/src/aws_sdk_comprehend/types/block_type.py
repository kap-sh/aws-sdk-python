"""Generated from Smithy shape ``com.amazonaws.comprehend#BlockType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

BlockType: TypeAlias = Literal[
    "LINE",
    "WORD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINE",
        "WORD",
    )
)


def serialize_aws_json_1_1(value: BlockType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BlockType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockType value: {data!r}")
    return cast(BlockType, data)
