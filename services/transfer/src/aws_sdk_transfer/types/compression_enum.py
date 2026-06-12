"""Generated from Smithy shape ``com.amazonaws.transfer#CompressionEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

CompressionEnum: TypeAlias = Literal[
    "ZLIB",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ZLIB",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: CompressionEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompressionEnum value: {data!r}")
    return cast(CompressionEnum, data)
