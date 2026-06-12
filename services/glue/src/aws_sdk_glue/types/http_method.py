"""Generated from Smithy shape ``com.amazonaws.glue#HTTPMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

HTTPMethod: TypeAlias = Literal[
    "GET",
    "POST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GET",
        "POST",
    )
)


def serialize_aws_json_1_1(value: HTTPMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HTTPMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HTTPMethod value: {data!r}")
    return cast(HTTPMethod, data)
