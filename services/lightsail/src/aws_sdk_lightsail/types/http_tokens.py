"""Generated from Smithy shape ``com.amazonaws.lightsail#HttpTokens``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

HttpTokens: TypeAlias = Literal[
    "optional",
    "required",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "optional",
        "required",
    )
)


def serialize_aws_json_1_1(value: HttpTokens) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HttpTokens:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HttpTokens value: {data!r}")
    return cast(HttpTokens, data)
