"""Generated from Smithy shape ``com.amazonaws.firehose#ContentEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

ContentEncoding: TypeAlias = Literal[
    "NONE",
    "GZIP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "GZIP",
    )
)


def serialize_aws_json_1_1(value: ContentEncoding) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentEncoding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentEncoding value: {data!r}")
    return cast(ContentEncoding, data)
