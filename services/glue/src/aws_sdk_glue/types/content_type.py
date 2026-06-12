"""Generated from Smithy shape ``com.amazonaws.glue#ContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ContentType: TypeAlias = Literal[
    "APPLICATION_JSON",
    "URL_ENCODED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLICATION_JSON",
        "URL_ENCODED",
    )
)


def serialize_aws_json_1_1(value: ContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentType value: {data!r}")
    return cast(ContentType, data)
