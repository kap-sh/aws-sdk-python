"""Generated from Smithy shape ``com.amazonaws.glue#PropertyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

PropertyType: TypeAlias = Literal[
    "USER_INPUT",
    "SECRET",
    "READ_ONLY",
    "UNUSED",
    "SECRET_OR_USER_INPUT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER_INPUT",
        "SECRET",
        "READ_ONLY",
        "UNUSED",
        "SECRET_OR_USER_INPUT",
    )
)


def serialize_aws_json_1_1(value: PropertyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropertyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropertyType value: {data!r}")
    return cast(PropertyType, data)
