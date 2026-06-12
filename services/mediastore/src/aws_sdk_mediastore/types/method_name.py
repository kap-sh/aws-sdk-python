"""Generated from Smithy shape ``com.amazonaws.mediastore#MethodName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediastore.errors import DeserializationError

MethodName: TypeAlias = Literal[
    "PUT",
    "GET",
    "DELETE",
    "HEAD",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUT",
        "GET",
        "DELETE",
        "HEAD",
    )
)


def serialize_aws_json_1_1(value: MethodName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MethodName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MethodName value: {data!r}")
    return cast(MethodName, data)
